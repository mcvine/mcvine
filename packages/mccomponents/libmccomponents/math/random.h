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

#ifndef MCCOMPONENTS_RANDOM_H
#define MCCOMPONENTS_RANDOM_H


#include <memory>
#include <cstddef> // size_t

namespace mccomponents {

  namespace math {

    double random( double min, double max );
    int random(int min, int max);
    size_t random(size_t min, size_t max);
    double random01();
    void srandom( unsigned int );
    double random_DD( double min, double max );

  }
}

#endif 

// version
// $Id$

// End of file 
