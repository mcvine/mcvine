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
#include "mccomponents/kernels/sample/AbstractSQE.h"
#include "mccomponents/kernels/sample/SQE/SQE_fromexpression.h"


namespace wrap_mccomponents {

  using namespace mccomponents::sample;

  void wrap_SQE_fromexpression()
  {
    using namespace boost::python;

    typedef SQE_fromexpression w_t;

    class_<w_t, bases<mccomponents::sample::AbstractSQE>, boost::noncopyable >
      ("SQE_fromexpression",
       init<const char *>()
       )
      ;
  }

}

// version
// $Id$

// End of file 
