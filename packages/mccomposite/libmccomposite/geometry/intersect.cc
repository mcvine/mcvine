#include "mccomposite/geometry/intersect.h"

namespace mccomposite {

  namespace geometry {

    ArrowIntersector::distances_t intersect
    ( const Arrow & arrow, 
      const AbstractShape & shape )
    {
      ArrowIntersector intersector;
      intersector.setArrow( arrow );
      return intersector.calculate_intersections( shape );
    }
    
  }
}
