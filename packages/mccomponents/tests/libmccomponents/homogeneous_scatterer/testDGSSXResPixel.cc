// -*- C++ -*-
//

#include <iostream>
#include <cassert>
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/DGSSXResPixel.h"


// the absorber will absorb all neutrons
void test1()
{
  using namespace mccomponents;
  
  mccomposite::geometry::Cylinder cyl(0.0254/2., 0.01);
  double tof = 0.001;
  double pressure = 10.*101325;
  DGSSXResPixel pixel( tof, pressure, cyl);

  mcni::Neutron::Event event;
  event.state.position = mccomposite::geometry::Position( 0,0, -3 );
  event.state.velocity = mccomposite::geometry::Direction( 0,0, 3000);
  event.time = 0.;
  event.probability = 1.;

  pixel.scatter(event);
  std::cout << event.probability << std::endl;
  assert(event.probability > 0);
  std::cout << " - test 1 passed." << std::endl;
}


int main()
{
  test1();
  return 0;
}

// End of file 
