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
#include "mccomponents/kernels/sample/phonon/IncoherentInelastic.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"
#include "mccomponents/kernels/sample/phonon/AbstractDOS.h"
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"


namespace wrap_mccomponents {

  void wrap_Phonon_IncoherentInelastic_kernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::phonon::IncoherentInelastic w_t;

    kernel_wrapper<w_t>::wrap
      ( "Phonon_IncoherentInelastic_kernel",
	init<
	const w_t::atoms_t &, // atoms
	w_t::float_t, // unitcell_vol. AA**3
	w_t::dos_t &, // DOS
	w_t::dwcalculator_t &, // Debye Waller calculator
	w_t::float_t // temperature. K
	> ()
	[with_custodian_and_ward<1,2,
	 with_custodian_and_ward<1,4,
	 with_custodian_and_ward<1,5 > > > () ]
	)
      ;
    
  }

}


// version
// $Id: wrap_Phonon_IncoherentInelastic_kernel.cc 603 2010-10-04 15:58:16Z linjiao $

// End of file 
