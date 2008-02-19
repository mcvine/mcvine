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
#include "histogram/NdArray.h"


namespace wrap_mccomponents {

  template <typename Iterator, typename DataType,
	    typename Size, typename SuperSize,
	    unsigned int NDimension>
  void wrap_NdArray_T(const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::Histogram::NdArray<Iterator, DataType, Size, SuperSize, NDimension> w_t;

    class_<w_t>
      (classname, 
       init<
       Iterator, const Size *
       > () 
       )
      ;

  }

}

// version
// $Id$

// End of file 
