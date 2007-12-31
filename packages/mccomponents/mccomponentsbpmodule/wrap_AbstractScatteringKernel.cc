// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/AbstractScatteringKernel.h"


namespace wrap_mccomponents {

  void wrap_AbstractScatteringKernel()
  {
    using namespace boost::python;
    using namespace mccomponents;

    class_<AbstractScatteringKernel, boost::noncopyable>
      ("AbstractScatteringKernel", no_init)
      .def("scatter", &AbstractScatteringKernel::scatter)
      .def("absorb", &AbstractScatteringKernel::absorb)
      .def("scattering_coefficient", &AbstractScatteringKernel::scattering_coefficient)
      .def("absorption_coefficient", &AbstractScatteringKernel::absorption_coefficient)
      ;

  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
