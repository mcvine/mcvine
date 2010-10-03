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
#include <vector>
#include <cassert>
#include <cmath>
#include "mcni/neutron/units_conversion.h"
//#include "mcni/test/assert.h"

using namespace mcni::neutron_units_conversion;

void test1()
{
  assert( std::abs(Kelvin2meV-0.08617)/Kelvin2meV < 1e-4 );
  assert( std::abs(k2v-629.719)/k2v < 1e-3 );
  assert( std::abs(v2k-1.58801E-3)/v2k < 1e-3 );
  assert( std::abs(sqrte2v-437.3949)/sqrte2v < 1e-4 );
  assert( std::abs(vsq2e-5.227e-6)/vsq2e < 1e-4 );

  std::cout << v2E(E2v(60)) << std::endl;
}



int main()
{
  test1();
}

// version
// $Id$

// End of file 
