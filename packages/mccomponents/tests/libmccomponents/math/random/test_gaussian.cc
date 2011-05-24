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
#include "mcni/test/assert.h"
#include "mccomponents/math/random/gaussian.h"

#include "journal/debug.h"

void test1()
{
  using namespace mccomponents::math;
  int N = 1000000, nbins=200;
  double xmin=-5, xmax=5;
  double x;
  double h[nbins];

  // init histogram
  for (int i=0; i<nbins; i++) h[i] = 0;

  // generate random numbers and gather histogram
  for (int i=0; i<N; i++) {
    x = normal_distrib_rand();
    int bin = (x-xmin)*nbins/(xmax-xmin);
    if (bin<0 || bin>=nbins) {
      // std::cout << "* out of bound of histogram:" << x << std::endl;
      continue;
    }
    h[ bin ] += 1;
  }
  
  // print
  for (int i=0; i<nbins; i++)
    std::cout << h[i] << std::endl;
}

int main()
{
#ifdef DEBUG
  //  journal::debug_t("mccomposite.geometry.ArrowIntersector").activate();
  //  journal::debug_t(jrnltag).activate();
#endif
  test1();
}

// version
// $Id: test_choose_direction.cc 650 2010-10-22 03:25:53Z linjiao $

// End of file 
