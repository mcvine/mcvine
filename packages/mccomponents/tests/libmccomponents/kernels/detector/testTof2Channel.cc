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
#include "mccomponents/kernels/detector/Tof2Channel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


void test1()
{
  using namespace mccomponents::detector;

  Tof2Channel t2c( 1000., 5000., 1. );

  assert (t2c(3000) == 2000);
  assert (t2c(0) == -1);
  assert (t2c(10000) == -1);
}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
#endif
  test1();
  return 0;
}

// version
// $Id$

// End of file 
