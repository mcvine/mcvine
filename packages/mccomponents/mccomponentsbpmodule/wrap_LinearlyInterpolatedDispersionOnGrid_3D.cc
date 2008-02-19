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


#include "wrap_LinearlyInterpolatedDispersionOnGrid_3D.h"
#include "histogram/NdArray.h"


namespace wrap_mccomponents {

  void wrap_LinearlyInterpolatedDispersionOnGrid_3D()
  {
    typedef DANSE::Histogram::NdArray<double *, double, unsigned int, size_t, 7> array_7d_t;
    typedef DANSE::Histogram::NdArray<double *, double, unsigned int, size_t, 4> array_4d_t;
    wrap_LinearlyInterpolatedDispersionOnGrid_3D_T< array_7d_t, array_7d_t >
      ( "LinearlyInterpolatedDispersionOnGrid_3D_dblarrays" );
  }

}

// version
// $Id$

// End of file 
