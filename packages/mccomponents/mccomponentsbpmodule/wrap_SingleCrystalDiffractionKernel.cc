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
      .def_readonly("ra", &Lattice::ra)
      .def_readonly("rb", &Lattice::rb)
      .def_readonly("rc", &Lattice::rc)
      ;

    class_<HKL>
      ("HKL",
       init<w_t::float_t, w_t::float_t, w_t::float_t, w_t::float_t>()
       )
      .def_readonly("h", &HKL::h)
      .def_readonly("k", &HKL::k)
      .def_readonly("l", &HKL::l)
      .def_readonly("F2", &HKL::F2)
      ;

    wrap_vector2<HKL>( "HKL" );

    kernel_wrapper<w_t>::wrap
      ("SingleCrystalDiffractionKernel",
       init<const Lattice &, const w_t::hkllist_t &, w_t::float_t, w_t::float_t, w_t::float_t>()
       [with_custodian_and_ward<1,2,
        with_custodian_and_ward<1,3> >()]
       )
      .def("check_reflections", &w_t::check_reflections)
      ;
  }
}

// End of file 
