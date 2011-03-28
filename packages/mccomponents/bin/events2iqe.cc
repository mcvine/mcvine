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
#include <sstream>
#include <cassert>
#include "mccomponents/kernels/detector/EventModeMCA.h"
#include "mccomponents/kernels/detector/events2iqe.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


template <typename value_t>
value_t fromStr(const char *s)
{
  std::istringstream iss(s);
  value_t v;
  iss >> v;
  return v;
}


int main(int argc, char *argv[])
{
  typedef mccomponents::detector::EventModeMCA::Event event_t;
  typedef double float_t;
  typedef const event_t * event_it_t;
  typedef double * float_it_t;


  // parse inputs
  int index = 1;
  const char * eventsfile = argv[index++];
  int nevents = fromStr<int>(argv[index++]);
  float_t Qbegin = fromStr<float_t>(argv[index++]);
  float_t Qend = fromStr<float_t>(argv[index++]);
  float_t dQ = fromStr<float_t>(argv[index++]);
  float_t Ebegin = fromStr<float_t>(argv[index++]);
  float_t Eend = fromStr<float_t>(argv[index++]);
  float_t dE = fromStr<float_t>(argv[index++]);
  float_t Ei = fromStr<float_t>(argv[index++]);
  const char * pixelpositionfile = argv[index++];
  int npixels = fromStr<int>(argv[index++]);
  float_t tofUnit = fromStr<float_t>(argv[index++]);
  float_t mod2sample = fromStr<float_t>(argv[index++]);
  float_t toffset = fromStr<float_t>(argv[index++]);
  float_t tofmax = fromStr<float_t>(argv[index++]); 

  // input events
  event_it_t evtp = new event_t[nevents];
  std::ifstream evtsfs(eventsfile);
  int nbytes = sizeof(event_t) * nevents;
  evtsfs.read((char *)evtp, nbytes);
  
  // output intensities
  int NQ = (Qend-Qbegin)/dQ;
  int NE = (Eend-Ebegin)/dE;
  const int N = NQ*NE;
  float_it_t intensities = new float_t[N];
  for (int i=0; i<N; i++) intensities[i] = 0;

  // event -> qe conversion parameters
  float_t * pixelpositions = new float_t[3*npixels];
  std::ifstream ppfs(pixelpositionfile);
  nbytes = sizeof(float_t) * 3 * npixels;
  ppfs.read((char *)pixelpositions, nbytes);

  // reduce
  mccomponents::reduction::events2iqe
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
     pixelpositions,
     npixels,
     tofUnit, mod2sample,
     toffset, tofmax
     );
  
  //
  // for (int i=0; i<100; i++) {
  //   for (int j=0; j<100; j++) 
  //     std::cout << intensities[100*i+j] << ", ";
  //   std::cout << std::endl;
  // }
  
  // finalize
  delete [] pixelpositions;
  delete [] intensities;
  delete [] evtp;

  return 0;
}


// version
// $Id: testHe3.cc 601 2010-10-03 19:55:29Z linjiao $

// End of file 
