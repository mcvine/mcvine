// -*- C++ -*-
//


#include <boost/python.hpp>
#include "mccomponents/kernels/sample/DGSSXResKernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_DGSSXResKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::DGSSXResKernel w_t;

    kernel_wrapper<w_t>::wrap
      ("DGSSXResKernel",
       init<const w_t::X_t&, double, double, double, double, double> () 
       )
      ;
  }

}


// End of file 
