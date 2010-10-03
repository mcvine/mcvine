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

#include "mccomposite/geometry/AbstractShape.h"
#include "wrap_vector.h"


namespace wrap_mccomposite {

  void wrap_shapecontainer()
  {
    using namespace boost::python;
    using namespace mccomposite::geometry;

    wrap_pointer_vector<const AbstractShape>( "Shape" );
  }
}


// version
// $Id$

// End of file 
