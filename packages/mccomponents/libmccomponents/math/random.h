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

namespace mccomponents {

  namespace math {

    double random( double min, double max );
    double random01();
    void srandom( unsigned int );

  }
}

#endif 

// version
// $Id$

// End of file 
