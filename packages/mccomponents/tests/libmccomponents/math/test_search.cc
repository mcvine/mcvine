// -*- C++ -*-
// Jiao Lin <jiao.lin@gmail.com>

#include <iostream>
#include <cassert>
#include <string>
#include <cmath>
#include "mcni/test/assert.h"
#include "mccomponents/math/search.h"

using mcni::assertAlmostEqual;

int test1()
{
  std::cout << "* Testing " << "find_1st_bin_larger_than" << std::endl;

  double a[10] = {1,2,3,4,5,6,7,8,9,10};
  
  unsigned int index = mccomponents::math::find_1st_bin_larger_than<double, double *>(2.5, a, a+10);
  assert(index==2);
  
  index = mccomponents::math::find_1st_bin_larger_than<double, double *>(2, a, a+10);
  assert(index==1);

  index = mccomponents::math::find_1st_bin_larger_than<double, double *>(2.1, a, a+10);
  assert(index==2);

  index = mccomponents::math::find_1st_bin_larger_than<double, double *>(10.1, a, a+10);
  assert(index==10);

  index = mccomponents::math::find_1st_bin_larger_than<double, double *>(0.9, a, a+10);
  assert(index==0);

  index = mccomponents::math::find_1st_bin_larger_than<double, double *>(1.001, a, a+10);
  assert(index==1);

  index = mccomponents::math::find_1st_bin_larger_than<double, double *>(8.2, a, a+10);
  assert(index==8);

  return 0;
}


int main()
{
  std::cout << "== search tests ==" << std::endl;
  if (test1()) return 1;
  std::cout << "* All tests passed" << std::endl;
  return 0;
}

// version
// $Id$

// End of file 
