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
#include "mccomponents/kernels/sample/AbstractSQ.h"
#include "mccomponents/kernels/sample/SQAdaptor.h"
#include "mccomponents/kernels/sample/SQkernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_SQkernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;
    using namespace mccomponents::sample;

    typedef mccomponents::kernels::SQkernel w_t;

    kernel_wrapper<w_t>::wrap
      ("SQkernel",
       init<double, double,
       const AbstractSQ &,  
       double, double> () 
       [with_custodian_and_ward<1,4> () ]
       )
      ;
    
    class_<AbstractSQ, boost::noncopyable>
      ("AbstractSQ", no_init)
      .def("__call__", &AbstractSQ::operator() )
      ;
  }

}


// version
// $Id$

// End of file 
