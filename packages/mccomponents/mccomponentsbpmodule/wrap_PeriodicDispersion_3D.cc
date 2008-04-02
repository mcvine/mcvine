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
#include "mccomponents/kernels/sample/phonon/PeriodicDispersion_3D.h"


namespace wrap_mccomponents {

  void wrap_PeriodicDispersion_3D()
  {
    using namespace boost::python;
    typedef DANSE::phonon::AbstractDispersion_3D base_t;
    typedef DANSE::phonon::PeriodicDispersion_3D w_t;

    class_<w_t, bases<base_t>, boost::noncopyable>
      ("PeriodicDispersion_3D", init<const base_t &, const w_t::ReciprocalCell &>() )
      ;

    class_<w_t::ReciprocalCell>
      ("ReciprocalCell", init<>())
      .def_readwrite( "b1", &w_t::ReciprocalCell::b1)
      .def_readwrite( "b2", &w_t::ReciprocalCell::b2)
      .def_readwrite( "b3", &w_t::ReciprocalCell::b3)
      ;
  }

}


// version
// $Id$

// End of file 
