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


#include "wrap_LinearlyInterpolatableAxis.h"
#include "histogram/NdArray.h"


namespace wrap_mccomponents {

  void wrap_LinearlyInterpolatableAxis()
  {
    wrap_LinearlyInterpolatableAxis_T< double, unsigned int >
      ( "LinearlyInterpolatableAxis_dbl" );
  }

}

// version
// $Id$

// End of file 
