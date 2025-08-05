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
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"



class Absorber : public mccomponents::AbstractScatteringKernel {
public:
  double absorption_coefficient( const mcni::Neutron::Event & ev ) { return 1e20; }
  double scattering_coefficient( const mcni::Neutron::Event & ev ) { return 0; }
  void scatter( mcni::Neutron::Event & ev ) 
  {
    double tmp = ev.state.velocity.z;
    ev.state.velocity.z  = ev.state.velocity.x;
    ev.state.velocity.x = tmp;
  }
  void absorb( mcni::Neutron::Event & ev ) { ev.probability = -1; }
};


class ToX : public mccomponents::AbstractScatteringKernel {
public:
  ToX( ) :
    absorbed(0)
  {}
  double absorption_coefficient( const mcni::Neutron::Event & ev ) { return 0.5; }
  double scattering_coefficient( const mcni::Neutron::Event & ev ) { return 0.5; }
  void scatter( mcni::Neutron::Event & ev ) 
  {
    ev.state.velocity.x = 1;
    ev.state.velocity.y = 0;
    ev.state.velocity.z = 0;
    ev.probability *= scattering_coefficient(ev);
  }
  double absorbed;
  void absorb( mcni::Neutron::Event & ev ) 
  {
    absorbed += ev.probability;
    ev.probability = -1;
  }
};


// the absorber will absorb all neutrons
void test1()
{
  using namespace mccomponents;
  
  mccomposite::geometry::Box box(1,1,1);
  Absorber kernel;
  HomogeneousNeutronScatterer::Weights weights;

  HomogeneousNeutronScatterer absorber( box, kernel, weights );

  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );
  save.probability = 1.;
  
  size_t absorbed = 0, scattered = 0, transmitted = 0;
  size_t N = 1000;
  for (size_t i=0; i<N; i++) {
    event = save;
    absorber.scatter( event );
    if (event.probability<=0) absorbed ++;
  }
  assert( absorbed == N);
  std::cout << " - test 1 passed." << std::endl;
}


void test2()
{
  using namespace mccomponents;
  
  mccomposite::geometry::Box box(1,1,1);
  ToX kernel;
  HomogeneousNeutronScatterer::Weights weights(0, 1, 0);

  HomogeneousNeutronScatterer scatterer( box, kernel, weights );

  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );

  size_t N = 1000, Ndivision = 3;
  std::vector<size_t> Nz(Ndivision);
  for (size_t i=0; i<N; i++) {
    event = save;
    scatterer.scatter( event );
    assert (event.state.position.x == 0.5);
    assert (event.state.position.y == 0);
    assert (event.state.position.z < 0.5 && event.state.position.z > -0.5);

    Nz[ size_t( (event.state.position.z + 0.5) * Ndivision ) ] ++;
    
    assert (event.state.velocity.x == 1);
    assert (event.state.velocity.y == 0);
    assert (event.state.velocity.z == 0);
  }

  for (int i=0; i<Ndivision; i++) {
    //std::cout << Nz[i] << std::endl;
    assert (std::abs(Nz[i] - 1.*N/Ndivision) <  3. * std::sqrt( N/Ndivision ) );
  }
  std::cout << " - test 2 passed." << std::endl;
}


// kernels with transmission, absorption, and scattering.
// Check the fractional distribution among these three processes.
// A bunch of same neutrons along z direction are
// sent to a "stick".
void test3()
{
  using namespace mccomponents;
  
  mccomposite::geometry::Box box(0.01,0.01,1);
  ToX kernel;
  HomogeneousNeutronScatterer::Weights weights(0.1, 1, 1);
  
  HomogeneousNeutronScatterer scatterer( box, kernel, weights );

  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );

  size_t N = 10000;
  double scattered = 0, transmitted = 0;
  size_t nscattered = 0, ntransmitted = 0, nabsorbed =0;
  for (size_t i=0; i<N; i++) {
    event = save;
    scatterer.scatter( event );
    if (event.probability < 0) nabsorbed ++;
    else if (event.state.velocity.x == 1) {
      scattered += event.probability;
      nscattered ++;
    } 
    else {
      transmitted += event.probability;
      ntransmitted ++;
    }
  }

  double absorbed = kernel.absorbed;

  /*
  std::cout << "absorbed, scattered, transmitted = " 
	    << absorbed << ", "
	    << scattered << ", "
	    << transmitted
	    << std::endl;
  */
  assert ( std::abs(transmitted-N*std::exp(-1)) < 2* sqrt(N) );
  assert ( std::abs(absorbed-N*(1-std::exp(-1))/2.) < 2* sqrt(N) );
  assert ( std::abs(scattered-N*(1-std::exp(-1))/2.) < 2* sqrt(N) );
  std::cout << " - test 3 passed." << std::endl;
}


