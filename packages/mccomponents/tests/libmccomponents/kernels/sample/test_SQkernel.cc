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
#include "mccomponents/kernels/sample/AbstractSQ.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


void test1()
{
  using namespace mccomponents::sample;
  using namespace mccomponents::kernels;
  
  class TSQ: public AbstractSQ {
  public:
    virtual double operator () ( double Q ) 
    {
      return Q;
    }
  };

  double absorption_cross_section = 0.0, scattering_cross_section = 0.0;
  TSQ tsq;
  double Qmin = 0., Qmax = 10.;
  SQkernel k( absorption_cross_section,
	      scattering_cross_section,
	      tsq,
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
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
#endif
  test1();
  return 0;
}

// version
// $Id$

// End of file 
