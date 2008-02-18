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
#include "../lib/DebyeWallerFactor.h"
#include "../lib/DWFromDOS.h"

#include "DWFromDOS_Example.h"

int test1()
{
  journal::debug_t debug_DW("Debye Waller");
  debug_DW.activate();
  
  DOS<double>::f_arr e1(50), Z1(51);
  for (size_t i=0; i<50; i++) {
    e1[i] = i;
    Z1[i] = i*i;
  }
  try {
    DOS<double> dos1(e1,Z1);
    throw;
  }
  catch (DOS_Init_Error) {
    std::cout << "Great! catch dos initialization error!" << std::endl;
  }
}

int test2()
{
  DWFromDOS_Example example;
  double mass = 50.0, T = 300000.0, Q = 5.;
  example.DW_calculator->calc_DW_core( mass, T );
  double dw = example.DW_calculator->DW( Q );
  
  // now we need an oracle. 
  // since E << T ( ~50 << 30000/11. ), we can approximate
  // the BE factor to kT/E
  // Then the DW core is  \int Z(w)*(2*(kT/(hbar w))+1) / (hbar w) dw
  size_t n = 100;
  double de = (example.dos->max() - example.dos->min())/n;
  //std::cout << example.dos->max() << ", " << example.dos->min() << std::endl;
  //std::cout << de << std::endl;
  double e, Z;
  double core = 0;
  const double &T2E = Physics::Units::Conversion::Kelvin2meV;

  //std::cout << n << std::endl;
  for (size_t i=0; i<n; i++) {
    e = example.dos->min() + de * i;
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
  assert ((abs(dw_oracle-dw)/dw)<0.1);
  std::cout << std::endl << "all tests for DebyeWaller passed" << std::endl;
  
}


int main()
{
  test1();
  test2();
}


// version
// $Id: test_DW.cc 635 2007-08-02 20:12:47Z linjiao $

// End of file
