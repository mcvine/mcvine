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



#include <boost/python.hpp>
#include "mcni/AbstractNeutronScatterer.h"
#include "mcni/process_neutron_events.h"


namespace {
  
  void NeutronScatterer_scatter
  (mcni::AbstractNeutronScatterer & scatterer, mcni::Neutron::Event & ev )
  {
    scatterer.scatter( ev );
    return;
  }
  
  
  void NeutronScatterer_absorb
  (mcni::AbstractNeutronScatterer & scatterer, mcni::Neutron::Event & ev )
  {
    scatterer.absorb( ev );
    return;
  }
  
}

void wrap_abstractneutronscatterer() 
{
  using namespace boost::python;
  using namespace mcni;
  
  class_<AbstractNeutronScatterer, boost::noncopyable >
    ("AbstractNeutronScatterer",
     no_init )
    .def("absorb", NeutronScatterer_absorb)
    .def("scatter", NeutronScatterer_scatter)
    ;
}


// version
// $Id: wrap_neutron_buffer.cc 598 2007-01-21 19:48:06Z linjiao $

// End of file 
