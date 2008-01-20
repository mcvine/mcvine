// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include "mcstas2/mcni_integration/Component.h"
#include "mcni/boostpython_binding/wrap_component.h"

namespace wrap_mcstas2 {

  void wrap_mcni_integration_Component() 
  {
    using namespace mcni::boostpython_binding;
    
    boostpython_binding::component_wrapper<mcstas2::mcni_integration::Component>::wrap
      ("McStasComponentAsMcniComponent", 
       init<mcstas2::Component &>()
       [with_custodian_and_ward<1,2> () ]
       );
  }

}

// version
// $Id$

// End of file 
