#include <cstdlib>
#include "mccomposite/geometry/locate.h"
#include "mccomposite/geometry/overlap.h"
#include "journal/debug.h"
#include "mccomposite/geometry/shape2ostream.h"


namespace {
  double random( double min, double max ) 
  {
    using namespace std;
    return rand()*1./RAND_MAX*(max-min) + min;
  }
}

bool mccomposite::geometry::hasOverlap
(const mccomposite::geometry::AbstractShape & shape1,
 const mccomposite::geometry::AbstractShape & shape2,
 const mccomposite::geometry::BoundingBox &bb,
 size_t N
 )
{
  // randomly generate points in bounding box, and make sure they are not
  // inside or on surface both shapes
  for (size_t i=0; i<N; i++) {
    double x = random(bb.cx-bb.sx/2, bb.cx+bb.sx/2);
    double y = random(bb.cy-bb.sy/2, bb.cy+bb.sy/2);
    double z = random(bb.cz-bb.sz/2, bb.cz+bb.sz/2);
    Position p(x,y,z);
    Locator::Location l1 = locate(p, shape1);
    Locator::Location l2 = locate(p, shape2);
    if (l1!=Locator::outside &&l2!=Locator::outside) {
      return true;
    }
  }
  return false;
}
