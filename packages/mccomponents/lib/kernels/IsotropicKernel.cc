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
#include "mccomponents/kernels/IsotropicKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mccomponents/math/random.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::IsotropicKernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
};


#ifdef DEBUG
const char mccomponents::kernels::IsotropicKernel::Details::jrnltag[] = "IsotropicKernel";
#endif


mccomponents::kernels::IsotropicKernel::IsotropicKernel
( double absorption_cross_section,
  double scattering_cross_section)
  : m_absorption_cross_section( absorption_cross_section ),
    m_scattering_cross_section( scattering_cross_section ),
    m_details( new Details )
{}


double
mccomponents::kernels::IsotropicKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  float_t rt = m_absorption_cross_section * (2200/v);
  // std::cout << "absorption: " << rt << std::endl;
  return rt;
}


double
mccomponents::kernels::IsotropicKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  // std::cout << "scattering: " << m_scattering_cross_section << std::endl;
  return m_scattering_cross_section;
}


void
mccomponents::kernels::IsotropicKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::IsotropicKernel::S
( mcni::Neutron::Event & ev )
{
#ifdef DEBUG
  m_details->debug << "in" << ev << journal::endl;
#endif

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity
  double vi = state.velocity.length();

  // theta, phi
  double theta = math::random(0., mcni::PI);
  double phi = math::random(0., mcni::PI*2);

#ifdef DEBUG
  m_details->debug
    << "theta: " << theta << ", "
    << "phi: " << phi << ", "
    << journal::endl;
#endif

  // scattered neutron velocity vector
  double vx = vi*sin(theta)*cos(phi);
  double vy = vi*sin(theta)*sin(phi);
  double vz = vi*cos(theta);

  // adjust probability of neutron event
  // normalization factor is 2pi*pi/4pi = pi/2
  ev.probability *= sin(theta) * (mcni::PI/2);

  typedef mcni::Vector3<double> V3d;
  V3d vf(vx,vy,vz);
  state.velocity = vf;
  
#ifdef DEBUG
  m_details->debug
    << "out" << ev
    << journal::endl;
#endif

}


// version
// $Id$

// End of file 
