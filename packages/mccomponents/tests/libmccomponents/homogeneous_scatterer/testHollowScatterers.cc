// -*- C++ -*-
// Jiao Lin <jiao.lin@gmail.com>
//

/*
  Test a sample assembly with a plate at the center and a hollow cylinder can outside.
  Make sure the simulation gives the similar result as the case where there is only the plate
  (the hollow cylinder scatters several orders of magnitude less than the plate).
  
  "test1" simulate the case where is only the plate. "test2" simulate plate + can.
 */

#include <iostream>
#include <cassert>
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


// only scattering
class ToX : public mccomponents::AbstractScatteringKernel {
public:
  double m_xs;
  
  ToX(double xs) :
    m_xs(xs)
  {}
  double absorption_coefficient( const mcni::Neutron::Event & ev ) { return 0; }
  double scattering_coefficient( const mcni::Neutron::Event & ev ) { return 0; }
  void scatter( mcni::Neutron::Event & ev ) 
  {
    ev.state.velocity.x = 1;
    ev.state.velocity.y = 0;
    ev.state.velocity.z = 0;
    ev.probability *= m_xs;
  }
  void absorb( mcni::Neutron::Event & ev ) 
  {
  }
};


double test1()
{
  using namespace mccomponents;
  using namespace mccomposite::geometry;

  // plate
  Box sample_shape(0.04, 0.06, 0.001);

  // kernels
  ToX sample_kernel(1.0);

  // scatterers
  HomogeneousNeutronScatterer::Weights weights(0, 1, 1);
  HomogeneousNeutronScatterer sample(sample_shape, sample_kernel, weights);

  // composite
  // container
  mccomposite::CompositeNeutronScatterer::scatterercontainer_t container;
  container.push_back(&sample);
  // geometer
  mccomposite::CompositeNeutronScatterer::geometer_t geometer;
  Position origin(0,0,0); RotationMatrix norot(1,0,0, 0,1,0, 0,0,1);
  geometer.remember(sample, origin, norot);
  // sample assembly
  mccomposite::CompositeNeutronScatterer sample_assembly(sample_shape, container, geometer);
  
  mcni::Neutron::Event event, event0;
  event.state.position = mccomposite::geometry::Position( 0,0, -3);
  event.state.velocity = mccomposite::geometry::Direction( 0,0, 1);
  event.probability = 1;
  event0 = event;

  double tot_scatt = 0.;
  int N = 100000;
  for (int i=0; i<N; i++) {
    event = event0;
    sample_assembly.scatter( event );
    // std::cout << event << std::endl;
    if (event.state.position[2]<0.0005 && event.probability < 2)
      tot_scatt += event.probability;
  }
  // std::cout << tot_scatt/N << std::endl; // 0.001
  return tot_scatt/N;
}

double test2()
{
  using namespace mccomponents;
  using namespace mccomposite::geometry;

  // shapes
  // can
  Cylinder cyl1(0.03, 0.06), cyl2(0.0295, 0.061);
  Difference hollow_cyl(cyl1, cyl2);
  RotationMatrix rm(1,0,0, 0,0,-1, 0,1,0);
  Rotation can_shape(hollow_cyl, rm);
  // plate
  Box sample_shape(0.04, 0.06, 0.001);
  // all_shape
  Union all_shape(sample_shape, can_shape);

  // kernels
  ToX sample_kernel(1.0), can_kernel(1e-5);

  // scatterers
  HomogeneousNeutronScatterer::Weights weights(0, 1, 1);
  HomogeneousNeutronScatterer sample(sample_shape, sample_kernel, weights);
  HomogeneousNeutronScatterer can(can_shape, can_kernel, weights);

  // composite
  // container
  mccomposite::CompositeNeutronScatterer::scatterercontainer_t container;
  container.push_back(&sample);
  container.push_back(&can);
  // geometer
  mccomposite::CompositeNeutronScatterer::geometer_t geometer;
  Position origin(0,0,0); RotationMatrix norot(1,0,0, 0,1,0, 0,0,1);
  geometer.remember(sample, origin, norot);
  geometer.remember(can, origin, norot);
  // sample assembly
  mccomposite::CompositeNeutronScatterer sample_assembly(all_shape, container, geometer);
  
  mcni::Neutron::Event event, event0;
  event.state.position = mccomposite::geometry::Position( 0,0, -3);
  event.state.velocity = mccomposite::geometry::Direction( 0,0, 1);
  event.probability = 1;
  event0 = event;

  double tot_scatt = 0.;
  int N = 1000;
  for (int i=0; i<N; i++) {
    event = event0;
    sample_assembly.scatter( event );
    // std::cout << event << std::endl;
    if (std::abs(event.state.position[2])<0.0005 && event.probability < 2)
      tot_scatt += event.probability;
  }
  // std::cout << tot_scatt/N << std::endl; // 0.001
  return tot_scatt/N;
}


int main()
{
  double s1 = test1();
  double s2 = test2();
  assert (std::abs(s1-0.001)<0.0001);
  assert (std::abs(s2-0.001)<0.0001);
  return 0;
}

// End of file 
