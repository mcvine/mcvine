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

#ifndef MCNI_GEOMETRY_ROTATIONMATRIX_H
#define MCNI_GEOMETRY_ROTATIONMATRIX_H

namespace mcni {
  
  template <typename NumberType>
  class RotationMatrix: public Matrix3<NumberType> {
  public:

    // types
    typedef Matrix3<NumberType> base_t;
    typedef NumberType element_t;

    // meta-methods
    inline RotationMatrix( );
    inline RotationMatrix
    ( element_t m11, element_t m12, element_t m13,
      element_t m21, element_t m22, element_t m23,
      element_t m31, element_t m32, element_t m33
      );

  };

}


#include "RotationMatrix.icc"

#endif

// version
// $Id$

// Generated automatically by CxxMill on Wed Nov 28 10:43:14 2007

// End of file 
