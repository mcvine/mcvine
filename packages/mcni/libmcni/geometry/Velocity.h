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

#ifndef MCNI_GEOMETRY_VELOCITY_H
#define MCNI_GEOMETRY_VELOCITY_H

namespace mcni {
  
  template <typename NumberType>
  class Velocity: public Vector3<NumberType> {
  public:

    // types
    typedef Vector3<NumberType> base_t;

    // meta-methods
    inline Velocity( const NumberType &x, const NumberType &y,  const NumberType &z);
    inline Velocity( const base_t & v );
  };

}


template <typename NumberType>
mcni::Velocity<NumberType> operator *
(const mcni::RotationMatrix<NumberType> & m, const mcni::Velocity<NumberType> &r );


#include "Velocity.icc"

#endif

// version
// $Id$

// Generated automatically by CxxMill on Wed Nov 28 10:43:14 2007

// End of file 
