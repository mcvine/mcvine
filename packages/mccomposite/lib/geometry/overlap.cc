#include <cstdlib>
#include <cmath>
#include "mccomposite/geometry/locate.h"
#include "mccomposite/geometry/intersect.h"
#include "mccomposite/geometry/overlap.h"
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
  // randomly calculate intersections of a ray with a
  // shape. The intersections must be on the surface of that shape.
  // if that point is on the surface or the inside of the other shape
  // then we have a overlap
  
  for (size_t i=0; i<N; i++) {
    // std::cout << "iteration " << i << std::endl;
    double x = random(bb.cx-bb.sx/2, bb.cx+bb.sx/2);
    double y = random(bb.cy-bb.sy/2, bb.cy+bb.sy/2);
    double z = random(bb.cz-bb.sz/2, bb.cz+bb.sz/2);
    Position start(x,y,z);

    double cos_theta = random(-1., 1.);
    double sin_theta = std::sqrt(1-cos_theta*cos_theta);
    double phi = random(0, 2*M_PI);
    Direction dir(sin_theta*std::cos(phi), sin_theta*std::sin(phi), cos_theta);

    Arrow arrow(start, dir);
    // std::cout << start << ", " << dir << std::endl;

    ArrowIntersector::distances_t ds = intersect(arrow, shape1);
    // std::cout << "ds size" << ds.size() << std::endl;
    for (int i_p=0; i_p<ds.size(); i_p++) {
      // std::cout << "intersection #" << i_p << std::endl;
      Position p = start + ds[i_p]*dir;
      Locator::Location l2 = locate(p, shape2);
      // std::cout << p << ", " << l2 << std::endl;
      if (l2!=Locator::outside) {
	return true;
      }
    }
  }
  return false;
}
