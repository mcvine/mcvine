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

  EventModeMCA mca( "test.out", 100 );
  EventModeMCA::channels_t channels;
  channels.push_back( 5 );
  channels.push_back( 33 );
  channels.push_back( 1000 );

  mca.accept( channels, 2.2 );
}

void test1a()
{
  using namespace mccomponents;
  using namespace mccomponents::detector;

  std::ifstream fin("test.out");
  size_t length = sizeof(EventModeMCA::index_t) * 2 + sizeof(double);
  char * buffer = new char[length];
  fin.read( buffer, length );

  typedef EventModeMCA::Event Event;
  const Event & ev = * ( (const Event *)buffer );
  assert( ev.pixelID == 533 );
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
  return 0;
}

// version
// $Id$

// End of file 
