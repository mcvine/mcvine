// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/diffraction/SingleCrystalDiffractionKernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"
#include "wrap_vector.h"


namespace wrap_mccomponents {

  void wrap_SingleCrystalDiffractionKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;
    using namespace mccomponents::kernels;
    typedef mccomponents::kernels::SingleCrystalDiffractionKernel w_t;

    class_<Lattice>
      ("Lattice",
       init<const R_t &, const R_t &, const R_t &>()
       )
      .def_readonly("ra", &Lattice::ra);

    class_<HKL>
      ("HKL",
       init<int, int, int, w_t::float_t>()
       )
      .def_readonly("h", &HKL::h);

    wrap_vector2<HKL>( "HKL" );

    kernel_wrapper<w_t>::wrap
      ("SingleCrystalDiffractionKernel",
       init<const Lattice &, const w_t::hkllist_t &, w_t::float_t, w_t::float_t, w_t::float_t>()
       );
  }
}

// End of file 
