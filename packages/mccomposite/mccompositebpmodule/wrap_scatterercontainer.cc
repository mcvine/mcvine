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

#include "mccomposite/AbstractNeutronScatterer.h"
#include "wrap_vector.h"


namespace wrap_mccomposite {

  void wrap_scatterercontainer()
  {
    using namespace boost::python;
    using namespace mccomposite;

    wrap_pointer_vector<AbstractNeutronScatterer>( "NeutronScatterer" );
  }
}


// version
// $Id$

// End of file 
