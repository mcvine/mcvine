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
    
  float_t evaluate(float_t Ef) const {
    // ki is constant
    float_t kf = mcni::neutron_units_conversion::E2k(Ef);
    float_t Q2 = ki*ki + kf*kf - 2*ki*kf*cos_t;
    float_t Q = std::sqrt(Q2);
    return E_Q(Q) - (Ei-Ef);
  }
    
  float_t ki, Ei;
  float_t cos_t;
  E_Q_functor_t &E_Q;  
};


#endif
