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
// $Id$

// End of file 
