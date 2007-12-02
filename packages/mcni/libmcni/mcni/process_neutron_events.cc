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


#include <portinfo>
#include "journal/error.h"
#include "journal/debug.h"

#include "mcni/neutron.h"

#include "mcni/AbstractNeutronComponent.h"
#include "mcni/process_neutron_events.h"
#include "mcni/exceptions.h"

#include <numeric>


namespace {

  template <class NC>
  void _process_T
  (NC *nc, mcni::Neutron::Events &evts)
  {
#ifdef DEEPDEBUG
    journal::debug_t debug("scatter");
#endif
    using namespace mcni;

    static Neutron::Event swap_temp;
    
    size_t nn = evts.size();
    
    for (size_t index=0; index<nn; ) {
      
      Neutron::Event &ev = evts[index];
      
      //if (ev.probability < 0) continue;

      nc->scatter( ev ); 
      /*
      try {
	nc->scatter( ev ); 
      }
      catch (const neutron_fatal_path & err ) {
	// 
	throw;
      }
      */
      
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
  
}

void mcni::process
(AbstractNeutronComponent &nc, Neutron::Events &buffer)
{
  _process_T<AbstractNeutronComponent>( &nc, buffer );
}


// version
// $Id$

// End of file 
