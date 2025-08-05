// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <vector>
#include "mccomposite/CompositeNeutronScatterer_Impl.h"
#include "mccomposite/geometry/operations/Rotation.h"
#include "mccomposite/geometry/operations/Translation.h"
#include "mccomposite/geometry/intersect.h"
#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/neutron_propagation.h"

#include "mccomposite/vector2ostream.h"

namespace mccomposite {
  
  namespace CompositeNeutronScatterer_ImplDetails{
    
    char jrnltag[] = "CompositeNeutronScatterer_Impl";

    ///to save the temp shapes
    struct TempShapes {
      
      typedef const mccomposite::AbstractShape * Pointer;
      void add(Pointer ptr) { 
	pointers.push_back( ptr );
      }
      ~TempShapes( ) {
	for (size_t i=0; i<pointers.size(); i++) 
	  delete pointers[i];
      }
      std::vector< Pointer > pointers;
    };
    
    // helper functions
    /// transform position and direction vectors from global coord system
    /// to local coord system of an element. 
    /// The position of the element is given by "offset", 
    /// its orientation is specified by "rotmat".
    void global2local					\
    (mccomposite::geometry::Position & position, 
     mccomposite::geometry::Direction & direction, 
     const mccomposite::geometry::Vector & offset, 
     const mccomposite::geometry::RotationMatrix & rotmat)
    {
      position -= offset;
      mccomposite::geometry::RotationMatrix rotmatT = rotmat;
      rotmatT.transpose();
      
      position = rotmatT * position;
      direction = rotmatT * direction;
    }
    
    /// transform position and direction vectors from 
    /// local coord system of an element to the global coord system.
    /// The position of the element in the global coord system
    /// is given by "offset", 
    /// its orientation is specified by "rotmat".
    void local2global					\
    (mccomposite::geometry::Position & position, 
     mccomposite::geometry::Direction & direction, 
     const mccomposite::geometry::Vector & offset, 
     const mccomposite::geometry::RotationMatrix & rotmat)
    {
      position = rotmat * position;
      direction = rotmat * direction;
      position += offset;
    }
    
  }
}


struct mccomposite::CompositeNeutronScatterer_Impl::Details {
  
  // meta-methods
  Details( CompositeNeutronScatterer_Impl & i_target )
    : target(i_target)
  {}
  
  // methods
  /// remember a shape pointer
  void remember(const AbstractShape * ptr) { tempshapes.add(ptr); }
  
  /// transform a neutron event from global to local coord system in place
  void global2local
  ( mcni::Neutron::Event &ev, const AbstractNeutronScatterer & scatterer)
  {
    typedef CompositeNeutronScatterer_Impl::geometer_t Geometer;
    Geometer &geometer = target.m_geometer;
    const Geometer::position_t & position = geometer.getPosition( scatterer );
    const Geometer::orientation_t & orientation = geometer.getOrientation( scatterer );
    
    CompositeNeutronScatterer_ImplDetails::global2local
      ( ev.state.position, ev.state.velocity, position, orientation );
  }
  
  /// transform a neutron event from local to global coord system in place
  void local2global
  ( mcni::Neutron::Event &ev, const AbstractNeutronScatterer & scatterer)
  {
    typedef CompositeNeutronScatterer_Impl::geometer_t Geometer;
    Geometer &geometer = target.m_geometer;
    const Geometer::position_t & position = geometer.getPosition( scatterer );
    const Geometer::orientation_t & orientation = geometer.getOrientation( scatterer );
    
    CompositeNeutronScatterer_ImplDetails::local2global
      ( ev.state.position, ev.state.velocity, position, orientation );
  }
  
  /// transform a bunch of neutrons from local coord system to global 
  /// coord system
  void local2global
  ( mcni::Neutron::Events &evts, const AbstractNeutronScatterer & scatterer)
  {
    for (size_t i=0; i<evts.size(); i++)
      local2global( evts[i], scatterer );
  }
  
  CompositeNeutronScatterer_Impl & target;
  CompositeNeutronScatterer_ImplDetails::TempShapes tempshapes;
};


