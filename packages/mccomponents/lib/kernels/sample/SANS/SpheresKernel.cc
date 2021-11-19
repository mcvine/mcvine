// -*- C++ -*-
//
//


#include <cmath>
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mccomponents/math/random.h"
#include "mccomponents/physics/constants.h"
#include "mccomponents/math/random/geometry.h"
#include "mccomponents/kernels/sample/SANS/SpheresKernel.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::SANSSpheresKernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
};


#ifdef DEBUG
const char mccomponents::kernels::SANSSpheresKernel::Details::jrnltag[] = "SANSSpheresKernel";
#endif


mccomponents::kernels::SANSSpheresKernel::SANSSpheresKernel
( float_t absorption_coefficient,
  float_t R, // AA
  float_t phi,
  float_t delta_rho, // fm/AA^3
  float_t max_angle // deg
  )
  : m_absorption_coefficient( absorption_coefficient ),
    m_R(R), m_phi(phi), m_delta_rho(delta_rho),
    m_max_angle(max_angle/180.*mcni::PI),
    m_target_radius(std::tan(m_max_angle)),
    m_details( new Details )
{}


double
mccomponents::kernels::SANSSpheresKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  return m_absorption_coefficient * (2200/v);
}


double
mccomponents::kernels::SANSSpheresKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  namespace conversion = mcni::neutron_units_conversion;
  float_t v = ev.state.velocity.length();
  float_t wl = 2*mcni::PI/(conversion::v2k*v);
  return 3./2*m_phi*m_delta_rho*m_delta_rho*wl*wl*m_R;
}

void
mccomponents::kernels::SANSSpheresKernel::absorb
( mcni::Neutron::Event & ev )
{
}

void
mccomponents::kernels::SANSSpheresKernel::S
( mcni::Neutron::Event & ev )
{
  typedef mcni::Neutron::State::position_t position_t;
  typedef mcni::Neutron::State::velocity_t velocity_t;

  namespace conversion = mcni::neutron_units_conversion;

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity, energy
  double vi = state.velocity.length();
  double Ei = conversion::v2E( vi ), ki = conversion::v2k * vi;
  K_t vec_ki = ki * conversion::v2k;

  // choose direction
  K_t vec_kf;
  math::choose_direction(vec_kf, vec_ki, m_target_radius*ki);
  K_t Q = vec_ki - vec_kf;
  double q = Q.length();
  ev.state.velocity = vec_kf * conversion::k2v;
  double qR = q*m_R;
  double f = 3*(std::sin(qR) - qR*std::cos(qR))/qR/qR/qR;
  ev.probability *= 2./9/mcni::PI*m_R*m_R*ki*ki*f*f;
}

// End of file
