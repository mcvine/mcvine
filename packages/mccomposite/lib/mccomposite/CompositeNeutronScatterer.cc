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


#include <sstream>
#include "mccomposite/CompositeNeutronScatterer.h"
#include "mccomposite/CompositeNeutronScatterer_Impl.h"
#include "mccomposite/geometry/visitors/BoundingBoxMaker.h"
#include "mccomposite/geometry/overlap.h"
#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/exception.h"

mccomposite::CompositeNeutronScatterer::CompositeNeutronScatterer
( const AbstractShape & shape, const scatterercontainer_t & scatterers, const geometer_t & geometer)
  : base_t( shape ),
    m_impl( new CompositeNeutronScatterer_Impl( shape, scatterers, geometer ) )
{
  set_max_multiplescattering_loops_among_scatterers(5); // default max number of times of scattering
  set_max_multiplescattering_loops_interactM_path1(1);
  set_min_neutron_probability(0);
}


mccomposite::CompositeNeutronScatterer::~CompositeNeutronScatterer
()
{
}

void mccomposite::CompositeNeutronScatterer::checkShapeOverlap() const
{
  const scatterercontainer_t & scatterers = m_impl->m_scatterers;
  geometry::BoundingBoxMaker bbm;
  size_t N = 100;
  for (size_t i=0; i<scatterers.size(); i++) {
    AbstractNeutronScatterer *s = scatterers[i];
    geometry::BoundingBox bb = bbm.make(s->shape());
    for (size_t j=i+1; j<scatterers.size(); j++) {
      if (geometry::hasOverlap(s->shape(), scatterers[j]->shape(), bb, N)) {
	std::ostringstream oss;
	oss << "Overlapping shapes: " << std::endl
	    << "  - shape 1: " << s->shape() << std::endl
	    << "  - shape 2: " << scatterers[j]->shape() << std::endl
	  ;
	throw Exception(oss.str());
      }
    }
  }
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
mccomposite::CompositeNeutronScatterer::set_max_multiplescattering_loops_among_scatterers
(unsigned int N)
{
  m_impl->max_multiplescattering_loops_among_scatterers = N;
}

unsigned int
mccomposite::CompositeNeutronScatterer::get_max_multiplescattering_loops_among_scatterers
()
{
  return m_impl->max_multiplescattering_loops_among_scatterers;
}

void
mccomposite::CompositeNeutronScatterer::set_max_multiplescattering_loops_interactM_path1
(unsigned int N)
{
  m_impl->max_multiplescattering_loops_interactM_path1 = N;
}

unsigned int
mccomposite::CompositeNeutronScatterer::get_max_multiplescattering_loops_interactM_path1
()
{
  return m_impl->max_multiplescattering_loops_interactM_path1;
}

void
mccomposite::CompositeNeutronScatterer::set_min_neutron_probability
(float_t p)
{
  m_impl->min_neutron_probability = p;
}

mccomposite::CompositeNeutronScatterer::float_t
mccomposite::CompositeNeutronScatterer::get_min_neutron_probability
()
{
  return m_impl->min_neutron_probability;
}

void
mccomposite::CompositeNeutronScatterer::print(std::ostream &os) const {
  os << "mccomposite::CompositeNeutronScatterer()";
}


// version
// $Id$

// End of file 
