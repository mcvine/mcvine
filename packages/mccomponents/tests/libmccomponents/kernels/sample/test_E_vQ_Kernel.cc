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
#include <cmath>

// #define DEBUG // hack
#include "mccomponents/kernels/sample/E_vQ_Kernel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


struct Const_E_vQ {
  double operator() (double Qx, double Qy, double Qz) const
  {
    return 5;
  }
};

struct Sin_E_vQ {
  double operator() (double Qx, double Qy, double Qz) const
  {
    return 10*std::sin(Qx + Qy + Qz) + 35;
  }
};

struct S_vQ {
  double operator() (double Qx, double Qy, double Qz) const
  {
    return 1;
  }
};


void test1()
{
  using namespace mccomponents::kernels;
  namespace conversion = mcni::neutron_units_conversion;
  
  typedef E_vQ_Kernel<Const_E_vQ, S_vQ> kernel_t;
  typedef mcni::Vector3<double> V3d;
  
  double Emax = 50;
  double absorption_cross_section = 1.;
  double scattering_cross_section = 1.;
  kernel_t k
    ( 
     Const_E_vQ(),
     S_vQ(),
     Emax,
     absorption_cross_section,
     scattering_cross_section
      );
  
  using namespace mcni::Neutron;
  Event ni
    (State
     ( State::position_t(0,0,0), 
       State::velocity_t(0,0,3000), 
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
	      << "n=" << n
	      << std::endl
	      << std::endl;
#endif
    assert (std::abs(E-5) < 1.e-10);
  }
  
}


void test2()
{
  using namespace mccomponents::kernels;
  namespace conversion = mcni::neutron_units_conversion;
  
  typedef E_vQ_Kernel<Sin_E_vQ, S_vQ> kernel_t;
  typedef mcni::Vector3<double> V3d;
  
  double Emax = 50;
  double absorption_cross_section = 1.;
  double scattering_cross_section = 1.;
  Sin_E_vQ E_vQ;
  kernel_t k
    ( 
     E_vQ,
     S_vQ(),
     Emax,
     absorption_cross_section,
     scattering_cross_section
      );
  
  using namespace mcni::Neutron;
  Event ni
    (State
     ( State::position_t(0,0,0), 
       State::velocity_t(0,0,3000), 
       State::spin_t() ),
     0, 1.);

  V3d vi = ni.state.velocity;
  double Ei = conversion::v2E(vi.length());
  
  for (int i=0; i<10; i++) {
    Event n = ni;
    k.scatter(n);
    V3d vf = n.state.velocity;
    V3d vdiff = vi-vf;
    V3d vQ = vdiff * conversion::v2k;
    double Q = vQ.length();
    double expectedE = E_vQ(vQ.x, vQ.y, vQ.z);
    double vfl = vf.length();
    double Ef = conversion::v2E(vfl);
    double E = Ei-Ef;
#ifdef DEBUG
    std::cout << "Q=" << Q << ", "
	      << "E=" << E << ", "
	      << "n=" << n
	      << std::endl
	      << std::endl;
#endif
    assert (std::abs(E-expectedE) < 1.e-10);
  }
  
}


int main()
{
#ifdef DEBUG
  journal::debug_t("E_vQ_Kernel").activate();
#endif
  test1();
  test2();
  return 0;
}

// version
// $Id: test_SQkernel.cc 601 2010-10-03 19:55:29Z linjiao $

// End of file 
