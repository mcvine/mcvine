#ifndef MCCOMPOSITE_GEOMETRY_INTERSECT_H
#define MCCOMPOSITE_GEOMETRY_INTERSECT_H

#include <vector>
#include "AbstractShape.h"
#include "Position.h"
#include "visitors/ArrowIntersector.h"

namespace mccomposite {

  namespace geometry {

    ArrowIntersector::distances_t intersect
    ( const Arrow & arrow, 
      const AbstractShape & shape );

    ArrowIntersector::distances_t forward_intersect
    ( const Arrow & arrow, 
      const AbstractShape & shape );

    /// find the index of the shape in the list "shapes"
    /// that is first hit by a particle.
    /// the particle's position and moving direction is given.
    template <typename index_t>
    index_t find_1st_hit
    ( const Position start, const Direction & direction, 
      const std::vector<const AbstractShape *> & shapes );
    
  }
}


#include "intersect.icc"

#endif
