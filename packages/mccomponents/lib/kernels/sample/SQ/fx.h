// -*- C++ -*-
//
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQ_FX_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQ_FX_H


#include <vector>
#include "histogram/EvenlySpacedGridData_1D.h"

namespace mccomponents {

  namespace sample {

    typedef DANSE::Histogram::EvenlySpacedGridData_1D
    <double, double, std::vector<double>::iterator > fx;
        
  } // sample::

} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQ_FX_H

// End of file 
