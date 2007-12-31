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

#include "mccomponents/AbstractScatteringKernel.h"
#include "mccomponents/HomogeneousNeutronScatterer.h"

#include "mccomposite/boostpython_binding/wrap_scatterer.h"


namespace wrap_mccomponents {

  void wrap_HomogeneousNeutronScatterer()
  {

    using namespace mccomposite::boostpython_binding;

    scatterer_wrapper<mccomponents::HomogeneousNeutronScatterer>::wrap
      ("HomogeneousNeutronScatterer", 

       init< 
       const mccomponents::AbstractShape &, 
       mccomponents::AbstractScatteringKernel &,
       const mccomponents::HomogeneousNeutronScatterer::Weights & 
       >
       () 
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3
	> > () ]
       )
      .def( init< const mccomponents::AbstractShape &, 
	    mccomponents::AbstractScatteringKernel &,
	    const mccomponents::HomogeneousNeutronScatterer::Weights &,
	    double>
	    () 
	    [with_custodian_and_ward<1,2,
	     with_custodian_and_ward<1,3
	     > > () ] )
      ;

    
    class_<mccomponents::HomogeneousNeutronScatterer::Weights>
      ("MCWeights_AbsorptionScatteringTransmission",
       init<> ()
       )
      .def( init<double, double, double>() );
  }
}


// version
// $Id$

// End of file 
