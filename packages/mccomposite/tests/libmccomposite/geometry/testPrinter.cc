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
#include "mccomposite/geometry/visitors/Printer.h"
#include "mccomposite/geometry/shape2ostream.h"


using namespace mccomposite::geometry;

void test1()
{
  Box box(1,2,3);
  Printer printer(std::cout);
  box.identify( printer );
  std::cout << std::endl;

  std::cout << Cylinder(1,2) << std::endl;
  std::cout << Sphere(1) << std::endl;
}


void test2()
{
  Box box1(3,3,3);
  Box box2(1,1,1);

  std::cout << Difference(box1, box2) << std::endl;
  std::cout << Intersection(box1, box2) << std::endl;
  std::cout << Union(box1, box2) << std::endl;
}


void test3()
{
  Box box(1,1,1);

  std::cout << Dilation(box, 5) << std::endl;
  std::cout << Reflection(box, Vector(0,0,1)) << std::endl;
  std::cout << Translation(box, Vector(0,0,1)) << std::endl;
  RotationMatrix rotmat(1.,0.,0.,
			0.,1.,0.,
			0.,0.,1.);
  std::cout << Rotation(box, rotmat) << std::endl;
}


int main()
{
  test1();
  test2();
  test3();
}

// version
// $Id$

// End of file 
