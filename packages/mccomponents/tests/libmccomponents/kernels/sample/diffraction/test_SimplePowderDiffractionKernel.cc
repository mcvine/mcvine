// -*- C++ -*-
//
// Li Li
// Jiao Lin
//

#include <iostream>
#include <cassert>
#include "mccomponents/math/random.h"
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionData.h"
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionKernel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


void test1()
{
  using namespace mccomponents::kernels;
  
  SimplePowderDiffractionData::Peak peakarr[] = {
    {3.1353,   3.3,  8, 0, 0},
    {1.9200,   0.0, 12, 0, 0},
    {1.6374,   3.2, 24, 0, 0},
    {1.5677,   6.3,  8, 0, 0},
    {1.3576,   6.2,  6, 0, 0}
  };

  SimplePowderDiffractionData data;
  data.Dd_over_d = 1e-5;
  data.DebyeWaller_factor = 1.0;
  data.unitcell_volume = 5.43053*5.43053*5.43053;//*10e-30;
  data.density = 2.33;
  data.atomic_weight = 28.08;
  data.number_of_atoms = 16;
  data.absorption_cross_section = 0.171;
  data.incoherent_cross_section = 0.004;
  
  for (int i=0; i<5; i++) 
    data.peaks.push_back(peakarr[i]);

  SimplePowderDiffractionKernel kernel(data);

  using namespace std;
  using namespace mccomponents::math;
  mcni::Neutron::Event ev;
  typedef mcni::Vector3<double> V_t;
  
  for (int i=0; i<1000; i++) {
    double vx=5.0*random(-1,1), vy=5.0*random(-1,1), vz=random(1000.0, 3000.0);
    //cout << "vx, vy, vz before scattering: " << vx <<" "<< vy << " "<< vz << endl; 
    ev.state.velocity = V_t(vx, vy, vz);
    kernel.scatter(ev);
    
    //cout << ev << endl;
    if (ev.state.velocity.z != vz) {
	cout << "find one! " << i <<endl;
	cout << "vx, vy, vz before scattering: " << vx <<" "<< vy << " "<< vz 
	     << " total: "<< sqrt(vx*vx+vy*vy+vz*vz)<<endl;
	cout << "after scattering: " << ev << endl;
    }
  }
}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
  //journal::debug_t("SimplePowderDiffractionKernel").activate();
#endif
  test1();
  return 0;
}

// version
// $Id$

// End of file 
