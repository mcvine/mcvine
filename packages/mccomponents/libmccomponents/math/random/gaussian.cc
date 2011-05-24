// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2011 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include "mccomponents/math/random.h"
#include "mccomponents/math/random/gaussian.h"


#ifdef DEEPDEBUG
#define DEBUG
#endif

#ifdef DEBUG
#include "journal/debug.h"
#endif


double 
mccomponents::math::normal_distrib_rand
()
{
  typedef double float_t;
  float_t x1, x2, w;
  do {
    x1 = 2.0 * random01() - 1.0;
    x2 = 2.0 * random01() - 1.0;
    w = x1*x1 + x2*x2;
  } while (w>=1.);
  
  w = std::sqrt((-2.*std::log(w))/w);
  return x1*w;
}


// version
// $Id: geometry.cc 652 2010-10-22 12:31:15Z linjiao $

// End of file 
