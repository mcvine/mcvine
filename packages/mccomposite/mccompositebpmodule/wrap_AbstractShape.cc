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
#include "mccomposite/geometry/AbstractShape.h"


namespace wrap_mccomposite {

  void wrap_AbstractShape()
  {
    using namespace boost::python;

    class_<mccomposite::geometry::AbstractShape, boost::noncopyable>
      ("AbstractShape", no_init)
      ;

  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
