#include <iostream>
#include "AbstractShape.h"
#include "Position.h"
#include "visitors/ArrowIntersector.h"

mccomposite::geometry::ArrowIntersector::distances_t intersect
( const mccomposite::geometry::Arrow & arrow, 
  const mccomposite::geometry::AbstractShape & shape );
