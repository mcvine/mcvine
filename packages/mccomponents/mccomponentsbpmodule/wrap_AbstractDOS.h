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


#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/AbstractDOS.h"


namespace wrap_mccomponents {

  template <typename Float>
  void wrap_AbstractDOS_T( const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::phonon::AbstractDOS<Float> w_t;

    class_<w_t, boost::noncopyable>
      (classname, no_init)
      .def( "emin", &w_t::emin )
      .def( "emax", &w_t::emax )
      .def( "__call__", &w_t::operator ())
      ;
  }

}


// version
// $Id$

// End of file 