mccomposite::CompositeNeutronScatterer_Impl::CompositeNeutronScatterer_Impl
( const AbstractShape & shape, const scatterercontainer_t & scatterers, 
  const geometer_t & geometer )
  : 
  max_multiplescattering_loops_among_scatterers(5),
  max_multiplescattering_loops_interactM_path1(2),
  m_shape( shape ),
  m_scatterers( scatterers ),
  m_geometer( geometer ),
  m_details( new Details(*this) )
{
  for (size_t scatterer_index = 0; scatterer_index<m_scatterers.size(); 
       scatterer_index++) {
    
    const AbstractNeutronScatterer & scatterer = *m_scatterers[scatterer_index];
    
    const AbstractShape &shape = scatterer.shape();
    
    // we need to first rotate the shape
    geometry::Rotation * rotated = new geometry::Rotation
      (shape, m_geometer.getOrientation(scatterer) );
    m_details->remember( rotated );
    
    // and then translate it to the proper position
    const geometry::Position & position = m_geometer.getPosition(scatterer);
    geometry::Translation *translated = new geometry::Translation
      (*rotated, geometry::Vector(position[0], position[1], position[2]) );
    m_details->remember( translated );
    
    // now we can add the translated shape to my list of shapes
    m_shapes.push_back( translated );
  }

  m_union_of_all_shapes = geometry::Union( m_shapes );
}


mccomposite::CompositeNeutronScatterer_Impl::~CompositeNeutronScatterer_Impl
()
{
}


double
mccomposite::CompositeNeutronScatterer_Impl::calculate_attenuation
(const mcni::Neutron::Event & ev, const geometry::Position & end)
{
  using namespace CompositeNeutronScatterer_ImplDetails;

  double ret = 1.;
  mcni::Neutron::Event ev1;
  
  for (size_t scatterer_index=0; scatterer_index<m_scatterers.size(); 
       scatterer_index++) {

    AbstractNeutronScatterer & scatterer = *(m_scatterers[scatterer_index]);
    ev1 = ev;

    
    // convert to local coords
    m_details->global2local(ev1, scatterer);
    
    //
    ret *= scatterer.calculate_attenuation( ev1, end );
  }
  
  return ret;
}


mccomposite::CompositeNeutronScatterer_Impl::InteractionType
mccomposite::CompositeNeutronScatterer_Impl::interactM_path1
(const mcni::Neutron::Event & ev, mcni::Neutron::Events &evts)
{
  using namespace geometry;
  using namespace CompositeNeutronScatterer_ImplDetails;
  typedef int index_t;
  
  
  mcni::Neutron::Event ev1 = ev;
  
  // if the event is outside of my shape, propagate it to the surface
  if (locate(ev1, m_shape) == Locator::outside) {
    propagate_to_next_incident_surface( ev1, m_shape );
  }

  mcni::Neutron::Events to_be_scattered;
  to_be_scattered.push_back( ev1 );
  
  scatterer_interface::InteractionType itype;

  int nloop = 0;
  
  while (to_be_scattered.size()>0 && nloop++<max_multiplescattering_loops_interactM_path1) {
    
    mcni::Neutron::Events to_be_scattered2;
    
    for (size_t i=0; i<to_be_scattered.size(); i++) {
      
      // for each event
      const mcni::Neutron::Event & ev = to_be_scattered[i];
      
      // if the neutron probability is too low, skip
      if (ev.probability >= 0 && ev.probability < min_neutron_probability)
	continue;
      
      // find out if it hits a scatterer
      index_t scatterer_index = find_1st_hit<index_t>
	( ev.state.position, ev.state.velocity, m_shapes );
      
      
      // no hit, that event will go out. so add that to the out-list
      if (scatterer_index<0 or scatterer_index>=m_scatterers.size()) 
	{ evts.push_back(ev); continue; }
      
      // try to scatter the neutron off the 1st scatterer it hits
      // 1. the scattterer
      AbstractNeutronScatterer & scatterer = *(m_scatterers[scatterer_index]);
      
      
      // 2. the scattered neutrons will be stored here
      mcni::Neutron::Events newly_scattered;
      // 3. convert event to local coords
      mcni::Neutron::Event local_event = ev;
      m_details->global2local( local_event, scatterer );
      // 4. scatter
      itype = scatterer.interactM_path1( local_event, newly_scattered );
      
      // absorbed. nothing to do
      if (itype == scatterer_interface::absorption)
	continue;
      
      // if we reach here, that means we got some new neutrons
      // 1. convert neutrons back to global coordinate
      m_details->local2global( newly_scattered, scatterer );
      
      // 2. we need to check those neutrons. 
      // some of them may already exited first surface. we just need
      // to add to the out-list. The rest we need to deal with them
      // scatter them again.
      for (size_t new_neutron_index = 0; new_neutron_index < newly_scattered.size();
	   new_neutron_index++ ) {
	const mcni::Neutron::Event & ev = newly_scattered[new_neutron_index];
	
	
	// exited. add it to the out-list
	if (locate(ev, m_shape) != Locator::inside) { 
	    evts.push_back(ev); continue; 
	}
	
	// not exited. need to scatter again.
	to_be_scattered2.push_back( ev );
      }
      
    }
    
    // now swap to_be_scattered2 and to_be_scattered
    // so that to_be_scattered contains the new neutrons that need to 
    // be further scattered
    to_be_scattered.swap( to_be_scattered2 );
  }

  // there could be left-over neutrons 
  // we just propagate them to the next out-surface
  for (int i=0; i<to_be_scattered.size(); i++) {
    // 1. save the neutron
    mcni::Neutron::Event save = to_be_scattered[i];
    mcni::Neutron::Event &ev = to_be_scattered[i];
    // 2. propagate out
    propagate_to_next_exiting_surface( ev, m_shape );
    // 3. compute attenuation
    double attenuation = calculate_attenuation( save, ev.state.position );
    ev.probability *= attenuation;
    evts.push_back(ev);
  }
  
  // 
  if (evts.size() == 0) return scatterer_interface::absorption;
  return scatterer_interface::scattering;
}


