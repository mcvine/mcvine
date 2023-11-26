// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//

#include <cmath>
#include "mccomponents/math/random.h"
#include "mccomponents/math/random/lorentzian.h"


#ifdef DEEPDEBUG
#define DEBUG
#endif

#ifdef DEBUG
#include "journal/debug.h"
#endif


double
mccomponents::math::lorentzian_distrib_rand
()
{
  typedef double float_t;
  float_t x = random01();
  float_t t = M_PI*(x - 0.5);
  return std::tan(t);
}


// End of file
