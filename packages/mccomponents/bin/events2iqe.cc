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
#include "drchops/events2iqe.h"
#include "drchops/solidangle_qe.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


template <typename value_t>
value_t fromStr(const char *s)
{
  std::istringstream iss(s);
  value_t v;
  try {
    iss >> v;
  } 
  catch (...) {
    std::cerr 
      << "failed to parse " << s 
      << std::endl;
    throw;
  }
  return v;
}


int main(int argc, char *argv[])
{
  typedef mccomponents::detector::EventModeMCA::Event event_t;
  typedef double float_t;
  typedef const event_t * event_it_t;
  typedef double * float_it_t;

#ifdef DEBUG
  journal::debug_t debug("Event2QE");
  debug.activate();
#endif


  // parse inputs
  int index = 1;
  const char * eventsfile = argv[index++];
  int nevents = fromStr<int>(argv[index++]);
  const char * outputfile = argv[index++];
  float_t Qbegin = fromStr<float_t>(argv[index++]);
  float_t Qend = fromStr<float_t>(argv[index++]);
  float_t dQ = fromStr<float_t>(argv[index++]);
  float_t Ebegin = fromStr<float_t>(argv[index++]);
  float_t Eend = fromStr<float_t>(argv[index++]);
  float_t dE = fromStr<float_t>(argv[index++]);
  float_t Ei = fromStr<float_t>(argv[index++]);
  const char * pixelpositionfile = argv[index++];
  const char * solidanglefile = argv[index++];
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
  int NQ = (Qend-Qbegin)/dQ + 0.5; Qend = Qbegin + dQ*(NQ+0.1);
  int NE = (Eend-Ebegin)/dE + 0.5; Eend = Ebegin + dE*(NE+0.1);
  const int N = NQ*NE;
  float_it_t intensities = new float_t[N];
  for (int i=0; i<N; i++) intensities[i] = 0;

  // pixel positions
  float_t * pixelpositions = new float_t[3*npixels];
  std::ifstream ppfs(pixelpositionfile);
  nbytes = sizeof(float_t) * 3 * npixels;
  ppfs.read((char *)pixelpositions, nbytes);

  // pixel solid angles
  float_t * solidangles = new float_t[npixels];
  std::ifstream safs(solidanglefile);
  nbytes = sizeof(float_t) * npixels;
  safs.read((char *)solidangles, nbytes);
  
  // reduce to iqe
  DANSE::reduction::events2iqe
    <event_t, float_t, event_it_t, float_it_t>
    (// input events
     evtp, evtp+nevents,
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

  // compute solid angles (q,e)
  float_it_t sa_arr = new float_t[N];
  for (int i=0; i<N; i++) sa_arr[i] = 0;
  typedef DRCHOPS_NAMESPACE_PREFIX::SaQE SaQE;
  SaQE sa( Qbegin, Qend, dQ,
	   Ebegin, Eend, dE,
	   sa_arr );
  DRCHOPS_NAMESPACE_PREFIX::calcSolidAngleQE<SaQE, double, unsigned int>
    (sa, Ei, 
     npixels, pixelpositions, solidangles
     );  

  // normalize iqe by saqe
  for (int i=0; i<N; i++) {
    double sa = sa_arr[i];
    if (std::abs(sa) < 1.e-10) {
      std::cerr
	<< "Error in normalizing iqe -- solid angle too small." << std::endl
	<< " - index in array: " << i 
	<< std::endl;
      intensities[i] = 0;
      continue;
    }
    intensities[i] /= sa;
  }
  
  // write out
  std::ofstream ofs(outputfile);
  ofs.write((char *)intensities, N * sizeof(float_t));

  std::cout << NQ << ", " << NE << std::endl;
  //
  // for (int i=0; i<100; i++) {
  //   for (int j=0; j<100; j++) 
  //     std::cout << intensities[100*i+j] << ", ";
  //   std::cout << std::endl;
  // }
  
  // finalize
  delete [] pixelpositions;
  delete [] solidangles;
  delete [] intensities;
  delete [] evtp;

  return 0;
}


// version
// $Id: testHe3.cc 601 2010-10-03 19:55:29Z linjiao $

// End of file 
