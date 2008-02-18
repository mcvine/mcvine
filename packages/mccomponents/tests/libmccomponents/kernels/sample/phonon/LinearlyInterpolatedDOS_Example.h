// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <iostream>
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedDOS.h"


namespace test{

  using namespace DANSE::phonon;

  struct LinearlyInterpolatedDOS_Example {
    
    typedef std::vector<double> array_t;
    typedef LinearlyInterpolatedDOS<double, array_t> w_t;
    
    LinearlyInterpolatedDOS_Example () 
    {
      array_t Z(50);
      for (size_t i=0; i<50; i++) {
	Z[i] = i*i;
      }
      
      dos = new w_t(0, 1., 50, Z);
    }
    
    ~LinearlyInterpolatedDOS_Example() {
      delete dos;
    }
    
    w_t *dos;
  };

}

// version
// $Id: test_DW.cc 430 2006-03-30 17:16:55Z linjiao $

// End of file
