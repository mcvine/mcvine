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
#include <string>

#include "mccomposite/AbstractNeutronScatterer.h"
#include "mccomposite/Geometer.h"

namespace wrap_mccomposite {
  
  using namespace boost::python;
  using namespace mccomposite;
  
  
  template <typename ElementType>
  void wrap_Geometer( const char * elementTypeName )
  {
    std::string name("Geometer_");
    name += elementTypeName;

    typedef mccomposite::Geometer<ElementType> w_t;
    
    class_<w_t>
      (name.c_str(), init<>())
      .def( "register", &w_t::remember )
      .def( "getPosition", &w_t::getPosition, return_internal_reference<1>() )
      .def( "getOrientation", &w_t::getOrientation, return_internal_reference<1>() )
      ;
  }
}


// version
// $Id$

// End of file 
