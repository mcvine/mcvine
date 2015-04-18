// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <iostream>
#include "mcni/geometry/Vector3.h"
#include "mcni/test/assert.h"


using namespace mcni;

void basicTests()
{
  Vector3<double> v1(0,0,1), v2, v3(v1);
  std::cout << "v1=" << v1 << std::endl
	    << "v2=" << v2 << std::endl
	    << "v3=" << v3 << std::endl
    ;
  Vector3<double> v4 = v1;
  std::cout << "v4=" << v4 << std::endl;
  double x=v4.x;
  v4.x = 3;

  Vector3<double> a(3,0,0), b(0,2,0), c(0,0,1), d;

  std::cout << "a=" << a << std::endl;

  std::cout << "b=" << b << std::endl;

  std::cout << "c=" << c << std::endl;
  std::cout << "a+b=" << a+b << std::endl;
  d = a + b;
  assertAlmostEqual(  d[0], 3 );
  assertAlmostEqual(  d[1], 2 );
  assertAlmostEqual(  d[2], 0 );
  
  std::cout << "a-b=" << a-b << std::endl;
  d = a - b;
  assertAlmostEqual(  d[0], 3 );
  assertAlmostEqual(  d[1], -2 );
  assertAlmostEqual(  d[2], 0 );

  std::cout << "a*b=" << a*b << std::endl;
  d = a * b;
  assertAlmostEqual(  d[0], 0 );
  assertAlmostEqual(  d[1], 0 );
  assertAlmostEqual(  d[2], 6 );

  std::cout << "a*2=" << a*2 << std::endl;
  d = a * 2;
  assertAlmostEqual(  d[0], 6 );
  assertAlmostEqual(  d[1], 0 );
  assertAlmostEqual(  d[2], 0 );

  Vector3<double> as, bs, cs;
  get_inversions(a,b,c, as,bs,cs);
  std::cout << "inversions of a,b,c = " <<as <<" "<<bs<<" "<< cs<<std::endl;
  assertAlmostEqual(  as[0], 1./3 );
  assertAlmostEqual(  bs[1], 0.5 );
  assertAlmostEqual(  cs[2], 1 );
}


void complexdouble_Tests()
{
  // typedef double float_t;
  typedef std::complex<float_t> complex_t;
  typedef mcni::Vector3< complex_t > cv_t;
  cv_t v = cv_t(complex_t(0,1), 0,0);
  std::cout << (v|v) << std::endl;

  mcni::cVector3 v1 = mcni::cVector3(mcni::Complex(0,1), 0, 0);
  std::cout << (v1|v1) << std::endl;
}


void memoryTest()
{
  size_t nlp1 = 5000;
  size_t nlp2 = 100000000;
  
  for (size_t i=0; i<nlp1; i++) {
    for (size_t j=0; j<nlp2; j++) {
      Vector3<double> v;
    }
  }
}


int main()
{
  basicTests();
  complexdouble_Tests();
  //memoryTest();
}

// version
// $Id$

// End of file 
