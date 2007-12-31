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

#include "mccomponents/mccomponents.h"


namespace mccomponents{

  class NeutronPrinter: public AbstractScatteringKernel {
  public:

    // meta-methods
    NeutronPrinter( ) {}

    // methods
    double absorption_coefficient( const mcni::Neutron::Event & ev )
    {
      return 1;
    }
    double scattering_coefficient( const mcni::Neutron::Event & ev )
    {
      return 1;
    }
    void scatter( mcni::Neutron::Event & ev )
    {
      std::cout << ev << std::endl;
    }
    void absorb( mcni::Neutron::Event & ev )
    {
      std::cout << ev << std::endl;
    }
  };

} // mccomponents



#include "mccomponents/boostpython_binding/wrap_kernel.h"

void wrap() 
{
  using namespace mccomponents::boostpython_binding;

  kernel_wrapper<mccomponents::NeutronPrinter>::wrap
    ("NeutronPrinter", 
     init<>() 
     );
}



// version
// $Id$

// End of file 
