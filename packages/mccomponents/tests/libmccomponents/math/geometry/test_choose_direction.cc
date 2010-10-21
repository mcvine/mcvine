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
#include "mccomponents/math/random/geometry.h"

#include "journal/debug.h"

using namespace std;
using namespace mccomponents::math;
char * jrnltag ="test_choose_direction";

typedef mcni::Vector3<double> V3;


void test1()
{
  int N = 10000;
  V3 dir;
  for (int i=0; i<N; i++) {
    choose_direction(dir);
  }
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
// $Id$

// End of file 
