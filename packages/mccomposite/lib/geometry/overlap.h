// -*- C++ -*-
//
//


#ifndef MCCOMPOSITE_GEOMETRY_OVERLAP_H
#define MCCOMPOSITE_GEOMETRY_OVERLAP_H


#include <iostream>
#include "AbstractShape.h"
#include "BoundingBox.h"

namespace mccomposite {

  namespace geometry {

    bool hasOverlap
    (const mccomposite::geometry::AbstractShape & shape1,
     const mccomposite::geometry::AbstractShape & shape2,
     const BoundingBox &bb,
     size_t N
     );

  }
}

#endif

// version
// $Id$

// End of file 
