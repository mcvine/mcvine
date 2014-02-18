// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2010 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionData.h"
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionKernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"
#include "wrap_vector.h"


namespace wrap_mccomponents {

  void wrap_SimplePowderDiffractionKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::SimplePowderDiffractionKernel w_t;
    typedef mccomponents::kernels::SimplePowderDiffractionData Data;

    kernel_wrapper<w_t>::wrap
      ("SimplePowderDiffractionKernel",
       init<const Data &> ()
       )
      ;

    class_<Data>
      ("SimplePowderDiffractionData",
       init<>()
       )
      .def_readwrite("Dd_over_d", &Data::Dd_over_d)
      .def_readwrite("DebyeWaller_factor", &Data::DebyeWaller_factor)
      .def_readwrite("unitcell_volume", &Data::unitcell_volume)
      .def_readwrite("density", &Data::density)
      .def_readwrite("atomic_weight", &Data::atomic_weight)
      .def_readwrite("number_of_atoms", &Data::number_of_atoms)
      .def_readwrite("absorption_cross_section", &Data::absorption_cross_section)
      .def_readwrite("coherent_cross_section", &Data::coherent_cross_section)
      .def_readwrite("incoherent_cross_section", &Data::incoherent_cross_section)
      .def_readwrite("peaks", &Data::peaks)
      ;

    class_<Data::Peak>
      ("SimplePowderDiffractionData_Peak",
       init<> ()
       )
      .def_readwrite("q", &Data::Peak::q)
      .def_readwrite("F_squared", &Data::Peak::F_squared)
      .def_readwrite("multiplicity", &Data::Peak::multiplicity)
      .def_readwrite("intrinsic_line_width", &Data::Peak::intrinsic_line_width)
      .def_readwrite("DebyeWaller_factor", &Data::Peak::DebyeWaller_factor)
      ;

    wrap_vector<Data::Peak>("SimplePowderDiffractionData_Peak");
    
  }

}


// version
// $Id$

// End of file 
