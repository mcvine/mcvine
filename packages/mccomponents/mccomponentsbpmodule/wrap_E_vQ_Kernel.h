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


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/E_vQ_Kernel.h"
#include "mccomponents/math/Fxyz_fromExpr.h"


namespace wrap_mccomponents {

  struct Wrap_E_vQ_Kernel{

    typedef mccomponents::math::Fxyz_fromExpr fxyz_t;
    typedef mccomponents::kernels::E_vQ_Kernel<fxyz_t, fxyz_t> \
    kernel_t;

    static kernel_t * newKernel
    (const std::string & E_vQ,
     const std::string & S_vQ,
     double Emax,
     double absorption_cross_section, 
     double scattering_cross_section
     );

    Wrap_E_vQ_Kernel();

  };

}


// version
// $Id$

// End of file 
