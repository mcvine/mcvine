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
// S(Q,E) = S(scalar Q) * delta(E - E(scalar Q))
// basic idea is that scattering function is a delta function


#ifndef MCCOMPONENTS_KERNELS_E_Q_KERNEL_H
#define MCCOMPONENTS_KERNELS_E_Q_KERNEL_H


#include <memory>
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "AbstractSQ.h"


namespace mccomponents {

  namespace kernels {

    template< typename E_Q_functor_t, 
	      typename S_Q_functor_t>
    class E_Q_Kernel : public AbstractScatteringKernel {
    public:
      
      // meta methods
      //! ctor
      //  E_Q: E(Q) function. 
      //  S_Q: S(Q) function. In many cases, identity function should
      //       be good -- see IdentitySQ
      //       The S values should be non-negative, and average to one
      //       for all Qs.
      //  Qmin, Qmax: range for Q to simulate
      //  absorption_coefficient: absorption coefficient (1./m)
      //  scattering_coefficient: scattering coefficient (1./m)
      E_Q_Kernel
      (const E_Q_functor_t & E_Q, 
       const S_Q_functor_t & S_Q,
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
      double m_Qmin, m_Qmax;
      double m_absorption_coefficient, m_scattering_coefficient;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class E_Q_Kernel
    
  } // kernels::
} // mccomponents::


#include "E_Q_Kernel.icc"

#endif // MCCOMPONENTS_KERNELS_E_Q_KERNEL_H

// version
// $Id: E_Q_Kernel.h 601 2010-10-03 19:55:29Z linjiao $

// End of file 
