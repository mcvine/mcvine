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


#include <iostream>
#include "mccomposite/geometry/visitors/Arrow.h"


// Arrow
mccomposite::geometry::Arrow::Arrow
(const position_t & i_start, const direction_t & i_direction )
  : start(i_start), 
    direction(i_direction)
{
}

mccomposite::geometry::Arrow::Arrow
()
  : start(0,0,0),
    direction(0,0,1)
{
}


void
mccomposite::geometry::Arrow::print
(std::ostream & os) const
{
  os << "arrow: " << start << "-->" << direction;
}


std::ostream & operator << 
(std::ostream & os, const mccomposite::geometry::Arrow & arrow)
{
  arrow.print( os );
  return os;
}


// version
// $Id$

// End of file 