void test4()
{
  using namespace mccomponents;

  double Y=0.01, Z=0.01, X=1;

  mccomposite::geometry::Box box(X,Y,Z);
  ToX kernel;
  HomogeneousNeutronScatterer::Weights weights(1, 1, 1);

  HomogeneousNeutronScatterer scatterer( box, kernel, weights );

  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );

  size_t N = 10000;
  double scattered = 0, transmitted = 0;
  size_t nscattered = 0, ntransmitted = 0, nabsorbed = 0;
  for (size_t i=0; i<N; i++) {
    event = save;
    scatterer.scatter( event );
    if (event.probability < 0) nabsorbed++;
    else if (event.state.velocity.x == 1) {
      scattered += event.probability;
      nscattered ++;
    } 
    else {
      transmitted += event.probability;
      ntransmitted ++;
    }
  }

  double absorbed = kernel.absorbed;

  /*
  std::cout << "nabsorbed, nscattered, ntransmitted = " 
	    << nabsorbed << ", "
	    << nscattered << ", "
	    << ntransmitted
	    << std::endl;

  std::cout << "absorbed, scattered, transmitted = " 
	    << absorbed << ", "
	    << scattered << ", "
	    << transmitted
	    << std::endl;
  */

  double expected = N*std::exp(-Z);
  //std::cout << expected << std::endl;
  assert ( std::abs(transmitted-expected) < 3*sqrt(expected) );
  expected = N*(1-std::exp(-Z))/2.;
  //std::cout << expected << std::endl;
  assert ( std::abs(absorbed-expected) < 3* sqrt(expected) );
  expected = N*(1-std::exp(-Z))/2. *std::exp(-0.5);
  //std::cout << expected << std::endl;
  assert ( std::abs(scattered-expected) < 3* sqrt(expected) );
  std::cout << " - test 4 passed." << std::endl;
}


void test5()
{
  using namespace mccomponents;
  
  mccomposite::geometry::Box box(1,1,1);
  Absorber kernel;
  HomogeneousNeutronScatterer::Weights weights;

  HomogeneousNeutronScatterer absorber( box, kernel, weights );

  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );
  event = save;
  
  mcni::Neutron::Events events;
  
  absorber.scatterM( event, events );
  
  assert (events.size()==0);
  std::cout << " - test 5 passed." << std::endl;
}


void test6()
{
  using namespace mccomponents;
  double size = 1e-4;
  mccomposite::geometry::Box box(size, size, size);
  ToX kernel;
  HomogeneousNeutronScatterer::Weights weights;

  HomogeneousNeutronScatterer scatterer( box, kernel, weights );
  
  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );
  event = save;
  
  mcni::Neutron::Events events;
  
  scatterer.scatterM( event, events );
  
  assert ( events.size() > 1 );
  size_t max_scatterings =  log10( size/HomogeneousNeutronScatterer::minimum_neutron_event_probability)/log10(1/size) + 2 ;
  assert ( events.size() <= max_scatterings );

  // scattered events should consists of
  //  - barely attenuated neutron along (0,0,1)
  //  - scattered to (1,0,0) with probability in the order of "size/2"
  //  - addtional neutrons to (1,0,0) with probability in the order of "size/2^n"
  // std::cout << events << std::endl;
  mcni::Neutron::Event event0 = events[0];
  assert (event0.state.velocity[0]==0);
  assert (event0.state.velocity[1]==0);
  assert (event0.state.velocity[2]==1);
  assert (std::abs(1-event0.probability)< 1e-3);

  mcni::Neutron::Event event1 = events[1];
  assert (event1.state.velocity[0]==1);
  assert (event1.state.velocity[1]==0);
  assert (event1.state.velocity[2]==0);
  assert (std::abs(size/2-event1.probability)< size*1e-3);

  mcni::Neutron::Event event2 = events[2];
  assert (event2.state.velocity[0]==1);
  assert (event2.state.velocity[1]==0);
  assert (event2.state.velocity[2]==0);
  double expected = (size*0.5) * (size*0.5)/2;
  assert (std::abs(event2.probability-expected) < expected*1e-3);

  std::cout << " - test 6 passed." << std::endl;
}

// calculate_attenuation
void test7()
{
  using namespace mccomponents;
  using namespace mccomposite::geometry;
  
  Box box1(1,1,1);
  Box box2(2,2,2);
  Difference diff(box2, box1);
  
  ToX kernel;
  HomogeneousNeutronScatterer::Weights weights(0, 1, 0);
  
  HomogeneousNeutronScatterer scatterer( diff, kernel, weights );
  
  mcni::Neutron::Event event;
  event.state.position = mccomposite::geometry::Position( 0,0, 0);
  event.state.velocity = mccomposite::geometry::Direction( 0,0, 1);
  event.probability = 1;
  mccomposite::geometry::Position end(0,0,4);
  
  // start from center, go out
  assert(std::abs(scatterer.calculate_attenuation(event, end)-0.60653) < 1e-6);
  
  // start from outside, go through center
  event.state.position = mccomposite::geometry::Position( 0,0, -5);
  assert(std::abs(scatterer.calculate_attenuation(event, end)-std::exp(-1)) < 1e-6);
  
  // start from inside right wall, go out
  event.state.position = mccomposite::geometry::Position( 0,0, 0.75);
  assert(std::abs(scatterer.calculate_attenuation(event, end)-std::exp(-0.25)) < 1e-6);  
  
  // start from inside left wall, go thru and out
  event.state.position = mccomposite::geometry::Position( 0,0, -0.75);
  assert(std::abs(scatterer.calculate_attenuation(event, end)-std::exp(-0.75)) < 1e-6);  
  
  // go through the side wall in the long way
  event.state.position = mccomposite::geometry::Position( 0.75,0, -5);
  assert(std::abs(scatterer.calculate_attenuation(event, end)-std::exp(-2)) < 1e-6); 
  
  // fly by the way
  event.state.position = mccomposite::geometry::Position( 1, 0, -5);
  assert(std::abs(scatterer.calculate_attenuation(event, end)-1) < 1e-6);
  
  std::cout << " - test 7 passed." << std::endl;
}


int main()
{
  test1();
  test2();
  test3();
  test4();
  test5();
  test6();
  test7();
  return 0;
}

// version
// $Id$

// End of file 
