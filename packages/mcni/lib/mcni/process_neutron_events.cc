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



#include "mcni/neutron.h"

#include "mcni/AbstractNeutronScatterer.h"
#include "mcni/process_neutron_events.h"
#include "mcni/exceptions.h"

#include <numeric>
#include <functional>
#include <algorithm>


namespace {

  template <class NC>
  void _process_T
  (NC *nc, mcni::Neutron::Events &evts)
  {
    using namespace mcni;

    static Neutron::Event swap_temp;
    
    size_t nn = evts.size();
    
    for (size_t index=0; index<nn; ) {
      
      Neutron::Event &ev = evts[index];
      
      nc->scatter( ev ); 
      if (ev.probability < 0) {
	// swap the current event with the last event
	swap_temp = evts[index];
	evts[index] = evts[nn-1];
	evts[nn-1] = swap_temp;
	nn --;
      } else {
	index ++;
      }
      
    }

    // remove the absorbed neutron events
    evts.erase( evts.begin() + nn, evts.end() );
  }

  struct WasAbsorbed : public std::unary_function<const mcni::Neutron::Event &, bool> {
    bool operator() (const mcni::Neutron::Event & event)
    {
      return event.probability<0.;
    }
  };
  
  template <class NC>
  void _processM_T
  (NC *nc, mcni::Neutron::Events &evts)
  {
    using namespace mcni;
    using namespace std;

    static Neutron::Event swap_temp;
    static Neutron::Events scattered;
    static WasAbsorbed wasAbsorbed;
    Neutron::Events ret;
    
    size_t nn = evts.size();
    
    for (size_t index=0; index<nn; index++) {

      Neutron::Event &ev = evts[index];
      scattered.clear();
      nc->scatterM( ev, scattered );

      remove_copy_if(scattered.begin(), scattered.end(),
		     back_inserter(ret),
		     wasAbsorbed);
    }
    
    evts.swap( ret );
  }
  
}

void mcni::process
(AbstractNeutronScatterer &nc, Neutron::Events &buffer)
{
  _process_T<AbstractNeutronScatterer>( &nc, buffer );
}

void mcni::processM
(AbstractNeutronScatterer &nc, Neutron::Events &buffer)
{
  _processM_T<AbstractNeutronScatterer>( &nc, buffer );
}


// version
// $Id$

// End of file 
