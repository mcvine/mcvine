// -*- C++ -*-
//
//


#include <cassert>
#include <iostream>
#include "mccomposite/geometry/shapes.h"
#include "mccomposite/geometry/visitors/BoundingBoxMaker.h"


using namespace mccomposite::geometry;

void test1()
{
  Box box(1,2,3);
  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(box);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0.);
  assert (bb.sx==1.);
  assert (bb.sy==2.);
  assert (bb.sz==3.);
}

void test1a()
{
  Cylinder cylinder(1,2);
  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(cylinder);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0.);
  assert (bb.sx==2.);
  assert (bb.sy==2.);
  assert (bb.sz==2.);
}

void test1b()
{
  Sphere sphere(1);
  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(sphere);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0.);
  assert (bb.sx==2.);
  assert (bb.sy==2.);
  assert (bb.sz==2.);
}

void test1c()
{
  Pyramid pyramid(2,3, 5);
  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(pyramid);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==-2.5);
  assert (bb.sx==2.);
  assert (bb.sy==3.);
  assert (bb.sz==5.);
}

void test2()
{
  Box box(1,1,1);
  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(box);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0);
  assert (bb.sx==1.);
  assert (bb.sy==1.);
  assert (bb.sz==1.);
}

/*
void test3()
{
  Box box1(1,1,1);
  Box box2(2,2,2);
  Difference diff(box2, box1);
  assert (locate( Position(0,0,0), diff ) == Locator::outside);
  assert (locate( Position(0,0,0.51), diff ) == Locator::inside);
  assert (locate( Position(0,0,0.5), diff ) == Locator::onborder);
}

void test4()
{
  Box box(1,1,1);
  Translation translation(box, Vector(0,0,0.5));

  Intersection intersection(box, translation);

  assert (locate( Position(0,0,0), intersection ) == Locator::onborder);
  assert (locate( Position(0,0,0.51), intersection ) == Locator::outside);
  assert (locate( Position(0,0,0.2), intersection ) == Locator::inside);

  Box box1(2,2,2);
  Intersection intersection2(box1, translation);
  assert (locate( Position(0,0,1), intersection2 ) == Locator::onborder);
  assert (locate( Position(0,0,0), intersection2 ) == Locator::onborder);

  Cylinder cylinder(2,2);
  Sphere sphere(2);
  Intersection intersection3(cylinder, sphere);
  assert (locate( Position(0,0,1), intersection3 ) == Locator::onborder);
  assert (locate( Position(0,0,2), intersection3 ) == Locator::outside);

}

void test5()
{
  Box box(1,1,1);
  Translation translation(box, Vector(0,0,0.5));

  Union aunion(box, translation);

  assert (locate( Position(0,0,0), aunion ) == Locator::inside);
  assert (locate( Position(0,0,1.01), aunion ) == Locator::outside);
  assert (locate( Position(0,0,1.00), aunion ) == Locator::onborder);
}

void test6()
{
  Box box(1,1,1);
  Dilation dilation(box, 5);

  assert (locate( Position(0,0,0), dilation ) == Locator::inside);
  assert (locate( Position(0,0,2.51), dilation ) == Locator::outside);
  assert (locate( Position(0,0,2.50), dilation ) == Locator::onborder);
}

void test7()
{
  Box box(1,1,10);
  RotationMatrix m(1,0,0,
		   0,0,1,
		   0,-1,0);
  Rotation rotated(box, m);

  assert (locate( Position(0,0,0), rotated ) == Locator::inside);
  assert (locate( Position(0,5.001, 0), rotated ) == Locator::outside);
  assert (locate( Position(0,5.0, 0), rotated ) == Locator::onborder);
}
*/
int main()
{
  test1();
  test1a();
  test1b();
  test1c();
  test2();
  /*
  test3();
  test4();
  test5();
  test6();
  test7();
  */
}

// End of file 
