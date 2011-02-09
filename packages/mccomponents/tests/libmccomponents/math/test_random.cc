// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include <iostream>
#include <cassert>
#include "mccomponents/math/random.h"


using namespace mccomponents;

void test1()
{
  for (size_t i=0; i<10000000; i++) {
    double t = math::random01() ;
    assert( t>0.0 && t <1.0 );
  }
}


int main()
{
  std::cout << "== \"random\" tests ==" << std::endl;
  test1();
  std::cout << "* All tests passed" << std::endl;
  return 0;
}

// version
// $Id$

// End of file 
