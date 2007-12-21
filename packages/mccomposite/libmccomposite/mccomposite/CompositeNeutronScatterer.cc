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


#include "mccomposite/CompositeNeutronScatterer.h"
#include "mccomposite/geometry/operations/Union.h"
#include "mccomposite/geometry/intersect.h"


mccomposite::CompositeNeutronScatterer::CompositeNeutronScatterer
(const AbstractShape & shape, const scatterercontainer_t & scatterers)
  : AbstractNeutronScatterer( shape ),
    m_scatterers( scatterers )
{
  for (size_t i = 0; i<m_scatterers.size(); i++) {
    m_shapes.push_back( &(m_scatterers[i]->shape()) );
  }
}


mccomposite::CompositeNeutronScatterer::~CompositeNeutronScatterer
()
{
}


void
mccomposite::CompositeNeutronScatterer::attenuate
(mcni::Neutron::Event & ev)
{
  for (size_t i=0; i<m_scatterers.size(); i++) 
    m_scatterers[i]->attenuate( ev );
}


mccomposite::CompositeNeutronScatterer::InteractionType
mccomposite::CompositeNeutronScatterer::interactM
(const mcni::Neutron::Event & ev, mcni::Neutron::Events &evts)
{
  using namespace geometry;

  int i = find_1st_hit<int>( ev.state.position, ev.state.velocity, m_shapes );
  // nothing hit. should just let go the neutron
  if (i<0 or i>m_scatterers.size()) return base_t::none;
  
  mcni::Neutron::Events scattered;

  // delegate the scaterer to deal with the neutron
  base_t::InteractionType itype = m_scatterers[i]->interactM( ev, scattered );

  // this means that the neutron is absorbed
  if (itype == absorption) return itype;
  
  while (scattered.size()>0) {

    mcni::Neutron::Events scattered2;

    for (size_t i=0; i<scattered.size(); i++) {

      // for each event
      const mcni::Neutron::Event & ev = scattered[i];

      // find out if it hits a scatterer
      i = find_1st_hit<int>( ev.state.position, ev.state.velocity, m_shapes );

      // no hit, that event will go out. so add that to the out-list
      if (i<0 or i>m_scatterers.size()) 
	{ evts.push_back(ev); continue; }
      
      // try to scatter the neutron off the 1st scatterer it hits
      mcni::Neutron::Events newly_scattered;
      itype = m_scatterers[i]->interactM( ev, newly_scattered );
      
      // absorbed. nothing to do
      if (itype == absorption) continue;

      // if we reach here, that means we go some new neutrons
      // add those neutrons to the scattered2 list
      copy( newly_scattered.begin(), newly_scattered.end(), back_inserter(scattered2));
      
    }
    
    // now swap scattered2 and scattered
    // so that scattered contains the new neutrons that need to 
    // be further scattered
    scattered.swap( scattered2 );
  }
}

mccomposite::CompositeNeutronScatterer::InteractionType
mccomposite::CompositeNeutronScatterer::interact
(mcni::Neutron::Event & ev)
{
  using namespace geometry;

  int i = find_1st_hit<int>( ev.state.position, ev.state.velocity, m_shapes );

  // nothing hit. should just let go the neutron
  if (i<0 or i>m_scatterers.size()) return base_t::none;
  
  // delegate the scaterer to deal with the neutron
  base_t::InteractionType itype = m_scatterers[i]->interact( ev );

  // this means that the neutron is absorbed
  if (itype == absorption) {
    ev.probability = -1;
    return itype;
  }
  
  // if the neutron just passed the scatterer without scattering
  if (itype == none) {
    // then we need to do scattering again
    return interact( ev );
  }

  // when we reach here, this means the event was scattered. 
  // we just need to attenuate the outgoing event
  attenuate( ev );
  return scattering;
}

// version
// $Id: CompositeNeutronScatterer.cc 591 2006-09-25 07:17:26Z linjiao $

// End of file 
