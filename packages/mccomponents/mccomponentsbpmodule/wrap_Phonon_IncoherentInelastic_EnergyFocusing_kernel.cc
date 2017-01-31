// -*- C++ -*-
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/IncoherentInelastic_EnergyFocusing.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"
#include "mccomponents/kernels/sample/phonon/AbstractDOS.h"
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"


namespace wrap_mccomponents {

  void wrap_Phonon_IncoherentInelastic_EnergyFocusing_kernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::phonon::IncoherentInelastic_EnergyFocusing w_t;

    kernel_wrapper<w_t>::wrap
      ( "Phonon_IncoherentInelastic_EnergyFocusing_kernel",
	init<
	const w_t::atoms_t &, // atoms
	w_t::float_t, // unitcell_vol. AA**3
	w_t::float_t, w_t::float_t, // Ef, dEf
	w_t::dos_t &, // DOS
	w_t::dwcalculator_t &, // Debye Waller calculator
	w_t::float_t, // temperature. K
	w_t::float_t, // average mass. atomic weight. default 0
	w_t::float_t, // total scattering xs. barn. default 0
	w_t::float_t  // total absorption xs. barn. default 0
	> ()
	[with_custodian_and_ward<1,2,
	 with_custodian_and_ward<1,6,
	 with_custodian_and_ward<1,7 > > > () ]
	)
      ;
    
  }

}

// End of file 
