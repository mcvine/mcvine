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


// #define DEEPDEBUG
// #define DEBUG

#ifdef DEEPDEBUG
#define __DEBUG__PHNN__COHINEL_POLY__
#endif

#ifdef DEBUG
#define __DEBUG__PHNN__COHINEL_POLY__
#endif

#ifdef __DEBUG__PHNN__COHINEL_POLY__
#include "journal/debug.h"
#endif

#include "mccomponents/physics/constants.h"
#include "mccomponents/math/random/geometry.h"
#include "mccomponents/kernels/sample/phonon/IncoherentInelastic.h"
#include "mccomponents/kernels/sample/phonon/utils.h"
#include "mccomponents/kernels/sample/phonon/AbstractDOS.h"
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"
#include "mccomponents/kernels/sample/phonon/scattering_length.h"
#include "mccomponents/kernels/sample/phonon/generateQ.h"


// all methods that are only to help implementation are in class "Details"
struct mccomponents::kernels::phonon::IncoherentInelastic::Details {

  // types
  typedef IncoherentInelastic w_t;

  // global const data
  static const char * jrnltag;

  // meta methods
  Details( w_t & kernel );
  
  // methods
  
  // data
  w_t & kernel;
  const static float_t zero;
  
  /// Ei+omega or Ei-omega?
  float_t
  pick_Ef( float_t &prob_factor, float_t Ei, float_t max_omega) const;
};


const char * mccomponents::kernels::phonon::IncoherentInelastic::
Details::jrnltag 
= "phonon_incoherent_inelastic_kernel";

const
mccomponents::kernels::phonon::IncoherentInelastic::float_t
mccomponents::kernels::phonon::IncoherentInelastic::
Details::zero
= 1e-1;




mccomponents::kernels::phonon::IncoherentInelastic::
Details::Details( w_t & i_kernel )
  : kernel(i_kernel)
{
}


