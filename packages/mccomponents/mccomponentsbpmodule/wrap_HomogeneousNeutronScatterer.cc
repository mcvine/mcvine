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
#include "mccomponents/homogeneous_scatterer/AbstractAbsorptionCoefficientCalculator.h"
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"

#include "mccomposite/boostpython_binding/wrap_scatterer.h"


namespace wrap_mccomponents {

  void wrap_HomogeneousNeutronScatterer()
  {

    using namespace mccomposite::boostpython_binding;
    using namespace boost::python;
    
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
      .def(init<const mccomponents::AbstractShape &,
      	   mccomponents::AbstractScatteringKernel &,
      	   mccomponents::AbstractAbsorptionCoefficientCalculator &,
      	   const mccomponents::HomogeneousNeutronScatterer::Weights &
      	   >
      	   ()
      	   [with_custodian_and_ward<1,2,
      	    with_custodian_and_ward<1,3,
      	    with_custodian_and_ward<1,4
      	    > > > () ]
      	   )
      .def_readwrite("max_multiplescattering_loops", &w_t::max_scattering_loops)
      .def_readwrite("min_neutron_probability", &w_t::min_neutron_probability)
      .def_readwrite("packing_factor", &w_t::packing_factor)
      .def("mu", &w_t::mu)
      .def("getKernel", &w_t::getKernel, return_value_policy<reference_existing_object>())
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
