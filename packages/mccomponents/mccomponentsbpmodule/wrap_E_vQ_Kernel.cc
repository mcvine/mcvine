// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2013 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//



#include <boost/python.hpp>

#include "wrap_E_vQ_Kernel.h"


namespace wrap_mccomponents {

  Wrap_E_vQ_Kernel::kernel_t * 
  Wrap_E_vQ_Kernel::newKernel
  (const std::string & E_vQ,
   const std::string & S_vQ,
   double Emax,
   double absorption_cross_section, 
   double scattering_cross_section
   )
  {
    return new kernel_t
      (fxyz_t(E_vQ, "Qx,Qy,Qz"),
       fxyz_t(S_vQ, "Qx,Qy,Qz"),
       Emax,
       absorption_cross_section,
       scattering_cross_section
       );
  }

  Wrap_E_vQ_Kernel::Wrap_E_vQ_Kernel()
  {
    using namespace boost::python;
    
    def("create_E_vQ_Kernel", 
	&newKernel,
	return_value_policy<manage_new_object>()
	);
    
    class_
      <kernel_t, 
      bases<mccomponents::AbstractScatteringKernel>,
      boost::noncopyable>
      ("E_vQ_Kernel", no_init)
      ;
  }
  
}


// version
// $Id$

// End of file 
