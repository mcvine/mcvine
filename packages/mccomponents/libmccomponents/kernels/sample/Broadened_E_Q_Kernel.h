// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2011  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


// E(scalar Q) "dispersion" function
// S(Q,E) = S(scalar Q) * gaussian(sigma(Q))(E-Er)
// This is slightly different from E_Q_Kernel, where
// the delta function is replaced by a guassian with a 
// width that is dependent on Q


#ifndef MCCOMPONENTS_KERNELS_BROADENED_E_Q_KERNEL_H
#define MCCOMPONENTS_KERNELS_BROADENED_E_Q_KERNEL_H


#include <memory>
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "AbstractSQ.h"


namespace mccomponents {

  namespace kernels {

    template< typename E_Q_functor_t, 
	      typename S_Q_functor_t,
	      typename Sigma_Q_functor_t>
    class Broadened_E_Q_Kernel : public AbstractScatteringKernel {
    public:
      
      // meta methods
      //! ctor
      //  E_Q: E(Q) function. 
      //  S_Q: S(Q) function. In many cases, identity function should
      //       be good -- see IdentitySQ
      //       The S values should be non-negative, and average to one
      //       for all Qs.
      //  sigma_Q: sigma(Q) function.
      //  Qmin, Qmax: range for Q to simulate
      //  absorption_coefficient: absorption coefficient (1./m)
      //  scattering_coefficient: scattering coefficient (1./m)
      Broadened_E_Q_Kernel
      (const E_Q_functor_t & E_Q, 
       const S_Q_functor_t & S_Q,
       const Sigma_Q_functor_t & sigma_Q,
       double Qmin, double Qmax,
       double absorption_coefficient,
       double scattering_coefficient);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void scatter( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      
      // data
      E_Q_functor_t m_E;
      S_Q_functor_t m_S;
      Sigma_Q_functor_t m_sigma;
      double m_Qmin, m_Qmax;
      double m_absorption_coefficient, m_scattering_coefficient;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class Broadened_E_Q_Kernel
    
  } // kernels::
} // mccomponents::


#include "Broadened_E_Q_Kernel.icc"

#endif // MCCOMPONENTS_KERNELS_BROADENED_E_Q_KERNEL_H

// version
// $Id: Broadened_E_Q_Kernel.h 601 2010-10-03 19:55:29Z linjiao $

// End of file 
