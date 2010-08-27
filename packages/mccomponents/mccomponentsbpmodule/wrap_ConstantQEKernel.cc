// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2007 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/ConstantQEKernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_ConstantQEKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::ConstantQEKernel w_t;

    kernel_wrapper<w_t>::wrap
      ("ConstantQEKernel",
       init<double, double, double, double> ()
       )
      ;
  }

}


// version
// $Id$

// End of file 
