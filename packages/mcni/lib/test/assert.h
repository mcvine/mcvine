// -*- C++ -*-

#ifndef MCNI_TEST_ASSERT_H
#define MCNI_TEST_ASSERT_H


#include <cmath>
#include "exception.h"


// assertion functions. useful for tests

namespace mcni{


  /// assertion exception class
  class AssertionError : public Exception {
    
  public:
    AssertionError( const char * msg = "assertion error" ) 
      : Exception( msg ) {}
  };

  

  /// assert two numbers are equal. only good for integers
  template <class Num1, class Num2>
  void assertNumberEqual( Num1 a, Num2 b );
  

  /// assert two numbers are almost equal. good for floats
  /*!
    @param a,b: two input numbers
    @param relerr: if the relative difference between the two input numbers is 
    larger than "relerr', then we say the two numbers are not almost equal
    @param abserr: if the absolute difference between the two input numbers is
    smaller than 'abserr', then we say the two numbers are not almost equal
   */
  template <class Num1, class Num2>
  void assertNumberAlmostEqual
  ( Num1 a, Num2 b, double relerr=0.01, double abserr = 1e-10 );


  /// assert two vectors are almost equal
  /*!
    @param v1, v2: two input vectors
    @param relerr, abserr: refer to function assertNumberAlmostEqual
   */
  template <class Vector1, class Vector2>
  void assertVectorAlmostEqual
  ( const Vector1 & v1, const Vector2 & v2, 
    double relerr=0.01, double abserr=1e-30);
  

  /// assert two vectors are almost equal
  /*!
    the "double" version of assertNumberAlmostEqual. It is expected to be
    used most frequently, so we give it a special name
   */
  inline void assertAlmostEqual
  ( double a, double b, double relerr=0.01, double abserr = 1e-10) {
    assertNumberAlmostEqual( a, b, relerr, abserr );
  }

} // mcni



#include "assert.icc"

#endif // MCNI_TEST_ASSERT_H
