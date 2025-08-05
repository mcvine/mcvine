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
#include "mcni/math/number.h"
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"



class Absorber : public mccomponents::AbstractScatteringKernel {
public:
  double absorption_coefficient( const mcni::Neutron::Event & ev ) { return 1000; }
  double scattering_coefficient( const mcni::Neutron::Event & ev ) { return 0; }
  void scatter( mcni::Neutron::Event & ev ) 
  {
    double tmp = ev.state.velocity.z;
    ev.state.velocity.z  = ev.state.velocity.x;
    ev.state.velocity.x = tmp;
  }
  void absorb( mcni::Neutron::Event & ev ) { ev.probability = -1; }
};


class RotateByY : public mccomponents::AbstractScatteringKernel {
public:
  RotateByY(double i_angle=90.) :
    angle(i_angle),
    absorbed(0)
  {
    double a = angle * mcni::PI / 180.;
    cosa = std::cos(a);
    sina = std::sin(a);
  }
  double absorption_coefficient( const mcni::Neutron::Event & ev ) { return 0.5; }
  double scattering_coefficient( const mcni::Neutron::Event & ev ) { return 0.5; }
  void scatter( mcni::Neutron::Event & ev ) 
  {
    double x = ev.state.velocity.x;
    double z = ev.state.velocity.z;
    
    ev.state.velocity.x = x*cosa + z*sina;
    ev.state.velocity.z = -x*sina + z*cosa;
  }
  double angle, absorbed, cosa, sina;
  void absorb( mcni::Neutron::Event & ev ) 
  {
    absorbed += ev.probability;
    ev.probability = -1;
  }
};


void test6()
{
  using namespace mccomponents;
  double size = 1e-4;
  mccomposite::geometry::Box box(size, size, size);
  RotateByY kernel;
  HomogeneousNeutronScatterer::Weights weights;

  HomogeneousNeutronScatterer scatterer( box, kernel, weights );
  
  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );
  event = save;
  
  mcni::Neutron::Events events;
  
  scatterer.scatterM( event, events );
  std::cout << event << std::endl;
  std::cout << "events" << std::endl;
  for (int i=0; i<events.size(); i++)
    std::cout << events[i] << std::endl;
  
  // assert ( events.size() > 1 );
  // size_t max_scatterings =  log10( size/HomogeneousNeutronScatterer::minimum_neutron_event_probability)/log10(1/size) + 2 ;
  // assert ( events.size() <= max_scatterings );

  // scattered events should consists of
  //  - barely attenuated neutron along (0,0,1)
  //  - scattered to (1,0,0) with probability in the order of "size/2"
  //  - addtional neutrons to (1,0,0) with probability in the order of "size/2^n"
  // std::cout << events << std::endl;
}


int main()
{
  test6();
  return 0;
}

// version
// $Id$

// End of file 
