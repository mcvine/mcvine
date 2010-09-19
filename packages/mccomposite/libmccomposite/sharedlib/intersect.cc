#include <algorithm>
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
    
    ArrowIntersector::distances_t forward_intersect
    ( const Arrow & arrow, 
      const AbstractShape & shape )
    {
      ArrowIntersector::distances_t all, ret;
      all = intersect( arrow, shape );
      
      using namespace std;
      remove_copy_if
	(all.begin(), all.end(), back_inserter( ret ),
	 bind2nd( less<double>(), 0 ) );
      
      return ret;
      
    }

  }
}
