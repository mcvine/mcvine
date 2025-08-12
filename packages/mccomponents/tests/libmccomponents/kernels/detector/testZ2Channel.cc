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
#include "mccomponents/kernels/detector/Z2Channel.h"


void test1()
{
  using namespace mccomponents::detector;

  typedef Z2Channel::vector_t vector_t;

  Z2Channel z2c( 1., 100, vector_t(0,0,1), vector_t(0,0,-0.5 + 0.005) );

  assert (z2c( vector_t(0,0,0.0001) ) == 50);
  assert (z2c( vector_t(0,0,0.49999) ) == 99);
  assert (z2c( vector_t(0,0,-0.49999) ) == 0);
  assert (z2c( vector_t(1,0,-0.49999) ) == 0);
  assert (z2c( vector_t(1,100,-0.49999) ) == 0);
  assert (z2c( vector_t(1,100,1.5) ) == -1);
  assert (z2c( vector_t(1,100,-1.5) ) == -1);
  assert (z2c( vector_t(1,100,0.500001) ) == -1);
  assert (z2c( vector_t(1,100,-0.500001) ) == -1);
}


int main()
{
  test1();
  return 0;
}

// version
// $Id$

// End of file 
