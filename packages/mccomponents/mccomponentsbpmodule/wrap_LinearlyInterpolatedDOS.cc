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


#include "wrap_LinearlyInterpolatedDOS.h"


namespace wrap_mccomponents {

  void wrap_LinearlyInterpolatedDOS()
  {
    wrap_LinearlyInterpolatedDOS_T< double, std::vector<double> >
      ( "LinearlyInterpolatedDOS_dbl" );
  }

}

// version
// $Id$

// End of file 
