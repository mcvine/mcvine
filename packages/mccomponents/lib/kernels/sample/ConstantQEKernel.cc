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


#include <cmath>
#include "mccomponents/kernels/sample/ConstantQEKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mccomponents/math/random.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::ConstantQEKernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
  
  // data
  const static double m_epsilon;
};


#ifdef DEBUG
const char mccomponents::kernels::ConstantQEKernel::Details::jrnltag[] = "ConstantQEKernel";
#endif

const double mccomponents::kernels::ConstantQEKernel::Details::m_epsilon = 1e-1;


mccomponents::kernels::ConstantQEKernel::ConstantQEKernel
( double Q, double E, 
  double absorption_coefficient,
  double scattering_coefficient)
  : m_Q(Q), m_E(E),
    m_absorption_coefficient( absorption_coefficient ),
    m_scattering_coefficient( scattering_coefficient ),
    m_details( new Details )
{}


double
mccomponents::kernels::ConstantQEKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  return m_absorption_coefficient * (2200/v);
}


double
mccomponents::kernels::ConstantQEKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  return m_scattering_coefficient;
}


void
mccomponents::kernels::ConstantQEKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::ConstantQEKernel::S
( mcni::Neutron::Event & ev )
{
  namespace conversion = mcni::neutron_units_conversion;

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity
  double vi = state.velocity.length();
  // incident neutron energy
  double Ei = conversion::v2E( vi );
  // final energy
  double Ef = Ei-m_E;
  //std::cout << "E=" << m_E << ", Ei=" << Ei << ", Ef=" << Ef << std::endl;
  // final velocity magnitude
  double vf = conversion::E2v( Ef );
  
  // theta, phi
  double ki = conversion::v2k* vi;
  double kf = conversion::v2k* vf;
  double cost = (ki*ki+kf*kf-m_Q*m_Q)/(2*ki*kf);
  double sint = std::sqrt(1-cost*cost);
  // 
  double phi = math::random(0., mcni::PI*2);
  
  // scattered neutron velocity vector
  double vx = vf*sint*cos(phi);
  double vy = vf*sint*sin(phi);
  double vz = vf*cost;
  
  typedef mcni::Vector3<double> V3d;
  V3d ez = state.velocity; ez.normalize();
  // if e1 is not in z-direction
  // we set e2 to be the cross product of e1 and (0,0,1)
  // if e1 is right on the z-direction, that means e1 = (0,0,1)
  // and we set e2 = (1,0,0) or whatever
  V3d ex;
  if (std::abs(ez.x)>m_details->m_epsilon || std::abs(ez.y)>m_details->m_epsilon) { 
    ex = V3d(0,0,1) * ez; ex.normalize();
  } else {
    ex = V3d(1,0,0) * ez; ex.normalize();
  }
  V3d ey = ez * ex;
  // == v_f ==
  V3d v_f = vx*ex + vy*ey + vz*ez;

  // adjust probability of neutron event
  // ev.probability *= 1.;
  state.velocity = v_f;
}


// version
// $Id$

// End of file 
