#include "mccomposite/geometry/intersect.h"

mccomposite::geometry::ArrowIntersector::distances_t intersect
( const mccomposite::geometry::Arrow & arrow, 
  const mccomposite::geometry::AbstractShape & shape )
{
  mccomposite::geometry::ArrowIntersector intersector;
  intersector.setArrow( arrow );
  return intersector.calculate_intersections( shape );
}
