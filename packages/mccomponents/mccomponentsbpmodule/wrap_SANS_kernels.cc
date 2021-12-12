// -*- C++ -*-
//
//

#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/SANS/SpheresKernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"

namespace wrap_mccomponents {

  void wrap_SANSSpheresKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::SANSSpheresKernel w_t;

    kernel_wrapper<w_t>::wrap
      ( "SANSSpheresKernel",
        init<
        w_t::float_t, // absoprtion_coefficient. 1/m
        w_t::float_t, // R. AA
        w_t::float_t, // phi
        w_t::float_t, // delta_rho, // fm/AA^3
        w_t::float_t  // max_angle // degree
        > ()
        )
      ;
  }

  void wrap_SANS_kernels()
  {
    wrap_SANSSpheresKernel();
  }

}

// End of file
