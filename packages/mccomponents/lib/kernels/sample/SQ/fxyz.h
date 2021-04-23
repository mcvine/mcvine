// -*- C++ -*-
//
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQ_FXYZ_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQ_FXYZ_H


#include <vector>
#include "histogram/EvenlySpacedGridData_3D.h"

namespace mccomponents {

  namespace sample {

    typedef DANSE::Histogram::EvenlySpacedGridData_3D
    <double, double, double, double, std::vector<double>::iterator > fxyz;

  } // sample::

} // mccomponents::

#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQ_FXYZ_H

// End of file
