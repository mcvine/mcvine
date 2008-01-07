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
#include "mccomponents/kernels/sample/AbstractSQE.h"
#include "mccomponents/kernels/sample/SQEkernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_SQEkernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;
    using namespace mccomponents::sample;

    typedef mccomponents::kernels::SQEkernel w_t;

    class_<w_t, bases<mccomponents::AbstractScatteringKernel>, boost::noncopyable >
      ("SQEkernel",
       init<double, double,
       const AbstractSQE &, 
       double, double, double, double> () 
       [with_custodian_and_ward<1,4> () ]
       )
      ;
    
    class_<AbstractSQE, boost::noncopyable>
      ("AbstractSQE", no_init)
      .def("__call__", &AbstractSQE::operator() )
      ;
  }

}


// version
// $Id$

// End of file 
