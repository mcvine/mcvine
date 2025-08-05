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
#include "mccomponents/kernels/detector/He3.h"
#include "mccomponents/physics/constants.h"


class He3: public mccomponents::kernels::He3 {
public:
  He3( double p ): mccomponents::kernels::He3(p) {}
  void absorb( mcni::Neutron::Event & ev )  {}
};

void test1()
{
  using namespace mccomponents;
  using namespace mccomponents::kernels;

  ::He3 he3( 1.013e5 * 10 );

  mcni::Neutron::Event ev;
  ev.state.velocity.z = 3000;

  double mu = he3.absorption_coefficient( ev ) ;
  double diameter = 0.025;
  double eff = 1-std::exp(-mu*diameter) ;

  std::cout << eff << std::endl;
  assert (eff - 0.9 < 0.01);
}


int main()
{
  test1();
  return 0;
}

// version
// $Id$

// End of file 
