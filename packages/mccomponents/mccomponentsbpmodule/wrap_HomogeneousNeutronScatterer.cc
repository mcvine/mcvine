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
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"

#include "mccomposite/boostpython_binding/wrap_scatterer.h"


namespace wrap_mccomponents {

  void wrap_HomogeneousNeutronScatterer()
  {

    using namespace mccomposite::boostpython_binding;
    typedef mccomponents::HomogeneousNeutronScatterer w_t;
    scatterer_wrapper<w_t>::wrap
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
      .def_readwrite("max_multiplescattering_loops", &w_t::max_scattering_loops)
      .def_readwrite("packing_factor", &w_t::packing_factor)
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
