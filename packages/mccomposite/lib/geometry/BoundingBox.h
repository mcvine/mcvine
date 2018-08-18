// -*- C++ -*-
//
//


#ifndef MCCOMPOSITE_GEOMETRY_BOUNDINGBOX_H
#define MCCOMPOSITE_GEOMETRY_BOUNDINGBOX_H

namespace mccomposite {
  namespace geometry {

    struct BoundingBox {
      double cx, cy, cz; // center
      double sx, sy, sz; // size
    };
    
  }
}

#endif

// End of file 
