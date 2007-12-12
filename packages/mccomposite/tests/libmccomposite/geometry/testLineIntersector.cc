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
#include "mccomposite/geometry/visitors/LineIntersector.h"


using namespace mccomposite;
using namespace mcni;

void test1()
{
  Box box(1,2,3);
  LineIntersector intersector;
  intersector.setArrow( Position<double> (0,0,-5), Vector3<double>(0,0,1) );

  LineIntersector::distances_t distances = intersector.calculate_intersections( box );
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
