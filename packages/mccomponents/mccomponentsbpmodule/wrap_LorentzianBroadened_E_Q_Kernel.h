// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/LorentzianBroadened_E_Q_Kernel.h"
#include "mccomponents/math/Fx_fromExpr.h"

namespace wrap_mccomponents {

  struct Wrap_LorentzianBroadened_E_Q_Kernel{

    typedef mccomponents::math::Fx_fromExpr fx_t;
    typedef mccomponents::kernels::LorentzianBroadened_E_Q_Kernel<fx_t, fx_t, fx_t> \
    kernel_t;

    static kernel_t * newKernel
    (const char * E_Q,
     const char * S_Q,
     const char * gamma_Q,
     double Qmin, double Qmax,
     double absorption_cross_section,
     double scattering_cross_section
     );

    Wrap_LorentzianBroadened_E_Q_Kernel();

  };

}

// End of file
