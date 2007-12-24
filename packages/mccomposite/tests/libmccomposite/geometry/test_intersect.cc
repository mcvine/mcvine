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



int main()
{
#ifdef DEBUG
//   journal::debug_t("mccomposite.geometry.ArrowIntersector").activate();
//    journal::debug_t("mccomposite.geometry.Locator").activate();
//    journal::debug_t("mccomposite.geometry.intersect").activate();
//   journal::debug_t(jrnltag).activate();
#endif
  test1();
  test2();
  test3();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
