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


#ifdef DEBUG
#include "journal/debug.h"
#endif


namespace mccomponents {
  namespace HomogeneousNeutronScatterer_Impl {
    char jrnltag [] = "HomogeneousNeutronScatterer";
  }
}


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


mccomponents::HomogeneousNeutronScatterer::HomogeneousNeutronScatterer
( const AbstractShape & shape, AbstractScatteringKernel & kernel,
  const Weights & weights,
  double seed)
  : base_t( shape ),
    m_kernel( kernel ),
    m_weights( weights ),
    m_randomnumbergenerator( seed )
{
}


mccomponents::HomogeneousNeutronScatterer::InteractionType
mccomponents::HomogeneousNeutronScatterer::interact_path1(mcni::Neutron::Event &ev)
{
#ifdef DEBUG
  journal::debug_t debug(HomogeneousNeutronScatterer_Impl::jrnltag);
#endif

  using namespace mccomposite;
  
  // first we need to find where we are
  geometry::Locator::Location location = locate( ev, shape() );

  // if the neutron is already in this shape, we are good
  // but if it is outside, we need to propagate to the front surface 
  // of the shape.
  if (location != geometry::Locator::inside ) 
    propagate_to_next_incident_surface(ev, shape());

  // tof before exiting the shape for the first time
  double tof = tof_before_exit( ev, shape() );

  // neutron velocity
  double velocity = ev.state.velocity.length();
  // distance of flight
  double distance = tof*ev.state.velocity.length();
  
  // absorption
  double mu = m_kernel.absorption_coefficient( ev );
  // scattering
  double sigma = m_kernel.scattering_coefficient( ev );

  // probability of three interaction types happening
  double transmission_prob = std::exp( -(mu+sigma)*distance );
  double absorption_prob = (1-transmission_prob)*(mu/(mu+sigma));
  //double scattering_prob = (1-transmission_prob)*(sigma/(mu+sigma));
  
  // toss a dice and decide whether we should do transmission, absorption,
  // or scattering
  double transmission_mark = m_weights.transmission;
  double absorption_mark = transmission_mark + m_weights.absorption;
  double sum_of_weights = absorption_mark + m_weights.scattering;

  double r = m_randomnumbergenerator.generate(0, sum_of_weights);
  
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< "random number = " << r
	<< "marks = " << transmission_mark << ", "
	<< absorption_mark << ", "
	<< sum_of_weights 
	<< journal::endl;
#endif

  if (r < transmission_mark) {
    // transmission
    propagate_to_next_exiting_surface( ev, shape() );
    ev.probability *= transmission_prob * (sum_of_weights/m_weights.transmission);
    return base_t::none;
  }
  
  if (r >= transmission_mark && r < absorption_mark ) {
    // absorption
    ev.probability *= absorption_prob * (sum_of_weights/m_weights.absorption);
    m_kernel.absorb( ev );
    ev.probability = -1;
    return base_t::absorption;
  }

  if (r >= absorption_mark) {
    // scattering
    double x = m_randomnumbergenerator.generate(0, distance);
    double prob = sigma * distance * std::exp( -(mu+sigma) * x );
    ev.probability *= prob * (sum_of_weights/m_weights.scattering);
    propagate( ev, x/velocity );
    m_kernel.scatter( ev );
    mcni::Neutron::Event save = ev;
    propagate_to_next_exiting_surface( ev, shape() );
    ev.probability *= calculate_attenuation( save, ev.state.position );
    return base_t::scattering;
  }
  
  throw Exception("should not reach here");
}


mccomponents::HomogeneousNeutronScatterer::InteractionType 
mccomponents::HomogeneousNeutronScatterer::interactM_path1
(const mcni::Neutron::Event &, mcni::Neutron::Events &)
{
  return base_t::scattering;
}


double
mccomponents::HomogeneousNeutronScatterer::calculate_attenuation
( const mcni::Neutron::Event &ev, const mccomposite::geometry::Position &end)
{
  const mccomposite::geometry::Position &start = ev.state.position;

  double length = (end-start).length();

  double mu = m_kernel.absorption_coefficient( ev );
  double sigma = m_kernel.scattering_coefficient( ev );

  return std::exp( - (mu+sigma) * length );
}


// version
// $Id$

// End of file 
