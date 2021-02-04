// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/AbstractSQE.h"
#include "mccomponents/kernels/sample/SQE_EnergyFocusing_Kernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_SQE_EnergyFocusing_Kernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;
    using namespace mccomponents::sample;

    typedef mccomponents::kernels::SQE_EnergyFocusing_Kernel w_t;

    kernel_wrapper<w_t>::wrap
      ("SQE_EnergyFocusing_Kernel",
       init<double, double, double,
       AbstractSQE &,  
       double, double, double, double, double, double> () 
       [with_custodian_and_ward<1,5> () ]
       )
      ;
  }
}


// End of file 
