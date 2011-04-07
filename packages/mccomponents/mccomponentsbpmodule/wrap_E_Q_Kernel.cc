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

#include "wrap_E_Q_Kernel.h"


namespace wrap_mccomponents {

  Wrap_E_Q_Kernel::kernel_t * 
  Wrap_E_Q_Kernel::newKernel
  (const std::string & E_Q,
   const std::string & S_Q,
   double Qmin, double Qmax,
   double absorption_cross_section, 
   double scattering_cross_section
   )
  {
    return new kernel_t
      (fx_t(E_Q, "Q"),
       fx_t(S_Q, "Q"),
       Qmin, Qmax,
       absorption_cross_section,
	 scattering_cross_section
       );
  }

  Wrap_E_Q_Kernel::Wrap_E_Q_Kernel()
  {
    using namespace boost::python;

    def("create_E_Q_Kernel", 
	&newKernel,
	return_value_policy<manage_new_object>()
	);
    
    class_
      <kernel_t, 
      bases<mccomponents::AbstractScatteringKernel>,
      boost::noncopyable>
      ("E_Q_Kernel", no_init)
      ;
  }
  
}


// version
// $Id: wrap_ConstantQEKernel.cc 601 2010-10-03 19:55:29Z linjiao $

// End of file 
