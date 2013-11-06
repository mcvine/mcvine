// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <cmath>
#include "mccomponents/kernels/sample/SQkernel.h"
#include "mccomponents/kernels/sample/AbstractSQ.h"
#include "mccomponents/exception.h"
#include "mccomponents/math/random.h"
#include "mccomponents/physics/constants.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::SQkernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
};


#ifdef DEBUG
const char mccomponents::kernels::SQkernel::Details::jrnltag[] = "SQkernel";
#endif


mccomponents::kernels::SQkernel::SQkernel
( double absorption_coefficient,
  double scattering_coefficient,
  const sample::AbstractSQ & sq, 
  double Qmin, double Qmax)
  : m_absorption_coefficient( absorption_coefficient ),
    m_scattering_coefficient( scattering_coefficient ),
    m_epsilon(1.e-10),
    m_Qmin(Qmin), m_Qmax(Qmax), m_DQ(Qmax-Qmin),
    m_sq(sq),
    m_details( new Details )
{}


double
mccomponents::kernels::SQkernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  return m_absorption_coefficient * (2200/v);
}


double
mccomponents::kernels::SQkernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  return m_scattering_coefficient;
}


void
mccomponents::kernels::SQkernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::SQkernel::S
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
  double Ei = conversion::v2E( vi ), ki = conversion::v2k * vi;

  // final energy, wave vector
  double Ef = Ei;
  double kf = ki;

  // randomly pick momentum transfer
  // Q must satisfy 0<Q<2ki and Qmin<Q<Qmax
  double Qmin = std::max(m_Qmin, 0.),
    Qmax = std::min(m_Qmax, ki+kf);
  if (Qmax<Qmin) return; // no scatter
  double Q = math::random(Qmin, Qmax);
#ifdef DEBUG
  m_details->debug 
    << journal::at(__HERE__)
    << "generate Q between " << Qmin << " and " << Qmax 
    << ", Q=" << Q
    << journal::endl;
#endif

  // adjust probability of neutron event
  // !!!!!!!!!
  // need normalization factor here
  ev.probability *= m_sq(Q);

  // figure out the direction of the out-going neutron
  double cost = (kf*kf + ki*ki - Q*Q)/2/kf/ki;

  double sint = sqrt(1-cost*cost);

  double phi = math::random(0., 2 * physics::pi);

  double cosp = cos(phi), sinp = sin(phi);

  V3d e1 = ev.state.velocity; e1.normalize();

  // if e1 is not in z-direction
  // we set e2 to be the cross product of e1 and (0,0,1)
  // if e1 is right on the z-direction, that means e1 = (0,0,1)
  // and we set e2 = (1,0,0) or whatever
  V3d e2;
  if (std::abs(e1.x)>m_epsilon || std::abs(e1.y)>m_epsilon) { 
    e2 = V3d(0,0,1) * e1; e2.normalize();
  } else {
    e2 = V3d(1,0,0);
  }

  V3d e3 = e1 * e2;

  V3d ekf = e1*cost + e2*sint*cosp + e3 *sint*sinp;
  
#ifdef DEBUG
  m_details->debug 
    << journal::at(__HERE__)
    << "e1 = " << e1 << journal::newline
    << "e2 = " << e2 << journal::newline
    << "e3 = " << e3 << journal::newline
    << "ekf = " << ekf << journal::newline
    << journal::endl;
#endif
  ev.state.velocity = ekf * (kf*conversion::k2v);
}



// version
// $Id$

// End of file 
