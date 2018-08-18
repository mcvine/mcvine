// -*- C++ -*-
//
//


#ifndef MCCOMPOSITE_GEOMETRY_OVERLAP_H
#define MCCOMPOSITE_GEOMETRY_OVERLAP_H


#include <iostream>
#include "AbstractShape.h"

namespace mccomposite {

  namespace geometry {

    struct BoundingBox {
      double cx, cy, cz; // center
      double sx, sy, sz; // size
    };
    
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
