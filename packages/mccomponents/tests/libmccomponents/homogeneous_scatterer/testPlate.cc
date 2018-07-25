// -*- C++ -*-
//


// timing at heetuu:
// 1e6: 50s
// 3e6: 147s
// 6e6: 293s
// 1e7: 491s
// 3e7: 1473s
// 6e7: 3005s
// 1e8: 4977s

#include <iostream>
#include <cassert>
#include <cmath>
#include "mccomponents/math/random.h"
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"

class Isotropic : public mccomponents::AbstractScatteringKernel {
public:
  Isotropic( ) :
    absorbed(0.)
  {}
  double absorption_coefficient( const mcni::Neutron::Event & ev ) { return 100; }
  double scattering_coefficient( const mcni::Neutron::Event & ev ) { return 100; }
  void scatter( mcni::Neutron::Event & ev ) 
  {
    double z = mccomponents::math::random(-1., 1.);
    double cos_theta = z, sin_theta = sqrt(1-z*z);
    double phi = mccomponents::math::random(0., 2*M_PI);
    double vlen = ev.state.velocity.length();
    ev.state.velocity.x = vlen * sin_theta * cos(phi);
    ev.state.velocity.y = vlen * sin_theta * sin(phi);
    ev.state.velocity.z = vlen * cos_theta;
    ev.probability *= scattering_coefficient(ev);
  }
  double absorbed;
  void absorb( mcni::Neutron::Event & ev ) 
  {
    absorbed += ev.probability;
    ev.probability = -1;
  }
};


void test2()
{
  using namespace mccomponents;
  
  mccomposite::geometry::Box box(0.05,0.10,0.002);
  Isotropic kernel;
  HomogeneousNeutronScatterer::Weights weights(0, 1, 0);

  HomogeneousNeutronScatterer scatterer( box, kernel, weights );

  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 3000 );

  size_t N = 1000000;
  for (size_t i=0; i<N; i++) {
    event = save;
    scatterer.scatter( event );
    // uncomment the following to generate data useful for checking dark-angle
    /*
    std::cout
      << event.state.velocity.x << "\t"
      << event.state.velocity.y << "\t"
      << event.state.velocity.z << "\t"
      << event.probability << "\n";
    */
  }
  // std::cout << " - test 2 passed." << std::endl;
}

/*
Use the following python code to look at the I vs cos(theta) plot, which 
should show a dip of dark angle.

import numpy as np
a = np.loadtxt('./log.testPlate')
p = a[:, -1]
z = a[:, 2]
cost = z/3000.
I, edges = np.histogram(cost, weights=p)
centers = (edges[:-1] + edges[1:])/2
from matplotlib import pyplot as plt
plt.plot(centers, I)
plt.ylim(0, np.max(I)*1.1)
plt.show()
 */

int main()
{
  test2();
  return 0;
}

// End of file 
