// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2007 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"
#include "mccomponents/kernels/sample/phonon/CoherentInelastic_PolyXtal.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_Phonon_CoherentInelastic_PolyXtal_kernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::phonon::CoherentInelastic_PolyXtal w_t;

    kernel_wrapper<w_t>::wrap
      ( "Phonon_CoherentInelastic_PolyXtal_kernel",
	init<
	const w_t::dispersion_t &,
	const w_t::atoms_t &,
	w_t::float_t,
	w_t::dwcalculator_t & ,
	w_t::float_t,
	w_t::float_t, w_t::float_t, 
	w_t::float_t,
	size_t> ()
	[with_custodian_and_ward<1,2,
	 with_custodian_and_ward<1,3,
	 with_custodian_and_ward<1,5> > > () ]
	)
      ;
    
  }

}


// version
// $Id$

// End of file 
