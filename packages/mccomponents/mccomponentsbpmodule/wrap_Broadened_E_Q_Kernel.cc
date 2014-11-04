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



#include <boost/python.hpp>

#include "wrap_Broadened_E_Q_Kernel.h"


namespace wrap_mccomponents {

  Wrap_Broadened_E_Q_Kernel::kernel_t * 
  Wrap_Broadened_E_Q_Kernel::newKernel
  (const std::string & E_Q,
   const std::string & S_Q,
   const std::string & sigma_Q,
   double Qmin, double Qmax,
   double absorption_cross_section, 
   double scattering_cross_section
   )
  {
    return new kernel_t
      (fx_t(E_Q, "Q"),
       fx_t(S_Q, "Q"),
       fx_t(sigma_Q, "Q"),
       Qmin, Qmax,
       absorption_cross_section,
       scattering_cross_section
       );
  }

  Wrap_Broadened_E_Q_Kernel::Wrap_Broadened_E_Q_Kernel()
  {
    using namespace boost::python;

    def("create_Broadened_E_Q_Kernel", 
	&newKernel,
	return_value_policy<manage_new_object>()
	);
    
    class_
      <kernel_t, 
      bases<mccomponents::AbstractScatteringKernel>,
      boost::noncopyable>
      ("Broadened_E_Q_Kernel", no_init)
      ;
  }
  
}


// version
// $Id$

// End of file 
