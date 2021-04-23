// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <cmath>
#include "mccomponents/kernels/sample/SvQkernel.h"
#include "mccomponents/kernels/sample/AbstractSvQ.h"
#include "mccomponents/exception.h"
#include "mccomponents/math/random.h"
#include "mccomponents/physics/constants.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::SvQkernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
};


#ifdef DEBUG
const char mccomponents::kernels::SvQkernel::Details::jrnltag[] = "SvQkernel";
#endif

mccomponents::kernels::SvQkernel::SvQkernel
( double absorption_coefficient,
  double scattering_coefficient,
  sample::AbstractSvQ & sq)
  : m_absorption_coefficient( absorption_coefficient ),
    m_scattering_coefficient( scattering_coefficient ),
    m_epsilon(1.e-10),
    m_sq(sq),
    m_details( new Details )
{}

double
mccomponents::kernels::SvQkernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  return m_absorption_coefficient * (2200/v);
}

double
mccomponents::kernels::SvQkernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  return m_scattering_coefficient;
}

void
mccomponents::kernels::SvQkernel::absorb
( mcni::Neutron::Event & ev )
{
}

void
mccomponents::kernels::SvQkernel::S
( mcni::Neutron::Event & ev )
{
  typedef mcni::Neutron::State::position_t position_t;
  typedef mcni::Neutron::State::velocity_t velocity_t;
  typedef mcni::Vector3<double> V3d;

  namespace conversion = mcni::neutron_units_conversion;

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity, energy
  double vi = state.velocity.length();
  V3d ki = state.velocity * conversion::v2k;

  // randomly pick kf direction
  double costheta = math::random(-1., 1.);
  double _t = 1-costheta*costheta;
  double sintheta;
  if (_t<0) sintheta = 0;
  else sintheta = sqrt(_t);
  double phi = math::random(0., 2*mcni::PI);
  double sinphi = sin(phi), cosphi = cos(phi);
  velocity_t vf(vi*sintheta*cosphi, vi*sintheta*sinphi, vi*costheta);
  V3d kf = vf * conversion::v2k;
  V3d Q = ki-kf;
  ev.probability *= m_sq(Q);
  ev.state.velocity = vf;
}

// End of file
