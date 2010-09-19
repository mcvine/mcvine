/***************************************************************************
                          vector3.cpp  -  description
 ---------------------------------------------------------------------------
    begin                : Thu Sep 6 2001
    copyright            : (C) 2001-2007 by Jiao Lin
    email                : linjiao@its.caltech.edu
***************************************************************************/


#include "mcni/geometry/Vector3.h"

// specializations

namespace mcni {

  cVector3 operator*( Complex c, const dVector3 & v)
  {
    return cVector3( c*v.x, c*v.y, c*v.z);
  }
  
  cVector3 operator*( double d, const cVector3 & v)
  {
    return cVector3( d*v.x, d*v.y, d*v.z);
  }
  
  cVector3 operator*( const cVector3 &v1, const dVector3 &v2)
  {
    cVector3 tmp =  Complex(1.0)*v2;
    return v1*tmp;
  }
  
  cVector3 operator*( const dVector3 &v1, const cVector3 &v2)
  {
    cVector3 tmp = Complex(1.0)*v1;
    return tmp*v2;
  }
  
  cVector3 operator+( const cVector3 &cv, const dVector3 &dv)
  {
    return cVector3( cv.x+dv.x, cv.y+dv.y, cv.z+dv.z);
  }
  
  cVector3 operator+( const dVector3 &dv, const cVector3 &cv)
  {
    return (cv+dv);
  }
  
  Complex operator|( const cVector3 & v1, const cVector3 & v2)
  {
    return conj(v1.x)*v2.x+conj(v1.y)*v2.y+conj(v1.z)*v2.z;
  }
  
  Complex operator|( const dVector3 & v1, const cVector3 & v2)
  {
    cVector3 _v1 = Complex(1.0)*v1;
    return (_v1|v2);
  }
  Complex operator|( const cVector3 & v1, const dVector3 & v2)
  {
    return (v2|v1);
  }
  
  
}
