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


#ifndef MCCOMPONENTS_RANDOM_GAUSSIAN_H
#define MCCOMPONENTS_RANDOM_GAUSSIAN_H


#include "mcni/geometry/Vector3.h"


namespace mccomponents{

  namespace math{

    // generate random numbers in a normal distribution
    // center at 0 and mean deviation is 1
    double normal_distrib_rand();

  } // math

} // mccomponents


#endif //MCCOMPONENTS_RANDOM_GAUSSIAN_H


// version
// $Id: geometry.h 601 2010-10-03 19:55:29Z linjiao $

// End of file 
