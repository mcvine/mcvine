// -*- C++ -*-
//
//


#include <cmath>
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mccomponents/math/random.h"
#include "mccomponents/math/random/geometry.h"
#include "DGSSXResKernel.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


namespace mccomponents{
  namespace kernels{
    const double ksq2e = mcni::neutron_units_conversion::k2v*mcni::neutron_units_conversion::k2v*mcni::neutron_units_conversion::vsq2e;
  }
}

struct 
mccomponents::kernels::DGSSXResKernel::Details {

  typedef mccomponents::kernels::DGSSXResKernel kernel_t;
    
#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
#endif
  
  Details(kernel_t &i_kernel) 
    :
    kernel(&i_kernel)
#ifdef DEBUG
    ,debug( jrnltag )
#endif
    {}

  kernel_t * kernel;
};


mccomponents::kernels::DGSSXResKernel
::DGSSXResKernel
( const X_t &target_position, float_t target_radius,
  float_t tof_at_target, float_t dtof,
  double absorption_coefficient,
  double scattering_coefficient)
  : m_target_position(target_position),
    m_target_radius(target_radius),
    m_tof_at_target(tof_at_target),
    m_dtof(dtof),
    m_absorption_coefficient( absorption_coefficient ),
    m_scattering_coefficient( scattering_coefficient ),
    m_details( new Details(*this) )
{
}


double
mccomponents::kernels::DGSSXResKernel
::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  return m_absorption_coefficient * (2200/v);
}



double
mccomponents::kernels::DGSSXResKernel
::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  // this is a simplified model
  return m_scattering_coefficient;
}



void
mccomponents::kernels::DGSSXResKernel
::absorb
( mcni::Neutron::Event & ev )
{
}



void
mccomponents::kernels::DGSSXResKernel
::S
( mcni::Neutron::Event & ev )
{
  namespace conversion = mcni::neutron_units_conversion;
  typedef mcni::Vector3<double> V3d;

  // input neutron state
  mcni::Neutron::State & state = ev.state;

  // vector from neutron position to the target
  V3d displacement = m_target_position - state.position;
  // pick direction of scattered neutron
  V3d vf_dir;
  double solid_angle=math::choose_direction
    (vf_dir, displacement, m_target_radius);
  vf_dir.normalize();
  
  // randomly pick tof
  double tof=math::random(m_tof_at_target-m_dtof/2., m_tof_at_target+m_dtof/2.);

  // compute vf length
  double vf = displacement.length()/(tof-ev.time);
  // compute vf vector
  V3d vf_vec = vf_dir * vf;
  // compute final energy
  double Ef = conversion::v2E(vf);

  // compute probability factor
  double dE_over_dt = 2*Ef/tof;
  double prob = solid_angle/4./mcni::PI * m_dtof * dE_over_dt;
  double vf_over_vi = vf/state.velocity.length();

  // set vf
  state.velocity = vf_vec;
  ev.probability *= prob * vf_over_vi;
}

// End of file 
