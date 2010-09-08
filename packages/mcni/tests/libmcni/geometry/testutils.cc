// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2010 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <iostream>
#include "mcni/geometry/utils.h"
#include "mcni/test/assert.h"


using namespace mcni;

void test1()
{
  typedef Vector3<double> V3;
  V3 x(1,0,0), y(0,1,0), z(0,0,1);
  
  assertVectorAlmostEqual(rotated(x,z,PI/2), y, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(y,z,PI/2), -x, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(z,z,PI/2), z, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(x+y,z,PI/2), y-x, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(x+y*2,z,PI/2), y-x*2, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(x+z,z,PI/2), y+z, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(y*1.123+z,z,PI/2), -x*1.123+z, 1e-5, 1e-5);
  assertVectorAlmostEqual
    (rotated(x*0.25+y*1.123+z*0.2223,z,PI/2),
     y*0.25-x*1.123+z*0.2223, 
     1e-5, 1e-5);

  assertVectorAlmostEqual(rotated(x,x,PI/2), x, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(y,x,PI/2), z, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(z,x,PI/2), -y, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(y+z,x,PI/2), z-y, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(y+z*2,x,PI/2), z-y*2, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(x+z,x,PI/2), x-y, 1e-5, 1e-5);
  assertVectorAlmostEqual(rotated(y*1.123+x,x,PI/2), z*1.123+x, 1e-5, 1e-5);
  assertVectorAlmostEqual
    (rotated(x*0.25+y*1.123+z*0.2223,x,PI/2),
     x*0.25+z*1.123-y*0.2223, 
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(x, x+y+z, 2*PI/3.),
     y,
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(x, x+y+z, 4*PI/3.),
     z,
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(y, x+y+z, 2*PI/3.),
     z,
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(y, x+y+z, 4*PI/3.),
     x,
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(z, x+y+z, 2*PI/3.),
     x,
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(z, x+y+z, 4*PI/3.),
     y,
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(x, x+y, PI),
     y,
     1e-5, 1e-5);

  assertVectorAlmostEqual
    (rotated(y, x+y, PI),
     x,
     1e-5, 1e-5);

}


int main()
{
  test1();
}

// version
// $Id$

// End of file 
