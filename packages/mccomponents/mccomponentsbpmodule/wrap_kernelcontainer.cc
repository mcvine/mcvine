// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "wrap_vector.h"


namespace wrap_mccomponents {

  void wrap_kernelcontainer()
  {
    using namespace boost::python;
    using namespace mccomponents;

    wrap_pointer_vector<AbstractScatteringKernel>( "Kernel" );
  }
}


// version
// $Id$

// End of file 
