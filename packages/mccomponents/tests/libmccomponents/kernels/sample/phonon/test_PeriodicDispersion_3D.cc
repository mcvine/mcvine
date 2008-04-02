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
#include "LinearlyInterpolatedDispersionOnGrid_3D_Example.h"
#include "mccomponents/kernels/sample/phonon/PeriodicDispersion_3D.h"


namespace test{

  void test1()
  {
    LinearlyInterpolatedDispersionOnGrid_3D_Example example;
    typedef DANSE::phonon::PeriodicDispersion_3D w_t;
    
    w_t::ReciprocalCell rc = {w_t::K_t(2,0,0), w_t::K_t(0,2,0), w_t::K_t(0,0,2)};
    w_t dispersion( example.disp, rc );

    assert ( dispersion.energy( 0, w_t::K_t(2,0,0) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(4,0,0) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(0,2,0) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(0,4,0) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(0,0,4) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(0,0,2) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(0,2,2) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(0,4,2) ) == dispersion.energy( 0, w_t::K_t(0,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(1,2,0) ) == dispersion.energy( 0, w_t::K_t(3,0,0) ) );
    assert ( dispersion.energy( 0, w_t::K_t(1.234,4,0) ) == dispersion.energy( 0, w_t::K_t(11.234,0,0) ) );
  }

}

int main()
{
  test::test1();
}


// version
// $Id$

// End of file 
