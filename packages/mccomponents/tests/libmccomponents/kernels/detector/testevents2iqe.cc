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
#include "drchops/events2iqe.h"
#include "mccomponents/kernels/detector/EventModeMCA.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


void test1()
{
  typedef mccomponents::detector::EventModeMCA::Event event_t;
  typedef double float_t;
  typedef const event_t * event_it_t;
  typedef double * float_it_t;

  // input events
  event_t event;
  event.pixelID = 100;
  event.tofChannelNo = 60000;
  event.n = 9.;
  event_it_t evtp = &event;

  // output intensities
  const unsigned int NX = 100, NY = 100, N = NX*NY;
  float_it_t intensities = new float_t[N];
  for (int i=0; i<N; i++) intensities[i] = 0;

  // histogram params
  float_t Qbegin=0,  Qend=10,  dQ=0.1;
  float_t Ebegin=-50, Eend=50, dE = 1.;

  // event -> qe conversion parameters
  float_t Ei = 51;
  float_t pixelPositions[3*1000];
  pixelPositions[3*100] = 1.;
  pixelPositions[3*100+1] = 1.;
  pixelPositions[3*100+2] = 3.;

  // reduce
  DANSE::reduction::events2iqe
    <event_t, float_t, event_it_t, float_it_t>
    (// input events
     evtp, evtp+1,
     // output
     intensities,
     // output histogram bin parameters
     Qbegin,  Qend,  dQ,
     Ebegin,  Eend,  dE,
     // event -> qe conversion parameters
     Ei,
     pixelPositions
     );
  
  //
  // for (int i=0; i<100; i++) {
  //   for (int j=0; j<100; j++) 
  //     std::cout << intensities[100*i+j] << ", ";
  //   std::cout << std::endl;
  // }
  
  // finalize
  delete [] intensities;
}


int main()
{
#ifdef DEBUG
  journal::debug_t("Event2QE").activate();
#endif
  test1();
  return 0;
}

// version
// $Id: testHe3.cc 601 2010-10-03 19:55:29Z linjiao $

// End of file 
