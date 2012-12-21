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
#include "mccomposite/CompositeNeutronScatterer_Impl.h"


mccomposite::CompositeNeutronScatterer::CompositeNeutronScatterer
( const AbstractShape & shape, const scatterercontainer_t & scatterers, const geometer_t & geometer)
  : base_t( shape ),
    m_impl( new CompositeNeutronScatterer_Impl( shape, scatterers, geometer ) )
{
  set_max_multiple_scattering_number(4); // default max number of times of scattering
}


mccomposite::CompositeNeutronScatterer::~CompositeNeutronScatterer
()
{
}


void 
mccomposite::CompositeNeutronScatterer::scatter(mcni::Neutron::Event &ev)
{
  m_impl->scatter(ev);
}

void 
mccomposite::CompositeNeutronScatterer::scatterM
(const mcni::Neutron::Event &ev, mcni::Neutron::Events &evts)
{
  m_impl->scatterM(ev, evts);
}

mccomposite::CompositeNeutronScatterer::InteractionType
mccomposite::CompositeNeutronScatterer::interact_path1
(mcni::Neutron::Event &ev)
{
  m_impl->interact_path1( ev );
}

mccomposite::CompositeNeutronScatterer::InteractionType
mccomposite::CompositeNeutronScatterer::interactM_path1
(const mcni::Neutron::Event &ev, mcni::Neutron::Events &evts)
{
  m_impl->interactM_path1( ev, evts );
}

double
mccomposite::CompositeNeutronScatterer::calculate_attenuation
( const mcni::Neutron::Event &ev, const geometry::Position &end)
{
  m_impl->calculate_attenuation( ev, end );
}

void
mccomposite::CompositeNeutronScatterer::set_max_multiple_scattering_number
(unsigned int N)
{
  m_impl->max_scattering_loops = N;
}


// version
// $Id$

// End of file 
