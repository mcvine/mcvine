// -*- C++ -*-
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
#include "LinearlyInterpolatedDOS_Example.h"


namespace test {

  typedef std::vector<double> array_t;
  typedef LinearlyInterpolatedDOS<double, array_t> w_t;


  void test1()
  {
    array_t Z(50);
    try {
      w_t dos(0., 1., 51, Z);
      throw;
    }
    catch (DOS_Init_Error) {
      std::cout << "Great! caught dos initialization error!" << std::endl;
    }
    
  }  
  
  void test2()
  {
    
    array_t Z(501);
    for (size_t i=0; i<501; i++) Z[i] = i*i;
    
    w_t dos(0., .1, 501, Z);
    
    size_t n(500);
    double e0 = 0, e1 = 50, de = (e1-e0)/n;
    
    double integrated = 0.;
    for (size_t i=0; i<n; i++) {
      integrated += dos.value( e0 + de*i );
    }
    integrated*=de;
    assert ( std::abs(integrated-1.) < 0.05 );

    // test method sod()
    double sod = dos.sod(), sod_expected = 3./e1/e1/e1;
    assert (std::abs(sod-sod_expected)/sod_expected < 1e-2);
    // std::cout << dos.sod() << std::endl;
  }
  
}


int main()
{
  using namespace test;
  test1();
  test2();
}


// version
// $Id$

// End of file
