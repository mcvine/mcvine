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



#include "mcni/boostpython_binding/wrap_component.h"
#include "mcni/DummyComponent.h"



void wrap_dummycomponent() 
{
  using namespace mcni::boostpython_binding;

  boostpython_binding::component_wrapper<mcni::DummyComponent>::wrap
    ("DummyComponent", init< const char * >() );
}


// version
// $Id: wrap_neutron_buffer.cc 598 2007-01-21 19:48:06Z linjiao $

// End of file 
