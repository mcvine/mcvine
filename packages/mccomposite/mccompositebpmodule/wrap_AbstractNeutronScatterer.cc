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


#include <boost/python.hpp>
#include "mccomposite/AbstractNeutronScatterer.h"


namespace wrap_mccomposite {

  void wrap_AbstractNeutronScatterer()
  {
    using namespace boost::python;

    class_<mccomposite::AbstractNeutronScatterer, bases<mcni::AbstractNeutronScatterer>,
      boost::noncopyable>
      ("AbstractNeutronScatterer", no_init)
      .def("shape", &mccomposite::AbstractNeutronScatterer::shape, return_internal_reference<>())
      ;

  }
}


// version
// $Id$

// End of file 
