// -*- C++ -*-
//
//


#include <cassert>
#include <iostream>
#include "mccomposite/geometry/shapes.h"
#include "mccomposite/geometry/overlap.h"


using namespace mccomposite::geometry;
size_t N = 100;

void test1()
{
  //identical box
  Box box1(1,2,3);
  Box box2(1,2,3);
  BoundingBox bb={0.,0.,0.,1.,2.,3.};
  assert(hasOverlap(box1, box2, bb, 1));

  // shifted along z
  Translation tbox1(box2, Vector(0,0,2.999));
  BoundingBox bb1={0,0,1.5,1,2,6};
  assert(hasOverlap(box1, tbox1, bb1, N));

  Translation tbox1a(box2, Vector(0,0,3.001));
  assert(!hasOverlap(box1, tbox1a, bb1, N));

  Translation tbox1b(box2, Vector(0,0,3.));
  assert(hasOverlap(box1, tbox1b, bb1, N));

  // shifted along y
  Translation tbox2(box2, Vector(0,1.999,0));
  BoundingBox bb2={0,1,0,1,4,3};
  assert(hasOverlap(box1, tbox2, bb2, N));

  Translation tbox2a(box2, Vector(0,2.001,0));
  assert(!hasOverlap(box1, tbox2a, bb2, N));
}

void test2()
{
  Cylinder outcyl1(3, 3), incyl1(2, 5);
  Cylinder outcyl2(2, 3), incyl2(1, 5);
  Difference hcyl1(outcyl1, incyl1);
  Difference hcyl2(outcyl2, incyl2);
  BoundingBox bb={0,0,0, 6,6,3};
  assert(hasOverlap(hcyl1, hcyl2, bb, N));
}

void test2a()
{
  Cylinder outcyl1(3, 3), incyl1(2, 5);
  Cylinder outcyl2(1.9999, 3), incyl2(1, 5);
  Difference hcyl1(outcyl1, incyl1);
  Difference hcyl2(outcyl2, incyl2);
  BoundingBox bb={0,0,0, 6,6,3};
  assert(!hasOverlap(hcyl1, hcyl2, bb, N));
}

void test2b()
{
  Cylinder outcyl1(3, 3), incyl1(2, 5);
  Cylinder outcyl2(2.000001, 3), incyl2(1, 5);
  Difference hcyl1(outcyl1, incyl1);
  Difference hcyl2(outcyl2, incyl2);
  BoundingBox bb={0,0,0, 6,6,3};
  assert(hasOverlap(hcyl1, hcyl2, bb, N));
}

int main()
{
  test1();
  test2();
  test2a();
  test2b();
}

// End of file 
