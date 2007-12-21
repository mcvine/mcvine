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


#include "mccomposite/AbstractNeutronScatterer.h"

mccomposite::AbstractNeutronScatterer::AbstractNeutronScatterer
(const AbstractShape & shape)
  : m_shape( shape )
{
}

mccomposite::AbstractNeutronScatterer::~AbstractNeutronScatterer
()
{
}

const mccomposite::AbstractShape & mccomposite::AbstractNeutronScatterer::shape
() const
{
  return m_shape;
}

void
mccomposite::AbstractNeutronScatterer::scatter
(mcni::Neutron::Event & ev)
{
  interact( ev );
}

void
mccomposite::AbstractNeutronScatterer::attenuate
(mcni::Neutron::Event & ev)
{
}

void
mccomposite::AbstractNeutronScatterer::scatterM
(const mcni::Neutron::Event & ev, mcni::Neutron::Events &evts)
{
  interactM( ev, evts );
}

mccomposite::AbstractNeutronScatterer::InteractionType
mccomposite::AbstractNeutronScatterer::interactM
(const mcni::Neutron::Event & ev, mcni::Neutron::Events &evts)
{
  mcni::Neutron::Event newev = ev;
  InteractionType ret = interact(newev);
  evts.push_back( newev );
  return ret;
}



// version
// $Id: AbstractNeutronScatterer.cc 591 2006-09-25 07:17:26Z linjiao $

// End of file 
