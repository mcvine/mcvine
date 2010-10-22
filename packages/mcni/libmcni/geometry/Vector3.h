// -*- C++ -*-
/***************************************************************************
                                vector3.h  
 ---------------------------------------------------------------------------
    begin                : Thu Sep 6 2001
    copyright            : (C) 2001-2007 by Jiao Lin
    email                : linjiao@its.caltech.edu
***************************************************************************/


#ifndef MCNI_GEOMETRY_VECTOR3_H
#define MCNI_GEOMETRY_VECTOR3_H


#include "mcni/math/number.h"


namespace mcni{ 
  
  // 3D Vector
  // inner product: (a|b)
  // outer product: a*b
  // input and output operator: >>, <<
  // string format: (a,b,c)
  template <class T>
  class Vector3
  {
    
  public:
    T &x;
    T &y;
    T &z;
    
    // types
    typedef T value_type;

    //
    inline static size_t size() { return 3; }
    
    // iterators
    typedef const T* const_iterator;
    typedef T* iterator;
    inline const_iterator begin() const {return m_data;}
    inline iterator begin() {return m_data;}
    inline const_iterator end() const {return m_data+3;}
    inline iterator end() {return m_data+3;}
    
    // meta-methods
    Vector3 ( const T & xx, const T & yy, const T & zz) ;
    Vector3 ( const T & xx ) ;
    Vector3 ( );
    Vector3 ( const Vector3<T> & rhs );
    const Vector3 <T> & operator = ( const Vector3<T> & rhs );
    
    // methods
    Vector3 <T> & normalize( void);
    inline T length(void) const;
    // square of length
    inline T length2(void) const;
    
    // operators
    Vector3 <T> operator+(const Vector3 <T> & b) const;
    const Vector3 <T> & operator+=(const Vector3 <T> & b);
    Vector3 <T> operator-(const Vector3 <T> & b) const;
    Vector3 <T> operator-() const;
    const Vector3 <T> & operator-=(const Vector3 <T> & b);
    Vector3 <T> operator*(T n) const;
    Vector3 <T> operator*(const Vector3 <T> & b) const;
    inline const T & operator[]( size_t i ) const;
    inline T & operator[]( size_t i ) ;
    
  private:
    T m_data[3];
  };
  
  
  // operators
  template <class T>
  T operator |(const Vector3 <T> &a, const Vector3 <T> &b);
  
  template <class T>
  Vector3 <T> operator*(T n, const Vector3 <T> & a);
  
  
  // specializations
  typedef Vector3<double> dVector3;
  typedef Vector3<Complex> cVector3;
  typedef Vector3<int> iVector3;
  
  cVector3 operator*( Complex c, const dVector3 & v);
  cVector3 operator*( double d, const cVector3 & v);
  cVector3 operator*( const cVector3 &v1, const dVector3 &v2);
  cVector3 operator*( const dVector3 &v1, const cVector3 &v2);
  cVector3 operator+( const cVector3 &cv, const dVector3 &dv);
  cVector3 operator+( const dVector3 &dv, const cVector3 &cv);
  // specialization for cVector3
  Complex operator|( const cVector3 & v1, const cVector3 & v2);
  //template <> operator| <Complex> ( const cVector3 &v1, const cVector3 &v2)
  //{ return conj(v1.x)*v2.x+conj(v1.y)*v2.y+conj(v1.z)*v2.z; };
  Complex operator|( const dVector3 & v1, const cVector3 & v2);
  Complex operator|( const cVector3 & v1, const dVector3 & v2);
  
  
  // misc
  //! calculate "stars" of 3D vector3 x,y,z
  template <class FLOAT>
  void get_inversions( const Vector3<FLOAT> &x, const Vector3<FLOAT> &y, 
		       const Vector3<FLOAT> &z, Vector3<FLOAT> &x_star, 
		       Vector3<FLOAT> &y_star, Vector3<FLOAT> &z_star );

} // mcni:


// 
template <class T>
std::ostream & operator<<(std::ostream & os, const mcni::Vector3 <T> &v);
  

#include "Vector3.icc"

#endif // MCNI_GEOMETRY_VECTOR3_H


// version
// $Id$

// End of file

