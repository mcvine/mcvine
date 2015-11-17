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


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQE_FXY_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQE_FXY_H


#include <vector>
#include "histogram/EvenlySpacedGridData_2D.h"

namespace mccomponents {

  namespace sample {

    typedef DANSE::Histogram::EvenlySpacedGridData_2D
    <double, double, double, std::vector<double>::iterator > fxy;
        
  } // sample::

} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQE_FXY_H

// version
// $Id$

// End of file 
