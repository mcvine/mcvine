// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <iostream>
#include <cassert>
#include "mcni/test/assert.h"
#include "LinearlyInterpolatedDispersionOnGrid_3D_Example.h"
#include "mccomponents/kernels/sample/phonon/ChangeCoordinateSystem_forDispersion_3D.h"


namespace test{

  void test1()
  {
    LinearlyInterpolatedDispersionOnGrid_3D_Example example;
    typedef DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D w_t;
    
    w_t::m_t transformation
      (3, 2, 1,
       1, 2, 3,
       0, 0, 1);

    w_t dispersion( example.disp, transformation );
    
    using mcni::assertNumberAlmostEqual;
    
    assertNumberAlmostEqual
      (dispersion.energy( 0, w_t::K_t(1,0,0) ), 
       example.disp.energy(0, w_t::K_t(3,1,0)) );
    
    assertNumberAlmostEqual
      ( dispersion.energy( 0, w_t::K_t(0,1,0) ),
	example.disp.energy(0, w_t::K_t(2,2,0)) );
    
    assertNumberAlmostEqual
      ( dispersion.energy( 0, w_t::K_t(0,0,1) ),
	example.disp.energy(0, w_t::K_t(1,3,1)) );
  }
}

int main()
{
  test::test1();
}


// version
// $Id$

// End of file 
