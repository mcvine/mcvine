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


using namespace mccomposite;

void test1()
{
  Box box(1,2,3);
  Printer printer(std::cout);
  box.identify( printer );
  std::cout << std::endl;
}



int main()
{
  test1();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
