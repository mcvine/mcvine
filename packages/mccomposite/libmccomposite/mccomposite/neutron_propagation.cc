// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include "mccomposite/exception.h"
#include "mccomposite/neutron_propagation.h"


namespace mccomposite {

  void propagate_to_next_exiting_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape)
  {
    double t; // the result
    tofs_t tofs;

    // where is the point of start relative to the shape?
    geometry::Locator::Location location = locate(ev, shape);

    // if inside, the next intersection must be what we want
    if (location == geometry::Locator::inside) {

      tofs = forward_intersect( ev, shape );
      if (tofs.size() == 0) throw Exception("not intersections");
      t = tofs[0];

    } else {

      // if outside, let us propagate the event to the front
      // surface of the shape
      if (location == geometry::Locator::outside) {
	propagate_to_next_incident_surface( ev, shape );
      }
      tofs = forward_intersect( ev, shape );

      // here, the event must be at the front surface of the shape.
      if (locate(ev, shape) != geometry::Locator::onborder) 
	throw Exception("event not at the front surface");

      // we need to find the first intersection that is not really 
      // the same point as the start point
      bool found = 0;
      for (size_t intersection_index=0; intersection_index<tofs.size(); 
	   intersection_index++) {
	geometry::Position middlepoint =\
	  ev.state.position + tofs[intersection_index] * 0.5 * ev.state.velocity;

	location = geometry::locate(middlepoint, shape);

	if (location == geometry::Locator::outside) 
	  // this means the starting point is already at the 
	  // exiting surface. nothing to do
	  return;
	if (location== geometry::Locator::inside)
	  { t = tofs[intersection_index]; found = 1; break; }
      }
      if (! found ) return;
    }
    propagate( ev, t );
  }


  void propagate_to_next_incident_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape)
  {
    double t;

    // if neutron is already inside the shape
    // throw exception
    geometry::Locator::Location location = locate(ev, shape);
    if (location==geometry::Locator::inside)
      throw Exception("neutron is already inside the shape");
    
    // get intersections
    tofs_t tofs = forward_intersect( ev, shape );
    if (tofs.size()==0) return;

    // if neutron is outside the shape, it is easy
    if (location == geometry::Locator::outside)
      t = tofs[0];
    else {
      // at border.
      // we need to find the first intersection that is not really 
      // the same point as the start point
      bool found = 0;
      for (size_t intersection_index=0; intersection_index<tofs.size(); intersection_index++) {
	geometry::Position middlepoint =\
	  ev.state.position + tofs[intersection_index] * 0.5 * ev.state.velocity;

	location = geometry::locate(middlepoint, shape);
	
	if (location == geometry::Locator::inside) 
	  // this means the starting point is already at the 
	  // incident surface. nothing to do
	  return;
       
	if (location == geometry::Locator::outside)
	  { t = tofs[intersection_index]; found = 1; break; }
      }
      if (! found ) return;
    }
    propagate( ev, t );
  }

  double tof_before_exit
  ( const mcni::Neutron::Event & ev, const geometry::AbstractShape & shape)
  {
    double t;

    geometry::Locator::Location location = locate(ev, shape);
    if (location == geometry::Locator::outside)
      throw Exception("neutron outside of shape");

    tofs_t tofs = forward_intersect( ev, shape );

    if (tofs.size()==0) throw Exception( "no intersection" );

    // inside, easy
    if (location == geometry::Locator::inside)
      return tofs[0];

    // need to find the first intersection that is not
    // essentially the same as the starting point.
    bool found = 0;

    for (size_t intersection_index=0; intersection_index<tofs.size(); 
	 intersection_index++) {

      geometry::Position middlepoint =\
	ev.state.position + tofs[intersection_index] * 0.5 * ev.state.velocity;

      location = geometry::locate(middlepoint, shape);
	
      if (location == geometry::Locator::outside) 
	return 0;
       
      if (location == geometry::Locator::inside)
	{ t = tofs[intersection_index]; found = 1; break; }
    }

    if (!found) t = 0;
    
    return t;
  }


  bool is_exiting
  ( const mcni::Neutron::Event & ev, const geometry::AbstractShape & shape)
  {
    Location location = locate(ev, shape);

    // if event is still inside the shape, it is not exiting
    if (location==geometry::Locator::inside) return 0;

    tofs_t tofs = forward_intersect( ev, shape );

    // if no interactions, that means the event is already exiting
    if (tofs.size() == 0) return 1;

    // if event is outside the shape, but will hit the shape again, it 
    // does not count as exiting
    if (location==geometry::Locator::outside && tofs.size() > 0 ) return 0;

    // if we reach here, the neutron is on surface. 
    // we are almost certain it is exiting. one more test need to be done,
    // however. we need to make sure all intersections are simply 
    // trivial repetition of the same surface.
    double previous = 0;
    for (size_t tof_index =0; tof_index < tofs.size(); tof_index++) {
      double now = tofs[tof_index];
      double middle = (previous + now)/2.;
      if (geometry::locate(ev.state.position + middle * ev.state.velocity, 
			   shape) != geometry::Locator::onborder )
	return 0;
      previous = now;
    }
    
    return 1;
  }

  bool is_moving (const mcni::Neutron::Event &ev)
  {
    static const double minimum_velocity = 1.e-6; // typical thermal neutron are 10^3 m/s
    return (ev.state.velocity.length()>minimum_velocity);
  }

}


// version
// $Id$

// End of file 
