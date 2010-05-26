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

#include <cmath>
#include <iostream>
#include <cassert>
#include "mccomponents/kernels/sample/SQE/SQE_fromexpression.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


void test1()
{
  using namespace mccomponents::sample;
  SQE_fromexpression sqe("Q+E");
 
  for (double Q=0; Q<10; Q+=0.1) {
    for (double E=0; E<40; E+=0.5) {
      double y = sqe(Q,E);
      assert (std::abs(y-(Q+E)) < 1e-6);
    }
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
