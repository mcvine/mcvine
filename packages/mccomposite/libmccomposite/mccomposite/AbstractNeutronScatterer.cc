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
#include "mccomposite/CompositeNeutronScatterer_Impl.h"


struct mccomposite::AbstractNeutronScatterer::Details {
  Details( AbstractNeutronScatterer & scatterer ) 
  {
    scatterers.push_back( &scatterer );
    composite = std::auto_ptr<CompositeNeutronScatterer_Impl> 
      (new CompositeNeutronScatterer_Impl
       ( scatterer.shape(), scatterers, geometer ) 
       );
  }

  CompositeNeutronScatterer_Impl::scatterercontainer_t scatterers;
  CompositeNeutronScatterer_Impl::geometer_t geometer;
  std::auto_ptr<CompositeNeutronScatterer_Impl> composite;
};



mccomposite::AbstractNeutronScatterer::AbstractNeutronScatterer
(const AbstractShape & shape)
  : m_shape( shape ),
    m_details( new Details(*this) )
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
  m_details->composite->scatter( ev );
}

double
mccomposite::AbstractNeutronScatterer::calculate_attenuation
(const mcni::Neutron::Event & ev, const geometry::Position & end) const
{
  return 1.;
}

void
mccomposite::AbstractNeutronScatterer::scatterM
(const mcni::Neutron::Event & ev, mcni::Neutron::Events &evts)
{
  m_details->composite->scatterM(ev, evts);
}

mccomposite::AbstractNeutronScatterer::InteractionType
mccomposite::AbstractNeutronScatterer::interactM_path1
(const mcni::Neutron::Event & ev, mcni::Neutron::Events &evts)
{
  mcni::Neutron::Event newev = ev;
  InteractionType ret = interact_path1(newev);
  evts.push_back( newev );
  return ret;
}

void
mccomposite::AbstractNeutronScatterer::print(std::ostream &os) const {
  os << "mccomposite::AbstractNeutronScatterer()";
}

std::ostream & operator<< (std::ostream &os, const mccomposite::AbstractNeutronScatterer & scatterer)
{
  scatterer.print(os);
}


// version
// $Id$

// End of file 
