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
#include "mccomponents/kernels/sample/Broadened_E_Q_Kernel.h"
#include "mccomponents/math/Fx_fromExpr.h"


namespace wrap_mccomponents {

  struct Wrap_Broadened_E_Q_Kernel{

    typedef mccomponents::math::Fx_fromExpr fx_t;
    typedef mccomponents::kernels::Broadened_E_Q_Kernel<fx_t, fx_t, fx_t> \
    kernel_t;

    static kernel_t * newKernel
    (const std::string & E_Q,
     const std::string & S_Q,
     const std::string & sigma_Q,
     double Qmin, double Qmax,
     double absorption_cross_section, 
     double scattering_cross_section
     );

    Wrap_Broadened_E_Q_Kernel();

  };

}


// version
// $Id$

// End of file 
