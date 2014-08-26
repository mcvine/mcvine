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
#include "mccomposite/mccomposite.h"
#include "mccomponents/homogeneous_scatterer/CompositeScatteringKernel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


class Kernel1: public mccomponents::AbstractScatteringKernel {
public:
  Kernel1( double mu, double sigma ) 
    : absorbed(0),
      scattered(0),
      m_mu(mu), 
      m_sigma(sigma),
      n_absorbed(0),
      n_scattered(0)
  {}
  virtual double absorption_coefficient( const mcni::Neutron::Event & ev )
  {
    return m_mu;
  }
  virtual double scattering_coefficient( const mcni::Neutron::Event & ev )
  {
    return m_sigma;
  }
  virtual void scatter( mcni::Neutron::Event & ev ) 
  {
    scattered += ev.probability; n_scattered ++;
    return;
  }
  virtual void absorb( mcni::Neutron::Event & ev ) 
  {
    absorbed += ev.probability; n_absorbed ++;
  }
  double absorbed, scattered, m_mu, m_sigma;
  int n_scattered, n_absorbed;
};



void test1()
{
  using namespace mccomponents;

  Kernel1 kernel1(2,1), kernel2(2,2);
  CompositeScatteringKernel::kernels_t kernels;
  kernels.push_back( &kernel1 );
  kernels.push_back( &kernel2 );
  std::vector<double> weights;
  weights.push_back(1); weights.push_back(1);
  CompositeScatteringKernel csk( kernels, weights, 0);
  
  mcni::Neutron::Event event, save;
  save.state.position = mccomposite::geometry::Position( 0,0, -5 );
  save.state.velocity = mccomposite::geometry::Direction( 0,0, 1 );
  
  event = save;
  
  assert (csk.absorption_coefficient( event ) == 2);
  assert (csk.scattering_coefficient( event ) == 3);

  size_t N = 10000;
  for (size_t i=0; i<N; i++) {
    event = save;
    csk.scatter( event );
  }
  
  assert( std::abs(kernel1.scattered-N) < std::sqrt(N) * 2 );
  assert( std::abs(kernel2.scattered-N) < std::sqrt(N) * 2 );
  assert( std::abs(kernel1.n_scattered-N/2.) < std::sqrt(N) * 2 );
  assert( std::abs(kernel2.n_scattered-N/2.) < std::sqrt(N) * 2 );

  for (size_t i=0; i<N; i++) {
    event = save;
    csk.absorb( event );
  }
  
  assert( std::abs(kernel1.absorbed-N) < std::sqrt(N) * 2 );
  assert( std::abs(kernel2.absorbed-N) < std::sqrt(N) * 2 );
  assert( std::abs(kernel1.n_absorbed-N/2.) < std::sqrt(N) * 2 );
  assert( std::abs(kernel2.n_absorbed-N/2.) < std::sqrt(N) * 2 );
}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
  // journal::debug_t("CompositeNeutronScatterer_Impl").activate();
#endif
  test1();
  return 0;
}

// version
// $Id$

// End of file 