mccomponents::kernels::phonon::IncoherentInelastic::float_t
mccomponents::kernels::phonon::IncoherentInelastic::
Details::pick_Ef
( float_t &prob_factor, float_t Ei, float_t max_omega) const
{
  float_t Ef;
  float_t e_range;

  if (Ei > max_omega) {
    e_range = 2 * max_omega;
    Ef = Ei - max_omega + math::random01() * e_range;
  } else {
    e_range = (Ei + max_omega);
    Ef = math::random01()* e_range;
  }
  prob_factor = e_range;
  return Ef;
}
  
  
mccomponents::kernels::phonon::IncoherentInelastic::
IncoherentInelastic
(const atoms_t &atoms,
 float_t unitcell_vol,
 dos_t & dos,
 dwcalculator_t & dw_calctor,
 float_t temperature
 ) 
  : m_atoms( atoms ),
    m_uc_vol( unitcell_vol ),
    m_dos( &dos ),
    m_DW_calc( &dw_calctor ),
    m_Temperature( temperature ),
    m_max_phonon_energy( dos.emax() ),
    m_details( new Details(*this) )
{
  
#ifdef DEBUG
  journal::debug_t debug(m_details->jrnltag);
  debug << "m_atoms=";
  for (size_t i = 0; i< m_atoms.size(); i++)
    debug  << m_atoms[i] << journal::newline;
  debug << journal::endl;
  
#endif

  // compute average mass
  m_Mass = 0;
  for (size_t i=0; i<m_atoms.size(); i++) {
    m_Mass += m_atoms[i].mass;
  }
  m_Mass /= m_atoms.size();

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
mccomponents::kernels::phonon::IncoherentInelastic::absorb
( neutron_t & ev )
{
}


mccomponents::kernels::phonon::IncoherentInelastic::float_t
mccomponents::kernels::phonon::IncoherentInelastic::absorption_coefficient
( const neutron_t & ev )
{
  float_t v = ev.state.velocity.length();
  float_t ret = m_total_absorption_xs/m_uc_vol * (2200/v);
  // convert to m**-1
  return ret * 1.e2;
}


mccomponents::kernels::phonon::IncoherentInelastic::float_t
mccomponents::kernels::phonon::IncoherentInelastic::scattering_coefficient
( const neutron_t & ev )
{
  float_t ret = m_total_scattering_xs/m_uc_vol;
  // convert to m**-1
  return ret * 1.e2;
}


void
mccomponents::kernels::phonon::IncoherentInelastic::scatter
( neutron_t & ev ) 
{
  namespace conversion = mcni::neutron_units_conversion;

#ifdef DEEPDEBUG
  journal::debug_t debug(m_details->jrnltag);
#endif

  const mcni::Neutron::State  &ns  = ev.state;
  const V_t v_i   = ns.velocity;
  
  // we need to manipulate the neutron probability. get the reference here.
  float_t               &prob = ev.probability; 

  /* initial velocity magnitude */
  float_t v_i_l = v_i.length();
  // initial energy
  float_t E_i = conversion::v2E( v_i_l );

  // = pick a scattering direction =
  V_t dir_f;
  math::choose_direction( dir_f ); dir_f.normalize();
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "picked scattering direction " << dir_f
	<< journal::endl;
#endif

#ifdef DEEPDEBUG1
  //prob*=4pi;
  std::cerr << "don't forget this multiplication factor!" << std::endl;
  throw;
#endif
  
  // = pick the final energy =
  float_t e_range;
  float_t E_f = m_details->pick_Ef( e_range, E_i, m_max_phonon_energy );
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "picked final energy " << E_f
	<< journal::endl;
#endif

  // +/- phonon energy
  float_t  omega = E_i - E_f; 

  // vf
  namespace conversion = mcni::neutron_units_conversion;
  float_t v_f_l = conversion::E2v( E_f );
  V_t v_f = v_f_l * dir_f;
  ev.state.velocity = v_f;
  
  // Q vector
  V_t v_Q = v_i - v_f;
  K_t Q = v_Q * conversion::v2k;
  
  // length of Q
  float_t Q_l = Q.length();

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "* E_i=" << E_i << ","
	<< "E_f=" << E_f << ","
	<< "v_f_l=" << v_f_l << ","
	<< "v_i=" << v_i << ","
	<< "v_f=" << v_f << ","
	<< "v_Q=" << v_Q << ","
	<< "omega =" << omega << ","
	<< "Q =" << Q << ","
	<< journal::endl;
#endif

  // change the velocity of neutron. other things stay put
  ev.state.velocity = v_f;

  // thermal factor
  float_t therm_factor = phonon_bose_factor( omega, m_Temperature );

  // debye waller factor	  
  float_t DW = exp( -m_DW_calc->DW( Q_l ) );
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "debye waller factor " << DW
	<< journal::endl;
#endif

  prob *= e_range; // for picking Ef

  // prob /= m_uc_vol;  // this is now in scattering_coefficient method
  // prob *= m_sigma_inc/m_Mass; // should be \sum{sigma_inc/M} 
  // m_sigma_inc should be in scattering_coefficient method
  prob /= m_Mass;
  prob *= v_f_l/v_i_l;
  prob *= DW;
  prob *= therm_factor;
  prob *= (*m_dos)( std::abs(omega) ); //  *m_dos_norm_factor; this is no longer necessary. dos() method is require to be normalized

  if (std::abs(omega) < m_details->zero*m_max_phonon_energy) 
    prob = 0.0;
  else
    prob *= conversion::k2E(Q_l)/std::abs(omega);

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "* prob = " << prob << ","
	<< "v_f_l/v_i_l=" << v_f_l/v_i_l << ","
	<< "m_Mass=" << m_Mass << ","
	<< "DW=" << DW << ","
	<< "k2E(Q_l)/abs(omega)=" << conversion::k2E(Q_l)/std::abs(omega) << ","
	<< "m_dos( abs(omega) )=" << (*m_dos)( std::abs(omega) ) << ","
	<< "therm_factor=" << therm_factor << ","
	<< journal::endl;
#endif


#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "*** prob = " << prob << ", "
	<< "Q=" << Q_l << ", "
	<< "omega=" << omega << ", "
	<< journal::endl;
#endif
}


// version
// $Id: IncoherentInelastic.cc 603 2010-10-04 15:58:16Z linjiao $

// End of file 

