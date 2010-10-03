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
#include "mcni/geometry/Matrix3.h"
#include "mcni/test/assert.h"


int main()
{
  using namespace mcni;
  typedef Matrix3<double> m3_t;
  typedef m3_t::v3_t v3_t;
  m3_t m1(0,0,1,
	  1,0,0,
	  0,1,0), 
    m2(m1), m3(m1);
  
  assertVectorAlmostEqual( m1[0], v3_t(0,0,1) );
  assertVectorAlmostEqual( m1[1], v3_t(1,0,0) );
  assertVectorAlmostEqual( m1[2], v3_t(0,1,0) );

  assertVectorAlmostEqual( m2[0], v3_t(0,0,1) );
  assertVectorAlmostEqual( m2[1], v3_t(1,0,0) );
  assertVectorAlmostEqual( m2[2], v3_t(0,1,0) );

  m3.transpose();
  assertVectorAlmostEqual( m3[0], v3_t(0,1,0) );
  assertVectorAlmostEqual( m3[1], v3_t(0,0,1) );
  assertVectorAlmostEqual( m3[2], v3_t(1,0,0) );

  m3_t m4 = m1;
  m4(0,0) = 1;
  assertVectorAlmostEqual( m4[0], v3_t(1,0,1) );

  try {
    m4(3,1) = 5;
  }
  catch (...) {
    std::cout << "good, caught error!" << std::endl;
  }
}

// version
// $Id$

// Generated automatically by CxxMill on Mon May 16 21:46:11 2005

// End of file 
