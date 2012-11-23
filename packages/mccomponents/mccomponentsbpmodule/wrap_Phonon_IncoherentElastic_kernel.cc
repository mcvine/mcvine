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
#include "mccomponents/kernels/sample/phonon/IncoherentElastic.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_Phonon_IncoherentElastic_kernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    typedef mccomponents::kernels::phonon::IncoherentElastic w_t;

    kernel_wrapper<w_t>::wrap
      ( "Phonon_IncoherentElastic_kernel",
	init<
	const w_t::atoms_t &, // atoms
	w_t::float_t, // unitcell_vol. AA**3
	w_t::float_t // dw_core. AA**2
	> ()
	[with_custodian_and_ward<1,2> () ]
	)
      ;
    
  }

}


// version
// $Id: wrap_Phonon_IncoherentElastic_kernel.cc 603 2010-10-04 15:58:16Z linjiao $

// End of file 
