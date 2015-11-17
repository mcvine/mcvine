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
#include "mcni/math/number.h"
#include "mccomponents/math/random.h"
#include "mccomponents/math/random/geometry.h"
#include "mccomponents/kernels/sample/ConstantEnergyTransferKernel.h"
#include "mccomponents/exception.h"


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
  double absorption_coefficient,
  double scattering_coefficient)
  : m_E(E),
    m_absorption_coefficient( absorption_coefficient ),
    m_scattering_coefficient( scattering_coefficient ),
    m_details( new Details )
{}


double
mccomponents::kernels::ConstantEnergyTransferKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  float_t v = ev.state.velocity.length();
  return m_absorption_coefficient * (2200/v);
}


double
mccomponents::kernels::ConstantEnergyTransferKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  // !!!!!!!!!!!!!!!!
  // we need better implementation here
  return m_scattering_coefficient;
}


void
mccomponents::kernels::ConstantEnergyTransferKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::ConstantEnergyTransferKernel::S
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
  if (Ef<0) {
    // no scattering can happen
    ev.probability = -1;
    return;
  }
  //std::cout << "E=" << m_E << ", Ei=" << Ei << ", Ef=" << Ef << std::endl;
  // final velocity magnitude
  double vf = conversion::E2v( Ef );

  // pick direction
  typedef mcni::Vector3<double> V3d;
  V3d dir_f;
  math::choose_direction(dir_f); dir_f.normalize();

  // adjust probability of neutron event
  // ev.probability *= 1;

  // adjust velocity
  state.velocity = dir_f * vf;
}


// version
// $Id$

// End of file 
