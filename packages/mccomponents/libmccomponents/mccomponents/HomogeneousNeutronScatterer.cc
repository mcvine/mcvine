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

#include "mccomponents/HomogeneousNeutronScatterer.h"
#include "mccomponents/AbstractScatteringKernel.h"
#include "mccomposite/geometry/visitors/Locator.h"


mccomponents::HomogeneousNeutronScatterer::~HomogeneousNeutronScatterer
()
{
}


mccomponents::HomogeneousNeutronScatterer::HomogeneousNeutronScatterer
( const AbstractShape & shape, AbstractScatteringKernel & kernel,
  const Weights & weights)
  : base_t( shape ),
    m_kernel( kernel ),
    m_weights( weights )
{
}


mccomponents::HomogeneousNeutronScatterer::InteractionType
mccomponents::HomogeneousNeutronScatterer::interact_path1(mcni::Neutron::Event &ev)
{
  using namespace mccomposite;
  
  // first we need to find where we are
  geometry::Locator::Location location = locate( ev, shape() );

  // if the neutron is already in this shape, we are good
  // but if it is outside, we need to propagate to the front surface 
  // of the shape.
  if (location != geometry::Locator::inside ) 
    propagate_to_next_incident_surface(ev, shape());

  double tof = tof_before_exit( ev, shape() );

  double distance = tof*ev.state.velocity.length();
  
  double mu = m_kernel.absorption_coefficient( ev );
  double sigma = m_kernel.scattering_coefficient( ev );

  double transmission_prob = std::exp( -(mu+sigma)*distance );
  double absorption_prob = (1-transmission_prob)*(mu/(mu+sigma));
  double scattering_prob = (1-transmission_prob)*(sigma/(mu+sigma));
  
  double allocated_for_transmission = transmission_prob * m_weights.transmission;
  double allocated_for_absorption = absorption_prob * m_weights.absorption;
  double allocated_for_scattering = scattering_prob * m_weights.scattering;

  double sum = allocated_for_scattering + allocated_for_absorption + allocated_for_transmission;
  
  allocated_for_transmission/=sum;
  allocated_for_absorption/= sum;
  allocated_for_scattering/= sum;
}


mccomponents::HomogeneousNeutronScatterer::InteractionType 
mccomponents::HomogeneousNeutronScatterer::interactM_path1
(const mcni::Neutron::Event &, mcni::Neutron::Events &)
{
}

double
mccomponents::HomogeneousNeutronScatterer::calculate_attenuation
( const mcni::Neutron::Event &ev, const mccomposite::geometry::Position &end)
{
}


// version
// $Id$

// End of file 
