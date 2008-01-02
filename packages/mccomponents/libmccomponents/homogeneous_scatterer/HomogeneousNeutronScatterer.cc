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

#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomposite/neutron_propagation.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


namespace mccomponents {
  namespace HomogeneousNeutronScatterer_Impl {
    char jrnltag [] = "HomogeneousNeutronScatterer";
  }
}


const double mccomponents::HomogeneousNeutronScatterer::minimum_neutron_event_probability = 1.e-20;


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
  Location location = locate( ev, shape() );

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


void 
mccomponents::HomogeneousNeutronScatterer::_interactM1
(const mcni::Neutron::Event &ev, mcni::Neutron::Events & evts)
{
#ifdef DEBUG
  journal::debug_t debug(HomogeneousNeutronScatterer_Impl::jrnltag);
#endif

//   std::cout << "_interactM1: " 
// 	    << "input neutron = " << ev << ", "
// 	    << "container of output neutrons = " << evts
// 	    << std::endl;

  using namespace mccomposite;

  mcni::Neutron::Event original = ev, ev1;
  
  // first we need to find where we are
  Location location = locate( original, shape() );

  // if the neutron is already in this shape, we are good
  // but if it is outside, we need to propagate to the front surface 
  // of the shape.
  if (location != geometry::Locator::inside ) 
    propagate_to_next_incident_surface(original, shape());

  // tof before exiting the shape for the first time
  double tof = tof_before_exit( original, shape() );

  // neutron velocity
  double velocity = original.state.velocity.length();
  // distance of flight
  double distance = tof*original.state.velocity.length();
  
  // absorption
  double mu = m_kernel.absorption_coefficient( original );
  // scattering
  double sigma = m_kernel.scattering_coefficient( original );

  // probability of three interaction types happening
  double transmission_prob = std::exp( -(mu+sigma)*distance );
  double absorption_prob = (1-transmission_prob)*(mu/(mu+sigma));
  //  double scattering_prob = (1-transmission_prob)*(sigma/(mu+sigma));

  // now we need to do transmission, absorption, and scattering, respectively
  
  // transmission
  ev1 = original;
  propagate_to_next_exiting_surface( ev1, shape() );
  ev1.probability *= transmission_prob;
  evts.push_back( ev1 );

//   std::cout << "1. evts = " << evts << std::endl;
  
  // absorption
  ev1 = original;
  ev1.probability *= absorption_prob;
  m_kernel.absorb( ev1 );

//   std::cout << "2. evts = " << evts << std::endl;

  // scattering
  ev1 = original;
  double x = m_randomnumbergenerator.generate(0, distance);
  double prob = sigma * distance * std::exp( -(mu+sigma) * x );
  ev1.probability *= prob;
  propagate( ev1, x/velocity );
  m_kernel.scatter( ev1 );
  evts.push_back( ev1 );

//   std::cout << "3. evts = " << evts << std::endl;

//   std::cout << "_interactM1: " 
// 	    << "outputs neutrons = " << evts
// 	    << std::endl;


}



mccomponents::HomogeneousNeutronScatterer::InteractionType 
mccomponents::HomogeneousNeutronScatterer::interactM_path1
(const mcni::Neutron::Event &ev, mcni::Neutron::Events &evts)
{
  using namespace mccomposite;

  mcni::Neutron::Events to_be_scattered, scattered;
  to_be_scattered.push_back(ev);

  while (to_be_scattered.size()) {

//     std::cout << "interactM_path1: "
// 	      << "to_be_scattered = " << to_be_scattered
// 	      << std::endl;
    
    mcni::Neutron::Events to_be_scattered2;

    for (size_t neutron_index = 0; neutron_index < to_be_scattered.size(); neutron_index++) {
      
      const mcni::Neutron::Event & ev1 = to_be_scattered[neutron_index];
      
      scattered.clear();
      // interact once
      _interactM1( ev1, scattered );
      
      // loop over scattered neutron and deal with each of them
      for (size_t scattered_neutron_index = 0;
	   scattered_neutron_index < scattered.size();
	   scattered_neutron_index ++ ) {
	
	const mcni::Neutron::Event & ev2 = scattered[ scattered_neutron_index ];
	
	// if the probability is too low, we just absorb it and done
	if (ev2.probability < minimum_neutron_event_probability) {
	  // nothing to do actually
	  continue;
	}

	// if it is on border or outside, we are done with it here
	if (locate(ev2, shape()) != geometry::Locator::inside) {
	  evts.push_back( ev2 );
	  continue;
	}
	
	// this means the event is inside the scatterer
	// add this event to a new "to-be-scattered" list
	to_be_scattered2.push_back( ev2 );
	
      } // loop over scattered neutrons

    } // loop over neutrons to be scattered
    
    to_be_scattered2.swap( to_be_scattered );
    
  } // while there are still neutrons to be scattered
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
