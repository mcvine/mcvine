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


void test1()
{
  mccomponents::random::Generator generator;
  for (size_t i=0; i<10; i++)
    std::cout << generator.generate01() << ", ";
  std::cout << std::endl;

  for (size_t i=0; i<10000000; i++) {
    double t = generator.generate01() ;
    assert( t>0.0 && t <1.0 );
  }
}


int main()
{
  test1();
  return 0;
}

// version
// $Id$

// End of file 
