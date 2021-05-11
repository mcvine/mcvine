// -*- C++ -*-
//
//

#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/AbstractSvQ.h"
#include "mccomponents/kernels/sample/SvQkernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"

namespace wrap_mccomponents {

  void wrap_SvQkernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;
    using namespace mccomponents::sample;

    typedef mccomponents::kernels::SvQkernel w_t;

    kernel_wrapper<w_t>::wrap
      ("SvQkernel",
       init<double, double, AbstractSvQ & > ()
       [with_custodian_and_ward<1, 4> () ]
       )
      ;

    class_<AbstractSvQ, boost::noncopyable>
      ("AbstractSvQ", no_init)
      .def("__call__", &AbstractSvQ::operator() )
      ;
  }

}

// End of file
