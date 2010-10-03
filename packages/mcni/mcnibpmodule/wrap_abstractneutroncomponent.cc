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
#include "mcni/AbstractNeutronComponent.h"
#include "mcni/process_neutron_events.h"


namespace {
  
}

void wrap_abstractneutroncomponent()
{
  using namespace boost::python;
  using namespace mcni;
  
  class_<AbstractNeutronComponent, bases<AbstractNeutronScatterer>, boost::noncopyable >
    ("AbstractNeutronComponent", no_init )
    .def_readonly( "name", &AbstractNeutronComponent::name )
    ;
}


// version
// $Id$

// End of file 
