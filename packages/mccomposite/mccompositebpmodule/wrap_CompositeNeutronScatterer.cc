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
    typedef CompositeNeutronScatterer w_t;

    scatterer_wrapper<w_t>::wrap
      ("CompositeNeutronScatterer", 

       init< const AbstractShape &, 
       const w_t::scatterercontainer_t &, 
       const w_t::geometer_t &> 
       () 
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3,
	with_custodian_and_ward<1,4> > > () ]
       )
      .def("checkShapeOverlap", &w_t::checkShapeOverlap)
      .add_property
      ("max_multiplescattering_loops_among_scatterers", 
       &w_t::get_max_multiplescattering_loops_among_scatterers,
       &w_t::set_max_multiplescattering_loops_among_scatterers
       )
      .add_property
      ("max_multiplescattering_loops_interactM_path1",
       &w_t::get_max_multiplescattering_loops_interactM_path1,
       &w_t::set_max_multiplescattering_loops_interactM_path1
       )
      .add_property
      ("min_neutron_probability",
       &w_t::get_min_neutron_probability,
       &w_t::set_min_neutron_probability
       )
      ;

  }
}


// version
// $Id$

// End of file 
