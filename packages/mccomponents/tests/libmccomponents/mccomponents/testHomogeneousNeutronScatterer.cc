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
#include "mccomponents/AbstractScatteringKernel.h"
#include "mccomponents/HomogeneousNeutronScatterer.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif



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
  }
  double absorbed;
  void absorb( mcni::Neutron::Event & ev ) 
  {
    absorbed += ev.probability;
    ev.probability = -1;
  }
};


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
  
  size_t absorbed = 0, scattered = 0, transmitted = 0;
  size_t N = 1000;
  for (size_t i=0; i<N; i++) {
    event = save;
    absorber.scatter( event );
    if (event.probability==-1) absorbed ++;
    else {
      assert(event.probability < 1.e-7 );
      if (event.state.velocity.x == 1.) scattered ++;
      else {
	assert(event.state.velocity.x==0);
	assert(event.state.velocity.y==0);
	assert(event.state.velocity.z==1);
	transmitted ++;
      }
    }
  }
  assert( std::abs(absorbed*1./N - 1./3) < 2./std::sqrt(1.*N) );
  assert( std::abs(scattered*1./N - 1./3) < 2./std::sqrt(1.*N) );
  assert( std::abs(transmitted*1./N - 1./3) < 2./std::sqrt(1.*N) );

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
}


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

  std::cout << "absorbed, scattered, transmitted = " 
	    << absorbed << ", "
	    << scattered << ", "
	    << transmitted
	    << std::endl;

  assert ( std::abs(transmitted-N*std::exp(-1)) < 2* sqrt(N) );
  assert ( std::abs(absorbed-N*(1-std::exp(-1))/2.) < 2* sqrt(N) );
  assert ( std::abs(scattered-N*(1-std::exp(-1))/2.) < 2* sqrt(N) );
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

  double expected = N*std::exp(-Z);
  //std::cout << expected << std::endl;
  assert ( std::abs(transmitted-expected) < 3*sqrt(expected) );
  expected = N*(1-std::exp(-Z))/2.;
  //std::cout << expected << std::endl;
  assert ( std::abs(absorbed-expected) < 3* sqrt(expected) );
  expected = N*(1-std::exp(-Z))/2. *std::exp(-0.5);
  //std::cout << expected << std::endl;
  assert ( std::abs(scattered-expected) < 3* sqrt(expected) );
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
  std::cout << events << std::endl;
}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
  // journal::debug_t("CompositeNeutronScatterer_Impl").activate();
#endif
  test1();
  test2();
  test3();
  test4();
  test5();
  test6();
  return 0;
}

// version
// $Id$

// End of file 
