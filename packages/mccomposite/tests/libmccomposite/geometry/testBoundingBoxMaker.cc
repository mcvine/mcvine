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

void test3()
{
  Box box1(1,1,1);
  Box box2(2,2,2);
  Difference diff(box2, box1);
  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(diff);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0);
  assert (bb.sx==2.);
  assert (bb.sy==2.);
  assert (bb.sz==2.);
}

void test4()
{
  Box box(1,1,1);
  Translation translation(box, Vector(0,0,0.5));

  Intersection intersection(box, translation);

  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(intersection);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0.25);
  assert (bb.sx==1.);
  assert (bb.sy==1.);
  assert (bb.sz==.5);

  Box box1(2,2,2);
  Intersection intersection2(box1, translation);
  bb = bbm.make(intersection2);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0.5);
  assert (bb.sx==1.);
  assert (bb.sy==1.);
  assert (bb.sz==1.);

  Cylinder cylinder(2,2);
  Sphere sphere(2);
  Intersection intersection3(cylinder, sphere);
  bb = bbm.make(intersection3);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0);
  assert (bb.sx==4);
  assert (bb.sy==4);
  assert (bb.sz==2.);
}

void test5()
{
  Box box(1,1,1);
  Translation translation(box, Vector(0,0,0.5));

  Union aunion(box, translation);

  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(aunion);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0.25);
  assert (bb.sx==1.);
  assert (bb.sy==1.);
  assert (bb.sz==1.5);
}

void test6()
{
  Box box(1,1,1);
  Dilation dilation(box, 5);

  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(dilation);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0);
  assert (bb.sx==5.);
  assert (bb.sy==5.);
  assert (bb.sz==5);
}

void test7()
{
  Box box(1,1,10);
  RotationMatrix m(1,0,0,
		   0,0,1,
		   0,-1,0);
  Rotation rotated(box, m);

  BoundingBoxMaker bbm;
  BoundingBox bb = bbm.make(rotated);
  assert (bb.cx==0.);
  assert (bb.cy==0.);
  assert (bb.cz==0);
  assert (bb.sx==10.);
  assert (bb.sy==10.);
  assert (bb.sz==10);
}

int main()
{
  test1();
  test1a();
  test1b();
  test1c();
  test2();
  test3();
  test4();
  test5();
  test6();
  test7();
}

// End of file 
