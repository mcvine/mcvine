// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


// E(scalar Q) "dispersion" function
// S(Q,E) = S(scalar Q) * lorentzian(gamma(Q))(E-Er)
// This is slightly different from Broadened_E_Q_Kernel, where
// the gaussian broadening is replaced by lorentzian


#ifndef MCCOMPONENTS_KERNELS_LORENTZIANBROADENED_E_Q_KERNEL_H
#define MCCOMPONENTS_KERNELS_LORENTZIANBROADENED_E_Q_KERNEL_H


#include <memory>
#include "KernelBase.h"
#include "AbstractSQ.h"


namespace mccomponents {

  namespace kernels {

    template< typename E_Q_functor_t,
	      typename S_Q_functor_t,
	      typename Gamma_Q_functor_t>
    class LorentzianBroadened_E_Q_Kernel : public KernelBase {
    public:
      // meta methods
      //! ctor
      //  E_Q: E(Q) function.
      //  S_Q: S(Q) function. In many cases, identity function should
      //       be good -- see IdentitySQ
      //       The S values should be non-negative, and average to one
      //       for all Qs.
      //  gamma_Q: gamma(Q) function.
      //  Qmin, Qmax: range for Q to simulate
      //  absorption_coefficient: absorption coefficient (1./m)
      //  scattering_coefficient: scattering coefficient (1./m)
      LorentzianBroadened_E_Q_Kernel
      (const E_Q_functor_t & E_Q, 
       const S_Q_functor_t & S_Q,
       const Gamma_Q_functor_t & gamma_Q,
       double Qmin, double Qmax,
       double absorption_coefficient,
       double scattering_coefficient);

      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );

    private:

      // data
      E_Q_functor_t m_E;
      S_Q_functor_t m_S;
      Gamma_Q_functor_t m_gamma;
      double m_Qmin, m_Qmax;
      double m_Emin, m_Emax;
      double m_absorption_coefficient, m_scattering_coefficient;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class LorentzianBroadened_E_Q_Kernel

  } // kernels::
} // mccomponents::


#include "LorentzianBroadened_E_Q_Kernel.icc"

#endif // MCCOMPONENTS_KERNELS_LORENTZIANBROADENED_E_Q_KERNEL_H

// End of file
