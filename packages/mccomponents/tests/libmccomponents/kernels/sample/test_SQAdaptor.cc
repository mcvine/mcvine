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
#include "mccomponents/kernels/sample/SQkernel.h"
#include "mccomponents/kernels/sample/SQAdaptor.h"


class TSQ {
public:
  double operator () ( double Q ) const 
  {
    return Q;
  }
};


void test1()
{
  using namespace mccomponents::sample;
  using namespace mccomponents::kernels;
  
  double absorption_cross_section = 0.0, scattering_cross_section = 0.0;
  TSQ tsq;
  SQAdaptor<TSQ> adapted(tsq);
  double Qmin = 0., Qmax = 10.;
  SQkernel k( absorption_cross_section,
	      scattering_cross_section,
	      adapted,
	      Qmin, Qmax);
  
  using namespace mcni::Neutron;
  Event ni(State( State::position_t(0,0,0), State::velocity_t(0,0,3000), State::spin_t() ),
	   0, 1.);
  
  for (int i=0; i<10; i++) {
    Event n = ni;
    k.scatter(n);
    std::cout << n << std::endl;
  }
}


int main()
{
  test1();
  return 0;
}

// version
// $Id$

// End of file 
