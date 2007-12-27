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


#ifndef MCCOMPOSITE_GEOMETRY_LOCATE_H
#define MCCOMPOSITE_GEOMETRY_LOCATE_H


#include <iostream>
#include "AbstractShape.h"
#include "Position.h"
#include "visitors/Locator.h"

namespace mccomposite {

  namespace geometry {
    
    Locator::Location locate
    ( const mccomposite::geometry::Position & position, 
      const mccomposite::geometry::AbstractShape & shape );

  }
}

#endif

// version
// $Id$

// End of file 
