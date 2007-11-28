// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#ifndef MCNI_GEOMETRY_MATRIX3_H
#define MCNI_GEOMETRY_MATRIX3_H


#include "Vector3.h"

namespace mcni{ 
  
  template <typename NumberType>
  class Matrix3 : public Vector3< Vector3<NumberType> > {
    
  public:
    
    // types
    typedef Vector3< Vector3<NumberType> > base_t;
    typedef Vector3<NumberType> v3_t;
    typedef Matrix3<NumberType> m3_t;
    
    // meta-methods
    inline Matrix3 ( const v3_t & xx, const v3_t & yy, const v3_t & zz);
    inline Matrix3 ( const v3_t & xx );
    Matrix3 ( );
    Matrix3 ( const m3_t & rhs );
    Matrix3( NumberType m11, NumberType m12, NumberType m13,
	     NumberType m21, NumberType m22, NumberType m23,
	     NumberType m31, NumberType m32, NumberType m33);
    
    // operators
    NumberType & operator () ( size_t x, size_t y );
    const NumberType & operator () ( size_t x, size_t y ) const ;
    v3_t operator *(const v3_t &v) const;

    // methods
    m3_t& transpose();

  };
  
} // mcni:


#include "Matrix3.icc"

#endif // MCNI_GEOMETRY_MATRIX3_H

// version
// $Id: matrix3.h 2 2005-06-08 18:28:09Z linjiao $

// End of file
