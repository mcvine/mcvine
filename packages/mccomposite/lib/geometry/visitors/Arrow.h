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


#ifndef MCCOMPOSITE_GEOMETRY_ARROW_H
#define MCCOMPOSITE_GEOMETRY_ARROW_H


#include "mccomposite/geometry/Position.h"
#include "mccomposite/geometry/Direction.h"


namespace mccomposite {
  
  namespace geometry {
    
    struct Arrow{
      
      // types
      typedef Position position_t;
      typedef Direction direction_t;
      
      // meta methods
      Arrow( const position_t & start, const direction_t & direction );
      Arrow();
      
      // methods
      /// Just for ostream << operator
      void print( std::ostream & os ) const;
      
      // data
      position_t start;
      direction_t direction;
    };
    
  }
}

// ostream
std::ostream & operator << 
(std::ostream & os, const mccomposite::geometry::Arrow & arrow);


#endif

// version
// $Id$

// End of file 
