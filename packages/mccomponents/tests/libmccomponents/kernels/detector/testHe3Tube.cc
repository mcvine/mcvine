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
#include "mccomponents/kernels/detector/He3Tube.h"
#include "mccomponents/physics/constants.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif

class MCA: public mccomponents::detector::AbstractMultiChannelAnalyzer {
public:
  void accept( const channels_t & channels, double n ) 
  {
    this->channels = channels;
    this->n = n;
  }

  channels_t channels;
  double n;
};

void test1()
{
  using namespace mccomponents;
  using namespace mccomponents::detector;
  using namespace mccomponents::kernels;
  typedef Z2Channel::vector_t vector_t;

  Z2Channel z2c( 1., 100, vector_t(0,0,1), vector_t(0,0,-0.5) );
  Tof2Channel t2c( 1000., 5000., 1. );

  He3Tube::channels_t tube_channels;
  tube_channels.push_back( 5 );

  MCA mca;
  He3Tube tube( 10 * physics::atm, tube_channels, z2c, t2c, mca);

  mcni::Neutron::Event event;
  event.state.position = mcni::Neutron::State::position_t( 0,0, 0.0001);
  event.probability = 10;
  event.time = 3000;
  tube.absorb( event );

  assert( mca.channels.size() == 3 );
  assert( mca.channels[0] == 5 );
  assert( mca.channels[1] == 50 );
  assert( mca.channels[2] == 2000 );
}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
#endif
  test1();
  return 0;
}

// version
// $Id$

// End of file 
