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
#include "mccomposite/geometry/visitors/ArrowIntersector.h"
#include "mccomposite/geometry/intersect.h"
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"

#include "journal/debug.h"

namespace {
  using namespace std;
  using namespace mccomposite::geometry;
  char * jrnltag ="testArrowIntersector";
  double epsilon = 1e-7;

  bool isclose(double a, double b) {
    return std::abs(a-b) < epsilon;
  }
}

void test1()
{
  Box box(1,2,3);
  typedef Position position_t;
  typedef Vector direction_t;
  typedef ArrowIntersector Intersector;
  Intersector intersector;
  intersector.setArrow( position_t (0,0,-5), direction_t(0,0,1) );

  Intersector::distances_t distances = intersector.calculate_intersections( box );
  assert (distances.size() == 2);
  assert (distances[0] == 3.5 );
  assert (distances[1] == 6.5 );
}

void test2()
{
  Box box(1,2,3);
  Arrow arrow( Position (0,0,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances = intersect(arrow, box);
  assert (distances.size() == 2);
  assert (distances[0] == 3.5 );
  assert (distances[1] == 6.5 );
}

void test3()
{
  Cylinder cylinder(1,2);
  Arrow arrow( Position (0,0,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances;
  distances = intersect(arrow, cylinder);
  assert (distances.size() == 2);
  assert (distances[0] == 4 );
  assert (distances[1] == 6 );

  Cylinder cylinder1(1,1);
  Arrow arrow1( Position (0,0,-5), Direction(0,0,1) );

  distances = intersect(arrow1, cylinder1);
  assert (distances.size() == 2);
  assert (distances[0] == 4.5 );
  assert (distances[1] == 5.5 );


  arrow1.start = Position(0.22,0.35,-5);
  arrow1.direction = Direction(0,0,1);

  distances = intersect(arrow1, cylinder1);
  assert (distances.size() == 2);
  assert (distances[0] == 4.5 );
  assert (distances[1] == 5.5 );


  arrow1.start = Position(-5,0,0);
  arrow1.direction = Direction(1,0,0);

  distances = intersect(arrow1, cylinder1);
  assert (distances.size() == 2);
  assert (distances[0] == 4 );
  assert (distances[1] == 6 );


  using std::sqrt; using std::abs;
  arrow1.start = Position(sqrt(2)/2,-5,0.17);
  arrow1.direction = Direction(0,1,0);

  distances = intersect(arrow1, cylinder1);
  assert (distances.size() == 2);
  assert (abs(distances[0] - ( 5-sqrt(2)/2 ) ) < 1.e-10 );
  assert (abs(distances[1] - ( 5+sqrt(2)/2 ) ) < 1.e-10 );

}

void test4()
{
  Sphere sphere(1);

  Arrow arrow( Position (0,0,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances = intersect(arrow, sphere);
  assert (distances.size() == 2);
  assert (distances[0] == 4 );
  assert (distances[1] == 6 );

  Arrow arrow2( Position (0,0,0), Direction(0,0,1) );

  ArrowIntersector::distances_t distances2 = intersect(arrow2, sphere);
  assert (distances2.size() == 2);
  assert (distances2[0] == -1 );
  assert (distances2[1] == 1 );
}

void test4a()
{
  Pyramid pyramid(2,3,5);
  Arrow arrow( Position (0,0,-5-5), Direction(0,0,1) );
  // vertical
  ArrowIntersector::distances_t distances = intersect(arrow, pyramid);
  assert (distances.size() == 2);
  assert (distances[0] == 5 );
  assert (distances[1] == 10 );

  // horizontal along x, half height, through axis
  arrow = Arrow(Position(0,0,2.5-5), Direction(1,0,0) );
  distances = intersect(arrow, pyramid);
  assert (distances.size() == 2);
  assert (distances[0] == -0.5 );
  assert (distances[1] == 0.5 );

  // horizontal along y, half height, through axis
  arrow = Arrow(Position(0,0,2.5-5), Direction(0,1,0) );
  distances = intersect(arrow, pyramid);
  assert (distances.size() == 2);
  assert (isclose(distances[0], -0.75 ));
  assert (isclose(distances[1], 0.75 ));

  // horizontal along y, half height, not through axis
  arrow = Arrow(Position(0.5,0,2.5-5), Direction(0,1,0) );
  distances = intersect(arrow, pyramid);
  assert (distances.size() == 2);
  assert (isclose(distances[0], -0.75 ));
  assert (isclose(distances[1], 0.75 ));

  // horizontal along xy diagonal, half height, through axis
  arrow = Arrow(Position(0,0,2.5-5), Direction(1,1.5,0) );
  distances = intersect(arrow, pyramid);
  assert (distances.size() == 2);
  assert (isclose(distances[0], -.5 ));
  assert (isclose(distances[1], .5 ));
  
  // horizontal along xy diagonal, base, through axis
  arrow = Arrow(Position(0,0,0-5), Direction(1,1.5,0) );
  distances = intersect(arrow, pyramid);
  assert (distances.size() == 2);
  assert (isclose(distances[0], -1 ));
  assert (isclose(distances[1], 1 ));

  // vertical, offset from axis with dx=.5
  arrow = Arrow(Position(0.5,0,0-5), Direction(0,0,1) );
  distances = intersect(arrow, pyramid);
  // std::cout << distances << std::endl;
  assert (distances.size() == 2);
  assert (isclose(distances[0], 0 ));
  assert (isclose(distances[1], 2.5 ));
  
}

void test5()
{
  Box box1(1,1,1);
  Box box2(2,2,2);
  Difference diff(box2, box1);

  Arrow arrow( Position (0,0,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances = intersect(arrow, diff);

#ifdef DEBUG
  journal::debug_t debug(jrnltag);
  debug << journal::at (__HERE__) 
	<< distances
	<< journal::endl;
#endif

  assert (distances.size() == 4);
  assert (distances[0] == 4 );
  assert (distances[1] == 4.5 );
  assert (distances[2] == 5.5 );
  assert (distances[3] == 6 );

  Arrow arrow2( Position (0.75,0,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances2 = intersect(arrow2, diff);

  assert (distances2.size() == 2);
  assert (distances2[0] == 4 );
  assert (distances2[1] == 6 );

}

void test6()
{
  Box box(2,2,2);
  Translation translated(box, Vector(0,0,0.5));
  Union aunion(box, translated);

  Arrow arrow( Position (0,0,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances = intersect(arrow, aunion);

  assert (distances.size() == 2);
  assert (distances[0] == 4 );
  assert (distances[1] == 6.5 );

  Arrow arrow2( Position (0.5,0.5,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances2 = intersect(arrow2, aunion);

  assert (distances2.size() == 2);
  assert (distances2[0] == 4 );
  assert (distances2[1] == 6.5 );

}

// union of shapes that have same edge
void test7()
{
  Box box(2,2,2);
  Union aunion(box, box);

  Arrow arrow( Position (0,0,-5), Direction(0,0,1) );

  ArrowIntersector::distances_t distances = intersect(arrow, aunion);

  assert (distances.size() == 4);
  assert (distances[0] == 4 );
  assert (distances[1] == 4 );
  assert (distances[2] == 6 );
  assert (distances[3] == 6 );

}

void test10()
{
  Box box(1,1,1);
  Dilation dilation(box, 10);

  Arrow arrow1( Position (0,0,-4), Direction(0,0,1) );

  ArrowIntersector::distances_t distances1 = intersect(arrow1, dilation);

  assert (distances1.size() == 2);
  assert ( abs(distances1[0] - (-1)) < 1.e-7);
  assert ( abs(distances1[1] - 9) < 1.e-7);
}


int main()
{
#ifdef DEBUG
//   journal::debug_t("mccomposite.geometry.ArrowIntersector").activate();
//   journal::debug_t("mccomposite.geometry.Locator").activate();
//   journal::debug_t(jrnltag).activate();
#endif
  test1();
  test2();
  test3();
  test4();
  test4a();
  test5();
  test6();
  test7();
  test10();
}

// version
// $Id$

// End of file 
