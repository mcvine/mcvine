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

namespace mccomposite {

  template <typename Position, typename Direction>
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


// ostream
template <typename Position, typename Direction>
std::ostream & operator << 
(std::ostream & os, const mccomposite::Arrow<Position, Direction> & arrow);


#include "Arrow.icc"

#endif

// version
// $Id$

// End of file 
