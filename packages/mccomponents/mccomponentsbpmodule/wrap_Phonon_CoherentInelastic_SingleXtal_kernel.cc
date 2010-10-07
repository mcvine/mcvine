// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2007-2010 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/math/rootfinding.h"
#include "mccomponents/kernels/sample/phonon/TargetCone.h"
#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"
#include "mccomponents/kernels/sample/phonon/CoherentInelastic_SingleXtal.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_Phonon_CoherentInelastic_SingleXtal_kernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;
    
    typedef mccomponents::kernels::phonon::CoherentInelastic_SingleXtal w_t;

    kernel_wrapper<w_t>::wrap
      ( "Phonon_CoherentInelastic_SingleXtal_kernel",
	init<
	const w_t::dispersion_t &,
	const w_t::atoms_t &,
	w_t::float_t,
	w_t::dwcalculator_t & ,
	w_t::float_t,
	w_t::float_t,
	const w_t::rootsfinder_t &,
	const w_t::target_region_t &,
	w_t::float_t
	> ()
	[with_custodian_and_ward<1,2,
	 with_custodian_and_ward<1,3,
	 with_custodian_and_ward<1,5,
	 with_custodian_and_ward<1,8,
	 with_custodian_and_ward<1,9> > > > > () ]
	)
      ;

  }

}


// version
// $Id$

// End of file 
