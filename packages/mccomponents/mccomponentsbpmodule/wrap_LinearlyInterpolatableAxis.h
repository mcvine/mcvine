// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatableAxis.h"


namespace wrap_mccomponents {

  template <typename Float, typename N>
  void wrap_LinearlyInterpolatableAxis_T(const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::phonon::LinearlyInterpolatableAxis<Float, N> w_t;

    class_<w_t>
      (classname, 
       init< 
       Float, Float, N
       > () 
       )
      ;

  }

}

// version
// $Id$

// End of file 
