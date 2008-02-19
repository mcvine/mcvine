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
#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"


namespace wrap_mccomponents {

  void wrap_AbstractDispersion_3D()
  {
    using namespace boost::python;
    typedef DANSE::phonon::AbstractDispersion_3D w_t;

    class_<w_t, boost::noncopyable>
      ("AbstractDispersion_3D", no_init)
      .def("nBranches", &w_t::nBranches )
      .def("nAtoms", &w_t::nAtoms )
      .def("energy", &w_t::energy )
      .def("polarization", &w_t::polarization )
      ;
  }

}


// version
// $Id$

// End of file 
