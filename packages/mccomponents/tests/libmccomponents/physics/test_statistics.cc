// -*- C++ -*-
//
//

#include <iostream>
#include <cmath>
#include <cassert>
#include "mccomponents/physics/statistics.h"


using namespace mccomponents::physics;

bool isclose(double a, double b, double eps)
{
  return (std::abs(a/b-1)<eps);
}

void test1()
{
  double expected[] = {258.01, 25.3541, 2.11725, 0.021339, 1.58505e-17, 1.58581e-101};
  int i=0;
  for (double exponent=-1.; exponent<4; exponent++) {
    double E = std::pow(10., exponent);
    if (!isclose(BoseEinsteinDistribution(E, 300.), expected[i], 1e-5)) {
      std::cerr<< "E=" << E << ": " << BoseEinsteinDistribution(E, 300.) << "!=" << expected[i] << std::endl;
      throw;
    }
    i++;
  }
  assert( isclose(BoseEinsteinDistribution(-100., 300.), 0.021339, 1e-5) );
  std::cout << BoseEinsteinDistribution(0., 300.) << std::endl;
  assert( BoseEinsteinDistribution(1e10, 300.) == 0 );
}


int main()
{
  test1();
  std::cout << "* All tests passed" << std::endl;
  return 0;
}

// End of file 