void
mccomposite::CompositeNeutronScatterer_Impl::scatterM
(const mcni::Neutron::Event & ev, mcni::Neutron::Events &evts)
{
  using namespace CompositeNeutronScatterer_ImplDetails;
  using namespace geometry;
  typedef int index_t;
  
  
  mcni::Neutron::Events scattered;
  scattered.push_back( ev );
  
  scatterer_interface::InteractionType itype;
  
  int nloop = 0;
  // this is the loop that neutrons got bounced among scatterers
  // this is not the loop neutrons got bounced inside one scatterer.
  while (scattered.size()>0 && nloop++<max_multiplescattering_loops_among_scatterers) {
    
    mcni::Neutron::Events scattered2;
    

    // loop over neutrons and compute scattered and transmitted
    // neutrons and put them into scattered2
    for (size_t i=0; i<scattered.size(); i++) {
      
      // for each event
      const mcni::Neutron::Event & ev = scattered[i];

      // if the neutron probability is low, skip
      if (ev.probability >= 0 && ev.probability < min_neutron_probability)
	continue;
      
      // if the neutron is not moving, we don't have a way to deal with it
      if (! is_moving( ev ) ) continue;

      // find out if it intersects with this scatterer
      // if not, it should be let go.
      
      if (is_exiting( ev, m_shape ) ) {
	evts.push_back( ev ); continue; 
      }
      
      
      // try to scatter the neutron 
      itype = interactM_path1( ev, scattered2 );
      
      // if there is an event that does not really get scattered
      // we have a problem
      if (scattered2.size()==1) {
	mcni::Neutron::Event & ev2 = scattered2[0];
	// no worry about divide by zero, we test that above
	if (std::abs(ev2.probability-ev.probability)/ev.probability < 1e-5) {
	  // XXX: this is hackish. solve the problem
	  // XXX: by propagating neutron forward a little bit
	  propagate(ev2, 1e-7);
	}

      }

      // absorbed. nothing to do
      if (itype == scatterer_interface::absorption) continue;
    }
    
    // now swap scattered2 and scattered
    // so that scattered contains the new neutrons that need to 
    // be further scattered
    scattered.swap( scattered2 );

  } // end of while loop 
  
  // there could be left-over neutrons 
  // we just propagate them out of this scatterer and add attenuation
  for (int i=0; i<scattered.size(); i++) {
    // 1. save the neutron
    mcni::Neutron::Event save = scattered[i];
    mcni::Neutron::Event &ev = scattered[i];
    // 2. propagate out
    propagate_out( ev, m_shape );
    // 3. compute attenuation
    double attenuation = calculate_attenuation( save, ev.state.position );
    ev.probability *= attenuation;
    evts.push_back(ev);
  }
  
  return;
}



