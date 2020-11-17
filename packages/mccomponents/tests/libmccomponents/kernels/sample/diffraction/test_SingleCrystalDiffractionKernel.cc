// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//

#include <iostream>
#include <cassert>
#include <algorithm>
#include "mccomponents/math/random.h"
#include "mccomponents/kernels/sample/diffraction/SingleCrystalDiffractionKernel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif

void test1()
{
  using namespace mccomponents::kernels;
  using namespace std;
  using namespace mccomponents::math;
  using namespace mcni::neutron_units_conversion;
  using mcni::PI;
  typedef SingleCrystalDiffractionKernel::K_t K_t;
  typedef SingleCrystalDiffractionKernel::R_t R_t;
  typedef SingleCrystalDiffractionKernel::hkllist_t hkllist_t;
  typedef SingleCrystalDiffractionKernel::hkl_t hkl_t;
  typedef SingleCrystalDiffractionKernel::float_t float_t;
  typedef std::pair<int, hkl_t> p_i_hkl_t;
  //
  std::cout << "test_SingleCrystalDiffractionKernel: Running test1" << std::endl;
  // lattice
  R_t a(3.0, 0., 0.), b(0., 3.0, 0.), c(0., 0., 3.0);
  SingleCrystalDiffractionKernel::lattice_t lattice(a, b, c);
  // hkl list sorted
  vector<p_i_hkl_t> vp;
  for (int h=-5; h<6; h++)
    for (int k=-5; k<6; k++)
      for (int l=-5; l<6; l++) {
        if (h==0 && k==0 && l==0) continue;
        hkl_t hkl = {h,k,l, 1.};
        int r2 = h*h+k*k+l*l;
        vp.push_back(make_pair(r2, hkl));
      }
  sort(vp.begin(), vp.end());
  hkllist_t hkllist;
  for (int i=0; i<vp.size(); i++) hkllist.push_back(vp[i].second);

  float_t mosaic=5./60/180*PI, delta_d_d=1e-4, absorption_cross_section=10.;
  SingleCrystalDiffractionKernel kernel(lattice, hkllist, mosaic, delta_d_d, absorption_cross_section);
  mcni::Neutron::Event ev;
  typedef mcni::Vector3<double> V_t;
  K_t ki = lattice.rc*3;
  V_t vi = ki*k2v;
  for (int i=0; i<100; i++) {
    // double vx=5.0*random(-1,1), vy=5.0*random(-1,1), vz=random(1000.0, 3000.0);
    //cout << "vx, vy, vz before scattering: " << vx <<" "<< vy << " "<< vz << endl;
    ev.state.velocity = vi;
    std::cout << "incident neutron " << ev << std::endl;
    kernel.scatter(ev);
    std::cout << "scattered neutron " << ev << std::endl;
    std::cout << std::endl;
  }

  std::cout << "test_SingleCrystalDiffractionKernel: Done" << std::endl;
}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
  journal::debug_t("SingleCrystalDiffractionKernel").activate();
#endif
  test1();
  return 0;
}

// End of file
