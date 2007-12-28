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

    wrap_pointer_vector<AbstractShape>( "Shape" );
  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
