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
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"

using namespace std;
using namespace mccomposite::geometry;


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



int main()
{
  test1();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
