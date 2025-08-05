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



  
void mccomponents::math::srandom( unsigned int seed )
{
  std::srand( seed );
}

int mccomponents::math::random(int min, int max)
{
  return int(random(0., double(max-min))) % (max-min) + min;
}
  
size_t mccomponents::math::random(size_t min, size_t max)
{
  return size_t(random(0., double(max-min))) % (max-min) + min;
}
  
double mccomponents::math::random( double min, double max ) 
{
  using namespace std;
  return rand()*1./RAND_MAX*(max-min) + min;
}

double mccomponents::math::random_DD( double min, double max ) 
{
  return random(min, max);
}

double mccomponents::math::random01()
{
  return random(0., 1.);
}


// version
// $Id$

// End of file 
