// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include <cstdlib>
#include "mccomponents/math/random.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


  
void mccomponents::math::srandom( unsigned int seed )
{
  std::srand( seed );
}
  
double mccomponents::math::random( double min, double max ) 
{
  using namespace std;
  return rand()*1./RAND_MAX*(max-min) + min;
}

double mccomponents::math::random01()
{
  return random(0., 1.);
}


// version
// $Id$

// End of file 
