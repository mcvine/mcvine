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

  class xxxCLASSxxx: public AbstractScatteringKernel {
  public:

    // meta-methods
    xxxCLASSxxx( ... ) { ... }
    virtual ~xxxCLASSxxx() {...}

    // methods
    double absorption_coefficient( const mcni::Neutron::Event & ev )
    {
    ...
    }
    double scattering_coefficient( const mcni::Neutron::Event & ev )
    {
    ...
    }
    void scatter( mcni::Neutron::Event & ev )
    {
    ...
    }
    void absorb( mcni::Neutron::Event & ev )
    {
    ...
    }
  };

} // mccomponents



#include "mccomponents/boostpython_binding/wrap_kernel.h"

void wrap() 
{
  using namespace mccomponents::boostpython_binding;

  kernel_wrapper<mccomponents::xxxCLASSxxx>::wrap
    ("xxxCLASSxxx", init<...>() );
}



// version
// $Id$

// End of file 
