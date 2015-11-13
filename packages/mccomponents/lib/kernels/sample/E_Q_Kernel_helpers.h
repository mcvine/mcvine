// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2010  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//



#ifndef MCCOMPONENTS_KERNELS_E_Q_KERNEL_HELPERS_H
#define MCCOMPONENTS_KERNELS_E_Q_KERNEL_HELPERS_H

#include "mcni/math/number.h"
#include "mccomponents/math/Functor.h"

template< typename E_Q_functor_t>
struct E_q_minus_deltaE: public mccomponents::math::Functor {
    
  typedef double float_t;
    
  E_q_minus_deltaE(E_Q_functor_t &i_E_Q, float_t i_cos_t, float_t i_Ei)
    :
    Ei(i_Ei)
    ,cos_t(i_cos_t)
    ,E_Q(i_E_Q)
  {
    ki = mcni::neutron_units_conversion::E2k(Ei);
  }
    
  float_t evaluate(float_t Q) const {
    // Q**2 - ki**2 - kf**2 + 2*ki*kf*cos(theta)
    // ki is constant
    // kf**2 = 2m/hbar**2 * Ef, where Ef = Ei - E(Q)
    float_t Ef = Ei - E_Q(Q);
    float_t kf = mcni::neutron_units_conversion::E2k(Ef);
    return Q*Q - ki*ki - kf*kf + 2*ki*kf* cos_t;
  }
    
  float_t ki, Ei;
  float_t cos_t;
  E_Q_functor_t &E_Q;  
};


#endif
