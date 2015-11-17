// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2014  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <cmath>
#include "mccomponents/kernels/sample/ConstantvQEKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mcni/neutron/units_conversion.h"
#include "mccomponents/math/random.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::ConstantvQEKernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
};


#ifdef DEBUG
const char mccomponents::kernels::ConstantvQEKernel::Details::jrnltag[] = "ConstantvQEKernel";
#endif


mccomponents::kernels::ConstantvQEKernel::ConstantvQEKernel
( double Qx, double Qy, double Qz, double E, double dE,
  double absorption_coefficient,
  double scattering_coefficient)
  : m_Q(Qx, Qy, Qz), m_E(E), m_dE(dE),
    m_absorption_coefficient( absorption_coefficient ),
    m_scattering_coefficient( scattering_coefficient ),
    m_details( new Details )
{}


double
mccomponents::kernels::ConstantvQEKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  return m_absorption_coefficient * (2200/v);
}


double
mccomponents::kernels::ConstantvQEKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  return m_scattering_coefficient;
}


void
mccomponents::kernels::ConstantvQEKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::ConstantvQEKernel::S
( mcni::Neutron::Event & ev )
{
  namespace conversion = mcni::neutron_units_conversion;

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity
  double vi = state.velocity.length();
  // incident neutron energy
  double Ei = conversion::v2E( vi );
  // incident neutron mommentum
  Q_t ki = state.velocity * conversion::v2k;
  // output neutron momentum
  Q_t kf = ki - m_Q;
  // output neutron velocity
  state.velocity = kf * conversion::k2v;
  // final energy
  double Ef = conversion::v2E(state.velocity.length());
  // energy transfer
  double E = Ei - Ef;
  // 
  double dE = E-m_E, t = dE/m_dE;
  
  // adjust probability of neutron event
  ev.probability *= std::exp(-t*t/2);
}


// version
// $Id$

// End of file 
