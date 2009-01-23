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
    
    array_t Z(51);
    for (size_t i=0; i<51; i++) Z[i] = i*i;
    
    w_t dos(0., 1., 51, Z);
    
    size_t n(200);
    double e0 = 0, e1 = 50, de = (e1-e0)/n;
    
    double integrated = 0.;
    for (size_t i=0; i<n; i++) {
      integrated += dos.value( e0 + de*i );
    }
    integrated*=de;
    
    assert ( std::abs(integrated-1.) < 0.05 );
  }
  
}


int main()
{
  using namespace test;
  test1();
  test2();
}


// version
// $Id: test_DW.cc 610 2007-05-12 00:58:57Z linjiao $

// End of file
