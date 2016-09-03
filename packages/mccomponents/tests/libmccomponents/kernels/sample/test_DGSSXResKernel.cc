// -*- C++ -*-
//

#include <iostream>
#include <cassert>
#include <cmath>

#define DEBUG // hack
#include "mccomponents/kernels/sample/DGSSXResKernel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif



void test1()
{
  using namespace mccomponents::kernels;
  namespace conversion = mcni::neutron_units_conversion;
  
  typedef DGSSXResKernel kernel_t;
  typedef mcni::Vector3<double> V3d;
  
  kernel_t::X_t target_position(3, 0, 0);
  double target_radius=0.025;
  double tof_at_target=0.001, dtof=1e-5;
  double absorption_cross_section = 1.;
  double scattering_cross_section = 1.;
  kernel_t k
    (target_position, target_radius,
     tof_at_target, dtof,
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
  }
  
}


int main()
{
#ifdef DEBUG
  journal::debug_t("DGSSXResKernel").activate();
#endif
  test1();
  return 0;
}

// End of file 
