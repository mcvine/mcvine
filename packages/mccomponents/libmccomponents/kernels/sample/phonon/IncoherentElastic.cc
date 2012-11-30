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


// #define DEBUG


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

  const static double m_epsilon;
};


#ifdef __DEBUG__PHNN__INCOHELAST__
const char mccomponents::kernels::phonon::IncoherentElastic::
Details::jrnltag []
= "phonon_incoherent_elastic_kernel";
#endif

const double mccomponents::kernels::phonon::IncoherentElastic::
Details::m_epsilon
= 1e-4;


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
  // calculate the total cross sections
  m_total_scattering_xs = 0;
  for (size_t i=0; i<m_atoms.size(); i++) {
    m_total_scattering_xs += m_atoms[i].incoherent_cross_section;
  }

  m_total_absorption_xs = 0;
  for (size_t i=0; i<m_atoms.size(); i++) {
    m_total_absorption_xs += m_atoms[i].absorption_cross_section;
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
  float_t v = ev.state.velocity.length();
  float_t ret = m_total_absorption_xs/m_uc_vol * (2200/v);
  // convert to m**-1
  return ret * 1.e2;
}


mccomponents::kernels::phonon::IncoherentElastic::float_t
mccomponents::kernels::phonon::IncoherentElastic::scattering_coefficient
( const neutron_t & ev )
{
  float_t ret = m_total_scattering_xs/m_uc_vol;
  // std::cout << "scattering_coefficient: " << ret << std::endl;
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
    << "Q: " << Q << ", "
    << "dw core: " << m_dw_core << ", "
    << "dw: " << dw << ", "
    << journal::endl;
#endif

  // scattered neutron velocity vector
  // == coordinate system ==
  V_t e1 = state.velocity; e1.normalize();
  // if e1 is not in z-direction
  // we set e2 to be the cross product of e1 and (0,0,1)
  // if e1 is right on the z-direction, that means e1 = (0,0,1)
  // and we set e2 = (1,0,0) or whatever
  K_t e2;
  if (std::abs(e1.x)>m_details->m_epsilon || std::abs(e1.y)>m_details->m_epsilon) { 
    e2 = V_t(0,0,1) * e1; e2.normalize();
  } else {
    e2 = V_t(1,0,0);
  }
  V_t e3 = e1 * e2;
  // == v_f ==
  V_t v_f = sin(theta)*cos(phi) * e2 
    + sin(theta)*sin(phi) * e3
    + cos(theta) * e1;
  v_f = v_f *  vi; // elastic scattering
  state.velocity = v_f;

  // adjust probability of neutron event
  // normalization factor is 2pi*pi/4pi = pi/2
  ev.probability *= sin(theta) * (mcni::PI/2) * dw;

#ifdef DEBUG
  m_details->debug
    << "out" << ev
    << journal::endl;
#endif

}


// version
// $Id: IncoherentElastic.cc 603 2010-10-04 15:58:16Z linjiao $

// End of file 

