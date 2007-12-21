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
#include "mccomposite/geometry/shapes.h"
#include "mccomposite/geometry/visitors/ArrowIntersector.h"
#include "mccomposite/geometry/intersect.h"
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"

#include "journal/debug.h"

using namespace std;
using namespace mccomposite::geometry;
char * jrnltag ="testArrowIntersector";

template <typename T>
std::ostream & operator << 
( std::ostream & os, const std::vector<T> & v )
{
  typedef std::vector<T> V;
  for (typename V::const_iterator it = v.begin(); it<v.end(); it++)
    os << *it << ", ";
  return os;
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

  ArrowIntersector::distances_t distances = intersect(arrow, cylinder);
  assert (distances.size() == 2);
  assert (distances[0] == 4 );
  assert (distances[1] == 6 );
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
  test5();
  test6();
  test10();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
