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

#include "mcni/AbstractNeutronComponent.h"


namespace mcni{

  class NeutronPrinter: public AbstractNeutronComponent {
  public:

    // meta-methods
    NeutronPrinter( const char *name) : AbstractNeutronComponent(name) {}
    virtual ~NeutronPrinter() {}

    // methods
    virtual void scatter(Neutron::Event & ev) 
    {
      std::cout << ev << std::endl;
    }
  };

} // mcni



#include "mcni/boostpython_binding/wrap_component.h"

void wrap() 
{
  using namespace mcni::boostpython_binding;

  boostpython_binding::component_wrapper<mcni::NeutronPrinter>::wrap
    ("NeutronPrinter", init<const char *>() );
}



// version
// $Id$

// End of file 
