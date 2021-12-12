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
    m_max_angle_tan(std::tan(m_max_angle)),
    m_solidangle(2*mcni::PI*(1.-std::cos(m_max_angle))), // area of sphere cap
    m_details( new Details )
{
  // std::cout << "solid angle: " << m_solidangle << std::endl;
  // std::cout << "max angle: " << m_max_angle << ", max angle tan" << m_max_angle_tan << std::endl;
}


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
  /*
  std::cout << "wl=" << wl << std::endl;
  std::cout << "sc_coeff" << 3./2*m_phi*m_delta_rho*m_delta_rho*wl*wl*m_R << std::endl;
  */
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
  K_t vec_ki = state.velocity * conversion::v2k;

  // choose direction
  K_t vec_kf;
  math::choose_direction(vec_kf, vec_ki, m_max_angle_tan*ki);
  double prob_factor = m_solidangle/4/mcni::PI;
  K_t Q = vec_ki - vec_kf;
  double q = Q.length();
  ev.state.velocity = vec_kf * conversion::k2v;
  double qR = q*m_R;
  double f = 3*(std::sin(qR) - qR*std::cos(qR))/qR/qR/qR;
  prob_factor *= 2./9/mcni::PI*m_R*m_R*ki*ki*f*f;
  /*
  std::cout << "q=" << q << ", qR=" << qR << std::endl;
  std::cout << "f=" << f << ", ki=" << ki << ", R=" << m_R << std::endl;
  */
  ev.probability *= prob_factor;
}

// End of file
