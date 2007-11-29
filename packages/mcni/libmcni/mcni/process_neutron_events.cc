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

#include "mcni/AbstractNeutronScatterer.h"
#include "mcni/process_neutron_events.h"
#include "mcni/exceptions.h"

#include <numeric>


namespace {

  template <class NC>
  size_t _process_T
  (NC *nc, mcni::Neutron::Events &evts, int n=-1)
  {
#ifdef DEEPDEBUG
    journal::debug_t debug("scatter");
#endif
    using namespace mcni;
    
    size_t nn = 0;
    if (n<0) nn = evts.size();
    else nn = std::min(size_t(n), evts.size());
    
    size_t n_processed = 0;
    
    for (size_t index=0; index<nn; ) {
      
      bool unuseful_neutron = false;
      Neutron::Event &ev = evts[index];
      
      try {
	//std::cout << "In file " << __FILE__ << " line " << __LINE__ << ":\n";
	//std::cout << _count << std::endl;
	//std::cout << "incident: " << ev << std::endl;
	nc->scatter( ev ); 
	//std::cout << "scattered: " << ev << std::endl;
	/*
	  std::cout << "In file " << __FILE__ << " "
	  << "neutron # " << _count << std::endl;
	*/
      }
      catch (const neutron_absorbed & err ) {
	unuseful_neutron = true;
#ifdef DEEPDEBUG
	debug << journal::at(__HERE__)
	      << err.what() << journal::endl
	      << "Incident neutron = " << ev << journal::endl;
#endif
      }
      catch (const neutron_fatal_path & err ) {
	unuseful_neutron = true;
	std::cerr << "Warning: In file " << __FILE__ << " line " << __LINE__
		  << err.what() << std::endl;
	std::cerr << "Incident neutron = " << ev << std::endl;
	throw;
      }
      
      if (unuseful_neutron) {
	evts[index] = evts[nn-1];
	nn --;
      } else {
	index ++;
      }
      
      n_processed ++;
    }
    
#ifdef DEEPDEBUG
    std::cout << "In file " << __FILE__ << " ";
    std::cout << "total number of good neutrons = " << nn << std::endl;
    std::cout << "total number of events processed = " << n_processed << std::endl;
#endif
    evts.erase( evts.begin() + nn, evts.end() );
    return n_processed;
  }
  
}

size_t mcni::process
(AbstractNeutronScatterer *nc, Neutron::Events &buffer, int n)
{
  return _process_T<AbstractNeutronScatterer>( nc, buffer, n);
}


size_t mcni::process
(const AbstractNeutronScatterer *nc, Neutron::Events &buffer, int n)
{
  return _process_T<const AbstractNeutronScatterer>( nc, buffer, n);
}



// version
// $Id: AbstractNeutronScatterer.cc 591 2006-09-25 07:17:26Z linjiao $

// Generated automatically by CxxMill on Thu Apr  7 14:44:15 2005

// End of file 
