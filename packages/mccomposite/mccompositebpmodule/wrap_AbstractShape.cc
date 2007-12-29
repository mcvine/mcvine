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


#include <sstream>
#include <boost/python.hpp>
#include "mccomposite/geometry/AbstractShape.h"
#include "mccomposite/geometry/shape2ostream.h"


namespace wrap_mccomposite {

  const char * shape_str( const mccomposite::geometry::AbstractShape & shape )
  {
    std::ostringstream oss;
    oss << shape;
    return oss.str().c_str();
  }

  void wrap_AbstractShape()
  {
    using namespace boost::python;

    class_<mccomposite::geometry::AbstractShape, boost::noncopyable>
      ("AbstractShape", no_init)
      .def("__str__", &shape_str)
      ;

  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
