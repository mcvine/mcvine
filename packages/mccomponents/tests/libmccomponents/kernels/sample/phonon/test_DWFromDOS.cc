// -*- C++ -*-
// test Debye Waller Factor
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <iostream>
#include <cassert>

#include "DWFromDOS_Example.h"

int test2()
{
  using namespace test;
  DWFromDOS_Example example;
  double mass = 50.0, T = 300000.0, Q = 5.;
  example.DW_calculator.calc_DW_core( mass, T );
  double dw = example.DW_calculator.DW( Q );
  
  // now we need an oracle. 
  // since E << T ( ~50 << 30000/11. ), we can approximate
  // the BE factor to kT/E
  // Then the DW core is  \int Z(w)*(2*(kT/(hbar w))+1) / (hbar w) dw
  size_t n = 100;
  double de = (example.dos_example.emax - example.dos_example.emin)/n;
  //std::cout << example.dos->max() << ", " << example.dos->min() << std::endl;
  //std::cout << de << std::endl;
  double e, Z;
  double core = 0;
  const double &T2E = mccomponents::physics::Kelvin2meV;

  //std::cout << n << std::endl;
  for (size_t i=0; i<n; i++) {
    e = example.dos_example.emin + de * i;
    //std::cout << "e=" << e << std::endl;
    if (e<1e-5) continue;
    Z = (*(example.dos))( e );
    //std::cout << ", Z=" << Z << std::endl;
    core += Z*(2*(T * T2E/e) + 1) / e;
    //std::cout << ", core=" << core << std::endl;
  }
  core *= 2.072*de;
  
  double dw_oracle = core * Q*Q /mass;
  
  std::cout << dw << ", " << dw_oracle << std::endl;
  assert ((std::abs(dw_oracle-dw)/dw)<0.1);
  std::cout << std::endl << "all tests for DebyeWaller passed" << std::endl;
  
}


int main()
{
  test2();
}


// version
// $Id$

// End of file
