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
#include "mccomponents/kernels/sample/ConstantEnergyTransferKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mccomponents/math/random.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif


struct mccomponents::kernels::ConstantEnergyTransferKernel::Details {

#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif
};


#ifdef DEBUG
const char mccomponents::kernels::ConstantEnergyTransferKernel::Details::jrnltag[] = "ConstantEnergyTransferKernel";
#endif


mccomponents::kernels::ConstantEnergyTransferKernel::ConstantEnergyTransferKernel
( double E, 
  double absorption_cross_section,
  double scattering_cross_section)
  : m_E(E),
    m_absorption_cross_section( absorption_cross_section ),
    m_scattering_cross_section( scattering_cross_section ),
    m_details( new Details )
{}


double
mccomponents::kernels::ConstantEnergyTransferKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_absorption_cross_section;
}


double
mccomponents::kernels::ConstantEnergyTransferKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_scattering_cross_section;
}


void
mccomponents::kernels::ConstantEnergyTransferKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::ConstantEnergyTransferKernel::scatter
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
  double theta = math::random(0, mcni::PI);
  double phi = math::random(0, mcni::PI*2);

  // scattered neutron velocity vector
  double vx = vf*sin(theta)*cos(phi);
  double vy = vf*sin(theta)*sin(phi);
  double vz = vf*cos(theta);

  // adjust probability of neutron event
  // normalization factor is 2pi*pi/4pi = pi/2
  ev.probability *= sin(theta) * (mcni::PI/2);

  typedef mcni::Vector3<double> V3d;
  V3d vfv(vx,vy,vz);
  state.velocity = vfv;
}


// version
// $Id$

// End of file 
