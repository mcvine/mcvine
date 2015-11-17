// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2013  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


// E(vector Q) "dispersion" function
// S(Q,E) = S(vector Q) * delta(E - E(vector Q))
// basic idea is that scattering function is a delta function for energy


#ifndef MCCOMPONENTS_KERNELS_E_VQ_KERNEL_H
#define MCCOMPONENTS_KERNELS_E_VQ_KERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {

  namespace kernels {

    template< typename E_vQ_functor_t, 
	      typename S_vQ_functor_t>
    class E_vQ_Kernel : public KernelBase {
    public:
      
      // meta methods
      //! ctor
      //  E_vQ: E(vQ) function. 
      //  S_vQ: S(vQ) function. In many cases, identity function should
      //       be good 
      //  Emax: maximum energy transfer
      //  absorption_coefficient: absorption coefficient (1./m)
      //  scattering_coefficient: scattering coefficient (1./m)
      E_vQ_Kernel
      (const E_vQ_functor_t & E_vQ, 
       const S_vQ_functor_t & S_vQ,
       double Emax,
       double absorption_coefficient,
       double scattering_coefficient);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      
      // data
      E_vQ_functor_t m_E;
      S_vQ_functor_t m_S;
      double m_Emax;
      double m_absorption_coefficient, m_scattering_coefficient;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class E_vQ_Kernel
    
  } // kernels::
} // mccomponents::


#include "E_vQ_Kernel.icc"

#endif // MCCOMPONENTS_KERNELS_E_VQ_KERNEL_H

// version
// $Id$

// End of file 
