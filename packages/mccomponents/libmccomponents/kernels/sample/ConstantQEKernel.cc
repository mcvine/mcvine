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
};


#ifdef DEBUG
const char mccomponents::kernels::ConstantQEKernel::Details::jrnltag[] = "ConstantQEKernel";
#endif


mccomponents::kernels::ConstantQEKernel::ConstantQEKernel
( double Q, double E, 
  double absorption_cross_section,
  double scattering_cross_section)
  : m_Q(Q), m_E(E),
    m_absorption_cross_section( absorption_cross_section ),
    m_scattering_cross_section( scattering_cross_section ),
    m_details( new Details )
{}


double
mccomponents::kernels::ConstantQEKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_absorption_cross_section;
}


double
mccomponents::kernels::ConstantQEKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_scattering_cross_section;
}


void
mccomponents::kernels::ConstantQEKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::ConstantQEKernel::scatter
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
  
  // adjust probability of neutron event
  // ev.probability *= 1.;
  
  typedef mcni::Vector3<double> V3d;
  V3d vfv(vx,vy,vz);
  state.velocity = vfv;
}


// version
// $Id$

// End of file 
