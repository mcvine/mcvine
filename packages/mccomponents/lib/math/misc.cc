#include "mccomponents/math/misc.h"
#include <cmath>

namespace misc{

  const double sign( const double &a, const double &b ) {
    return ((b) >= 0.0 ? std::abs(a) : -std::abs(a));
  }
  
}//misc
