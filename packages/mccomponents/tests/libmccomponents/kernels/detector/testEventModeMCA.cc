
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
#include "mccomponents/kernels/detector/EventModeMCA.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


void test1()
{
  using namespace mccomponents;
  using namespace mccomponents::detector;

  EventModeMCA::indexes_t dims;
  dims.push_back( 10 ); // ndets
  dims.push_back( 100 ); // npixels

  EventModeMCA mca( "test.out", dims );
  EventModeMCA::channels_t channels;
  channels.push_back( 5 ); // detID
  channels.push_back( 33 ); // pixID
  channels.push_back( 1000 ); // tofchannelno

  mca.accept( channels, 2.2 );
}

void test1a()
{
  using namespace mccomponents;
  using namespace mccomponents::detector;

  typedef EventModeMCA::Event Event;

  std::ifstream fin("test.out");
  size_t length = sizeof(Event);
  char * buffer = new char[length];
  fin.read( buffer, length );

  const Event & ev = * ( (const Event *)buffer );
  assert( ev.pixelID == 533 );
  assert( ev.tofChannelNo == 1000 );
  assert( ev.n == 2.2 );
  delete [] buffer;
}



void test2()
{
  using namespace mccomponents;
  using namespace mccomponents::detector;

  EventModeMCA::indexes_t dims;
  dims.push_back( 50 ); // npacks
  dims.push_back( 10 ); // ndets
  dims.push_back( 100 ); // npixels

  EventModeMCA mca( "test.out", dims );
  EventModeMCA::channels_t channels;
  channels.push_back( 21 ); // packID
  channels.push_back( 5 ); // detID
  channels.push_back( 33 ); // pixelID
  channels.push_back( 1000 ); // tofchannelno

  mca.accept( channels, 2.2 );
}

void test2a()
{
  using namespace mccomponents;
  using namespace mccomponents::detector;

  typedef EventModeMCA::Event Event;

  std::ifstream fin("test.out");
  size_t length = sizeof(Event);
  char * buffer = new char[length];
  fin.read( buffer, length );

  const Event & ev = * ( (const Event *)buffer );
  assert( ev.pixelID == 21533 );
  assert( ev.tofChannelNo == 1000 );
  assert( ev.n == 2.2 );
  delete [] buffer;
}



int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
#endif
  test1();
  test1a();
  test2();
  test2a();
  return 0;
}

// version
// $Id$

// End of file 