mccomposite::CompositeNeutronScatterer_Impl::InteractionType
mccomposite::CompositeNeutronScatterer_Impl::interact_path1
(mcni::Neutron::Event & ev)
{
  using namespace CompositeNeutronScatterer_ImplDetails;
  
  using namespace geometry;
  
  
  int scatterer_index = find_1st_hit<int>
    ( ev.state.position, ev.state.velocity, m_shapes );

  // nothing hit. should just let go the neutron
  if (scatterer_index < 0 or scatterer_index >= m_scatterers.size() ) {
    propagate_to_next_exiting_surface( ev, m_shape );
    return scatterer_interface::none;
  }

  // the scatterer
  AbstractNeutronScatterer & scatterer = *(m_scatterers[scatterer_index]);
  // need to convert event to local coords before scattering
  mcni::Neutron::Event local_event = ev;
  m_details->global2local(local_event, scatterer);
  // delegate the scaterer to deal with the neutron
  scatterer_interface::InteractionType itype = scatterer.interact_path1( local_event );
  
  // this means that the neutron is absorbed
  if (itype == scatterer_interface::absorption) {
    ev.probability = -1;
    return itype;
  }
  
  // now we need to convert back coordinate
  m_details->local2global( local_event, scatterer );
  ev = local_event;
  
  // if the neutron just passed the scatterer without scattering
  if (itype == scatterer_interface::none) {
    // if the neutron already at exiting surface or outside
    // the scatterer, nothing need to be done
    if (locate(ev, m_shape)!=geometry::Locator::inside)
      return itype;
    // if still insdie the composite, 
    // then we need to do scattering again
    return interact_path1( ev );
  }
  
  // when we reach here, this means the event was scattered. 
  // we just need to attenuate the outgoing event
  // and propagate neutron out.
  // 1. save the neutron
  mcni::Neutron::Event save = ev;
  // 2. propagate to surface if necessary
  if (locate(ev, m_shape) == Locator::inside) 
    propagate_to_next_exiting_surface( ev, m_shape );
  // 3. compute attenuation
  double attenuation = calculate_attenuation( save, ev.state.position );
  ev.probability *= attenuation;
  
  return scatterer_interface::scattering;
}


void
mccomposite::CompositeNeutronScatterer_Impl::scatter
(mcni::Neutron::Event & ev)
{
  using namespace CompositeNeutronScatterer_ImplDetails;

  using namespace geometry;

  // if the neutron is not moving, we don't have a way to deal with it
  if (! is_moving( ev ) ) {
    ev.probability = -1; return;
  }
      
  // event is exiting, nothing need to be done
  if (is_exiting(ev, m_shape)) {
    return;
  }
  // event does not really hit me, return
  // this is necessarily because the given "frame shape" of this composite
  // might not be the union of all element shapes. 
  // so the event might hit the "frame shape", but not really any scatterer
  if (is_exiting(ev, m_union_of_all_shapes)) {
    propagate_to_next_exiting_surface( ev, m_shape );
    return;
  }

  // otherwise, interacts once.
  scatterer_interface::InteractionType itype = interact_path1( ev );
  
  // if it is absorbed or it does not hit anything. we don't
  // need do more.
  if (itype == scatterer_interface::absorption) {
    return;
  }

  if (itype == scatterer_interface::none) {
    // need to call scatter again
    propagate_to_next_incident_surface( ev, m_union_of_all_shapes );
    scatter( ev );
    return;
  }
  
  // when we reach here, this means the event was scattered. 
  // we still need to attenuate the outgoing event
  // 1. find intersections
  tofs_t tofs = intersect(ev, m_shape);
  
  // 2. no intersection. nothing to do
  if (tofs.size()==0) {
    return;
  }

  // 3. with intersection. propagate to the last intersection and 
  // attenuate the neutron.
  // 3a. save the neutron
  mcni::Neutron::Event save = ev;
  // 2. propagate out
  propagate_out( ev, m_shape );
  // 3. compute attenuation
  double attenuation = calculate_attenuation( save, ev.state.position );
  ev.probability *= attenuation;
  
  return;
}

// version
// $Id$

// End of file 
