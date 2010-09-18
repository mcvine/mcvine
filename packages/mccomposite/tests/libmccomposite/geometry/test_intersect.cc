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


#include <cassert>
#include <iostream>
#include "mccomposite/geometry/shapes.h"
#include "mccomposite/geometry/intersect.h"

#include "journal/debug.h"

using namespace std;
using namespace mccomposite::geometry;
char * jrnltag ="test_intersect";


void test1()
{
  Sphere sphere( 1 );
  Translation t(sphere, Vector(0,0,2.2));
  
  std::vector<const AbstractShape *> shapes;
  shapes.push_back( &sphere );
  shapes.push_back( &t );

  Position start(0,0,-5);
  Direction direction(0,0,1);
  assert (find_1st_hit< int >( start, direction, shapes )==0);

  shapes.clear();
  shapes.push_back( &t );
  shapes.push_back( &sphere );
  assert (find_1st_hit< int >( start, direction, shapes )==1);

}

void test2()
{
  Box box1(2.1,2.1,2.1), box2(2,2,2);
  Difference box( box1, box2 );
  Sphere sphere( 1 );
  
  std::vector<const AbstractShape *> shapes;
  shapes.push_back( &box );
  shapes.push_back( &sphere );

  Position start(0,0,-5);
  Direction direction(0,0,1);
  assert (find_1st_hit< int >( start, direction, shapes )==0);

  start = Position(0, 0, -1);
  assert (find_1st_hit< int >( start, direction, shapes )==1);  

  start = Position(0, 0, -1+1e-10);
  assert (find_1st_hit< int >( start, direction, shapes )==1);  

  start = Position(0, 0, -1-1e-10);
  assert (find_1st_hit< int >( start, direction, shapes )==1);  

  start = Position(0, 0, -0.5);
  assert (find_1st_hit< int >( start, direction, shapes )==1);  

  start = Position(0, 0, 0);
  assert (find_1st_hit< int >( start, direction, shapes )==1);  

  start = Position(0, 0, 0.5);
  assert (find_1st_hit< int >( start, direction, shapes )==1);  

  start = Position(0, 0, 1);
  assert (find_1st_hit< int >( start, direction, shapes )==0);

  start = Position(0, 0, 1-1.e-10);
  assert (find_1st_hit< int >( start, direction, shapes )==0);

  start = Position(0, 0, 1+1.e-10);
  assert (find_1st_hit< int >( start, direction, shapes )==0);

  start = Position(0, 0, 1-1.e-5);
  assert (find_1st_hit< int >( start, direction, shapes )==1);

  start = Position(0, 0, 1-1.e-6);
  assert (find_1st_hit< int >( start, direction, shapes )==1);

  start = Position(0, 0, 1-1.e-7);
  assert (find_1st_hit< int >( start, direction, shapes )==0);

}


void test3()
{
  Box box(1,1,1);
  Sphere sphere1( 2), sphere2( 2.1 );
  Difference shell(sphere2, sphere1);
  
  std::vector<const AbstractShape *> shapes;
  shapes.push_back( &shell );
  shapes.push_back( &box );

  Position start(0,0,0.5);
  Direction direction(0,0,1);
  assert (find_1st_hit< int >( start, direction, shapes )==0);
}


void test4()
{
  Cylinder cyl1(0.5,1);
  Cylinder cyl2(0.1,1);
  Difference hc(cyl1, cyl2);
  
  std::vector<const AbstractShape *> shapes;
  shapes.push_back( &hc );

  Position start(-2,0,0);
  Direction direction(1,0,0);
  assert (find_1st_hit< int >( start, direction, shapes )==0);
}


void test5()
{
  Cylinder cyl1(0.002,0.1);
  Cylinder cyl2(0.,0.1);
  Difference hc(cyl1, cyl2);
  
  std::vector<const AbstractShape *> shapes;
  shapes.push_back( &hc );

  Position start(-1,0,0);
  Direction direction(1000,0,0);
  assert (find_1st_hit< int >( start, direction, shapes )==0);
}


void test6()
{
  Cylinder cyl1(0.002,0.1);
  Cylinder cyl2(0.,0.1);
  RotationMatrix m(1,-0,0, 0,0,1, 0,-1,0);
  Rotation r1(cyl1, m), r2(cyl2, m);
  Difference hc(r1, r2);
  
  std::vector<const AbstractShape *> shapes;
  shapes.push_back( &hc );

  Position start(-1,0,0);
  Direction direction(1000,0,0);
  assert (find_1st_hit< int >( start, direction, shapes )==0);
}


void test7()
{
  Cylinder cyl1(0.002,0.1);
  Cylinder cyl2(0.,0.1);
  RotationMatrix m(1,-0,0, 0,6.12323e-17,1, 0,-1,6.12323e-17);
  Rotation r1(cyl1, m), r2(cyl2, m);
  Difference hc(r1, r2);
  RotationMatrix mI(1,0,0, 0,1,0, 0,0,1);
  Rotation hcr(hc, mI);
  Vector t(0,0,0);
  Translation hcrt(hcr, t);
  
  std::vector<const AbstractShape *> shapes;
  shapes.push_back( &hcrt );

  Position start(0,0,-3);
  Direction direction(0,0,3659.51);
  assert (find_1st_hit< int >( start, direction, shapes )==0);
}


int main()
{
#ifdef DEBUG
//   journal::debug_t("mccomposite.geometry.ArrowIntersector").activate();
//   journal::debug_t("mccomposite.geometry.Locator").activate();
//   journal::debug_t("mccomposite.geometry.intersect").activate();
//   journal::debug_t(jrnltag).activate();
#endif
  test1();
  test2();
  test3();
  test4();
  test5();
  test6();
  test7();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
