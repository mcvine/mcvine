// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <cmath>
#include "mccomponents/kernels/sample/SQE_EnergyFocusing_Kernel.h"
#include "mccomponents/kernels/sample/AbstractSQE.h"
#include "mccomponents/exception.h"
#include "mccomponents/math/random.h"
#include "mccomponents/physics/constants.h"

// #define DEBUG
#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::SQE_EnergyFocusing_Kernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
};


#ifdef DEBUG
const char mccomponents::kernels::SQE_EnergyFocusing_Kernel::Details::jrnltag[] = "SQE_EnergyFocusing_Kernel";
#endif


mccomponents::kernels::SQE_EnergyFocusing_Kernel::SQE_EnergyFocusing_Kernel
( double absorption_cross_section,
  double scattering_cross_section,
  double unitcell_vol,
  sample::AbstractSQE & sqe, 
  double Qmin, double Qmax,
  double Emin, double Emax,
  double Ef, double dEf
  )
  : m_absorption_cross_section( absorption_cross_section ),
    m_scattering_cross_section( scattering_cross_section ),
    m_uc_vol(unitcell_vol),
    m_epsilon(1.e-10),
    m_Qmin(Qmin), m_Qmax(Qmax), m_DQ(Qmax-Qmin),
    m_Emin(Emin), m_Emax(Emax), m_DE(Emax-Emin),
    m_Ef(Ef), m_dEf(dEf),
    m_sqe(sqe),
    m_details( new Details )
{
  // std::cout << "E range" << m_Emin << ", " << m_Emax << std::endl;
}


double
mccomponents::kernels::SQE_EnergyFocusing_Kernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  float_t ret = m_absorption_cross_section/m_uc_vol * (2200/v);
  return ret;
}


double
mccomponents::kernels::SQE_EnergyFocusing_Kernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_scattering_cross_section/m_uc_vol;
}


void
mccomponents::kernels::SQE_EnergyFocusing_Kernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::SQE_EnergyFocusing_Kernel::S
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

  // energy transfer limits due to energy focusing
  double Emin1 = Ei - (m_Ef+m_dEf), Emax1 = Ei - (m_Ef-m_dEf);
  // randomly pick energy transfer
  double E;
  if (m_Emin > Ei) return; // if Ei is too small, won't scatter. nothing happen
  double Emin = std::max(m_Emin, Emin1), Emax = std::min(Emax1, std::min(Ei, m_Emax));
  E = math::random( Emin, Emax );
#ifdef DEBUG
  m_details->debug
    << journal::at(__HERE__)
    << "Original probability" << ev.probability << journal::newline
    << "generate E between " << m_Emin << " and " << std::min(Ei, m_Emax)
    << ", E=" << E
    << journal::endl;
#endif

  // final energy, wave vector
  double Ef = Ei - E;
  double kf = conversion::E2k(Ef);

  // randomly pick momentum transfer
  // Q must satisfy abs(ki-kf)<Q<ki+kf and Qmin<Q<Qmax
  double Qmin = std::max(m_Qmin, std::abs(ki-kf)),
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
  double prob_mul = m_sqe(Q,E) * Q * (Qmax-Qmin) * (Emax-Emin) / (2*ki*ki);
  ev.probability *= prob_mul;
#ifdef DEBUG
  m_details->debug
    << journal::at(__HERE__)
    << "Q, E="<< Q << ", " << E << ", " << journal::endl
    << "Qmin, Qmax=" << Qmin << ", " << Qmax << ", " << journal::endl
    << "Emin, Emax=" << Emin << ", " << Emax << ", " << journal::endl
    << "ki=" << ki << ", " << journal::endl
    << "S=" << m_sqe(Q,E) << journal::endl
    << "prob mul=" << prob_mul << journal::endl
    << journal::endl;
#endif
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
    << "prob = " << ev.probability << journal::newline
    << journal::endl;
#endif
  ev.state.velocity = ekf * (kf*conversion::k2v);
}

// End of file
