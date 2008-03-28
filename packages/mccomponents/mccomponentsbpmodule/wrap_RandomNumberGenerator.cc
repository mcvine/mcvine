// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2008 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/math/random.h"


namespace wrap_mccomponents {

  void wrap_RandomNumberGenerator()
  {
    using namespace boost::python;

    typedef mccomponents::random::Generator w_t;

    class_<w_t, boost::noncopyable >
      ("RandomNumberGenerator",
       init<double>()
       )
      .def( init<>() )
      ;
  }
}


// version
// $Id$

// End of file 
