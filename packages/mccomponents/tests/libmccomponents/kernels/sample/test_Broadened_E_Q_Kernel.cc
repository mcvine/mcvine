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
#include "mccomponents/kernels/sample/Broadened_E_Q_Kernel.h"

// #define DEBUG

#ifdef DEBUG
#include "journal/debug.h"
#endif


struct E_Q {
  double operator() (double Q) const
  {
    return Q*Q/3.;
  }
};

struct Sigma_Q {
  double operator() (double Q) const
  {
    return Q*0.5;
  }
};


void test1()
{
  using namespace mccomponents::sample;
  using namespace mccomponents::kernels;
  namespace conversion = mcni::neutron_units_conversion;
  
  typedef Broadened_E_Q_Kernel<E_Q, IdentitySQ, Sigma_Q> kernel_t;
  typedef mcni::Vector3<double> V3d;
  
  double Qmin = 0., Qmax = 20;
  double absorption_cross_section = 1.;
  double scattering_cross_section = 1.;
  kernel_t k
    ( 
     E_Q(),
     IdentitySQ(),
     Sigma_Q(),
     Qmin, Qmax,
     absorption_cross_section,
     scattering_cross_section
      );
  
  using namespace mcni::Neutron;
  Event ni
    (State
     ( State::position_t(0,0,0), 
       State::velocity_t(0,0,7750), 
       State::spin_t() ),
     0, 1.);

  V3d vi = ni.state.velocity;
  double Ei = conversion::v2E(vi.length());
  
  for (int i=0; i<10; i++) {
    Event n = ni;
    k.scatter(n);
    V3d vf = n.state.velocity;
    V3d vdiff = vi-vf;
    double Q = conversion::v2k * vdiff.length();
    double vfl = vf.length();
    double Ef = conversion::v2E(vfl);
    double E = Ei-Ef;
#ifdef DEBUG
    std::cout << "Q=" << Q << ", "
	      << "E=" << E << ", "
	      << "n=" << n << ", "
	      << "dE=" << E-Q*Q/3.
	      << std::endl;
#endif
  }
  
}


int main()
{
#ifdef DEBUG
  journal::debug_t("Broadened_E_Q_Kernel").activate();
#endif
  test1();
  return 0;
}

// version
// $Id: test_SQkernel.cc 601 2010-10-03 19:55:29Z linjiao $

// End of file 
