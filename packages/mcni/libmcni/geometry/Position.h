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

#ifndef MCNI_GEOMETRY_POSITION_H
#define MCNI_GEOMETRY_POSITION_H

namespace mcni {
  
  template <typename NumberType>
  class Position: public Vector3<NumberType> {
  public:

    // types
    typedef Vector3<NumberType> base_t;

    // meta-methods
    inline Position( const NumberType &x, const NumberType &y,  const NumberType &z);
    inline Position( const base_t & v );
  };

}


#include "Position.icc"

#endif

// version
// $Id$

// Generated automatically by CxxMill on Wed Nov 28 10:43:14 2007

// End of file 
