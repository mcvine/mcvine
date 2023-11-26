// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//



#include <boost/python.hpp>

#include "wrap_LorentzianBroadened_E_Q_Kernel.h"


namespace wrap_mccomponents {

  Wrap_LorentzianBroadened_E_Q_Kernel::kernel_t *
  Wrap_LorentzianBroadened_E_Q_Kernel::newKernel
  (const char * E_Q,
   const char * S_Q,
   const char * gamma_Q,
   double Qmin, double Qmax,
   double absorption_cross_section,
   double scattering_cross_section
   )
  {
    return new kernel_t
      (fx_t(E_Q, "Q"),
       fx_t(S_Q, "Q"),
       fx_t(gamma_Q, "Q"),
       Qmin, Qmax,
       absorption_cross_section,
       scattering_cross_section
       );
  }

  Wrap_LorentzianBroadened_E_Q_Kernel::Wrap_LorentzianBroadened_E_Q_Kernel()
  {
    using namespace boost::python;

    def("create_LorentzianBroadened_E_Q_Kernel",
        &newKernel,
        return_value_policy<manage_new_object>()
        );

    class_
      <kernel_t,
       bases<mccomponents::AbstractScatteringKernel>,
       boost::noncopyable>
      ("LorentzianBroadened_E_Q_Kernel", no_init)
      ;
  }
}

// End of file
