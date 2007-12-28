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

#include "mccomposite/CompositeNeutronScatterer.h"

#include "mccomposite/boostpython_binding/wrap_scatterer.h"


namespace wrap_mccomposite {

  void wrap_CompositeNeutronScatterer()
  {

    using namespace mccomposite::boostpython_binding;

    scatterer_wrapper<CompositeNeutronScatterer>::wrap
      ("CompositeNeutronScatterer", 

       init< const AbstractShape &, 
       const CompositeNeutronScatterer::scatterercontainer_t &, 
       const CompositeNeutronScatterer::geometer_t &> 
       () 
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3,
	with_custodian_and_ward<1,4> > > () ]
       )
      ;

  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
