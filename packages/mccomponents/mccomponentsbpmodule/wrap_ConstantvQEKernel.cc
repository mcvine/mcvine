// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2007-2014 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/ConstantvQEKernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_ConstantvQEKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::ConstantvQEKernel w_t;

    kernel_wrapper<w_t>::wrap
      ("ConstantvQEKernel",
       init<double, double, double, 
       double, double,
       double, double> ()
       )
      ;
  }

}


// version
// $Id$

// End of file 
