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
#include "LinearlyInterpolatedDOS_Example.h"
#include "mccomponents/kernels/sample/phonon/DWFromDOS.h"



namespace test {

  using namespace DANSE::phonon;


  struct DWFromDOS_Example {
    
    LinearlyInterpolatedDOS_Example dos_example;
    AbstractDOS<double> *dos;
    DWFromDOS<double> DW_calculator;
    
    DWFromDOS_Example () 
      : dos_example(),
	dos( dos_example.dos ),
	DW_calculator( *dos )
    {
    }
    
    ~DWFromDOS_Example() {
    }
    
  };

}


// version
// $Id$

// End of file

