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
#include "mccomponents/kernels/detector/EventModeMCA.h"


namespace wrap_mccomponents {

  void wrap_EventModeMCA()
  {
    using namespace boost::python;
    using namespace mccomponents::detector;

    typedef EventModeMCA w_t;

    class_<w_t, bases<AbstractMultiChannelAnalyzer>, boost::noncopyable >
      ("EventModeMCA",
       init<const char *, w_t::index_t>()
       )
      ;
  }
}


// version
// $Id$

// End of file 
