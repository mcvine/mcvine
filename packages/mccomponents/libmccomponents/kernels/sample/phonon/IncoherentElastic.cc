// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2008 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <portinfo>
#include <cassert>
#include "journal/warning.h"
#include "mccomponents/math/random.h"


#ifdef DEEPDEBUG
#define __DEBUG__PHNN__INCOHELAST__
#endif

#ifdef DEBUG
#define __DEBUG__PHNN__INCOHELAST__
#endif

#ifdef __DEBUG__PHNN__INCOHELAST__
#include "journal/debug.h"
#endif

#include "mccomponents/physics/constants.h"
#include "mccomponents/kernels/sample/phonon/IncoherentElastic.h"
#include "mccomponents/kernels/sample/phonon/utils.h"
// #include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"


// all methods that are only to help implementation are in class "Details"
struct mccomponents::kernels::phonon::IncoherentElastic::Details {

#ifdef __DEBUG__PHNN__INCOHELAST__
  const static char jrnltag[];
  journal::debug_t debug;
  Details() : debug( jrnltag ) {}
#endif

};


#ifdef __DEBUG__PHNN__INCOHELAST__
const char * mccomponents::kernels::phonon::IncoherentElastic::
Details::jrnltag 
= "phonon_incoherent_elastic_kernel";
#endif


mccomponents::kernels::phonon::IncoherentElastic::
IncoherentElastic
( const atoms_t &atoms,
  float_t unitcell_vol,
  float_t dw_core
  )
  : m_atoms( atoms ),
    m_uc_vol( unitcell_vol ),
    m_dw_core( dw_core ),
    m_details( new Details )
{
  // calculate the total scattering cross section
  m_total_scattering_xs = 0;
  for (size_t i=0; i<m_atoms.size(); i++) {
    m_total_scattering_xs += m_atoms[i].incoherent_cross_section + m_atoms[i].coherent_cross_section;
  }
}


void
mccomponents::kernels::phonon::IncoherentElastic::absorb
( neutron_t & ev )
{
}


mccomponents::kernels::phonon::IncoherentElastic::float_t
mccomponents::kernels::phonon::IncoherentElastic::absorption_coefficient
( const neutron_t & ev )
{
  //!!!!!! must reimplement this !!!!
  return scattering_coefficient( ev );
}


mccomponents::kernels::phonon::IncoherentElastic::float_t
mccomponents::kernels::phonon::IncoherentElastic::scattering_coefficient
( const neutron_t & ev )
{
  float_t ret = m_total_scattering_xs/m_uc_vol;
  // convert to m**-1
  return ret * 1.e2;
}


void
mccomponents::kernels::phonon::IncoherentElastic::scatter
( neutron_t & ev ) 
{
#ifdef DEBUG
  m_details->debug << "in" << ev << journal::endl;
#endif

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity
  double vi = state.velocity.length();

  // theta, phi
  double theta = math::random(0, mcni::PI);
  double phi = math::random(0, mcni::PI*2);

  // Q 
  namespace conversion = mcni::neutron_units_conversion;
  double Q = conversion::v2k*vi * 2 * sin(theta/2.);
  // Debye Waller factor
  double dw = exp(-m_dw_core*Q*Q);

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
  ev.probability *= sin(theta) * (mcni::PI/2) * dw;

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
// $Id: IncoherentElastic.cc 603 2010-10-04 15:58:16Z linjiao $

// End of file 

