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


//#include <portinfo>
#include <cassert>


// #define DEEPDEBUG
// #define DEBUG

#ifdef DEEPDEBUG
#define __DEBUG__PHNN__COHINEL_POLY__
#endif

#ifdef DEBUG
#define __DEBUG__PHNN__COHINEL_POLY__
#endif


#include "mcni/math/func.h"
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

  /// get mass and cross sections
  void
  get_mass_and_xs
  (const atoms_t &atoms, float_t &mass, 
   float_t &scattering_xs, float_t &absorption_xs);
};


const char * mccomponents::kernels::phonon::IncoherentInelastic::
Details::jrnltag 
= "phonon_incoherent_inelastic_kernel";

const
mccomponents::kernels::phonon::IncoherentInelastic::float_t
mccomponents::kernels::phonon::IncoherentInelastic::
Details::zero
= 1e-2;




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
  
  
void
mccomponents::kernels::phonon::IncoherentInelastic::
Details::get_mass_and_xs
(const atoms_t &atoms, float_t &mass, 
 float_t &scattering_xs, float_t &absorption_xs)
{
  
  mass = 0;
  scattering_xs = 0;
  absorption_xs = 0;
  
  for (size_t i=0; i<atoms.size(); i++) {
    mass += atoms[i].mass;
    scattering_xs += atoms[i].incoherent_cross_section;
    absorption_xs += atoms[i].absorption_cross_section;
  }
  mass /= atoms.size(); // average
}



mccomponents::kernels::phonon::IncoherentInelastic::
IncoherentInelastic
(const atoms_t &atoms,
 float_t unitcell_vol,
 dos_t & dos,
 dwcalculator_t & dw_calctor,
 float_t temperature,
 float_t ave_mass, 
 float_t scattering_xs, float_t absorption_xs
 ) 
  : m_atoms( atoms ),
    m_uc_vol( unitcell_vol ),
    m_dos( &dos ),
    m_DW_calc( &dw_calctor ),
    m_Temperature( temperature ),
    m_max_phonon_energy( dos.emax() ),
    m_details( new Details(*this) )
{
  m_details->get_mass_and_xs
    (m_atoms, m_Mass, m_total_scattering_xs, m_total_absorption_xs);
  // 
  if (ave_mass > 0.)
    m_Mass = ave_mass;
  if (scattering_xs > 0.)
    m_total_scattering_xs = scattering_xs;
  if (absorption_xs > 0.)
    m_total_absorption_xs = absorption_xs;
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
mccomponents::kernels::phonon::IncoherentInelastic::S
( neutron_t & ev ) 
{
  namespace conversion = mcni::neutron_units_conversion;


  const mcni::Neutron::State  &ns  = ev.state;
  const V_t v_i   = ns.velocity;
  
  // we need to manipulate the neutron probability. get the reference here.
  float_t &prob = ev.probability; 

  /* initial velocity magnitude */
  float_t v_i_l = v_i.length();
  // initial energy
  float_t E_i = conversion::v2E( v_i_l );

  // = pick a scattering direction =
  V_t dir_f;
  math::choose_direction( dir_f ); dir_f.normalize();

#ifdef DEEPDEBUG1
  //prob*=4pi;
  std::cerr << "don't forget this multiplication factor!" << std::endl;
  throw;
#endif
  
  // = pick the final energy =
  float_t e_range;
  float_t E_f = m_details->pick_Ef( e_range, E_i, m_max_phonon_energy );

  // +/- phonon energy
  float_t  omega = E_i - E_f; 

  // avoid divide by zero
  bool small_omega = std::abs(omega) < m_details->zero*m_max_phonon_energy;
  
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


  // change the velocity of neutron. other things stay put
  ev.state.velocity = v_f;

  // thermal factor
  float_t therm_factor = phonon_bose_factor( omega, m_Temperature );
  float_t beta = 1./(m_Temperature * physics::Kelvin2meV);

  // debye waller factor	  
  float_t DW = exp( -m_DW_calc->DW( Q_l ) );

  prob *= e_range; // for picking Ef

  // prob /= m_uc_vol;  // this is now in scattering_coefficient method
  // prob *= m_sigma_inc/m_Mass; // should be \sum{sigma_inc/M} 
  // m_sigma_inc should be in scattering_coefficient method
  prob /= m_Mass;
  prob *= v_f_l/v_i_l;
  prob *= DW;
  if (small_omega) {
    // with omega --> 0
    // therm_factor --> 1/(beta E)
    // dos --> sod * E**2
    prob *= m_dos->sod() / beta * conversion::k2E(Q_l);
  } else {
    prob *= therm_factor;
    prob *= (*m_dos)( std::abs(omega) ); //  *m_dos_norm_factor; this is no longer necessary. dos() method is require to be normalized
    prob *= conversion::k2E(Q_l)/std::abs(omega);
  }

  if (prob != prob) {
    std::cerr 
      << "* prob = " << prob << ","
      << "small_omega = " << small_omega << ", "
      << "dos sod = " << m_dos->sod() << ", "
      << "beta = " << beta << ", "
      << "energy of Q in meV" << conversion::k2E(Q_l) << ", "
      << "e_range = " << e_range << ", "
      << "v_f_l/v_i_l=" << v_f_l/v_i_l << ","
      << "m_Mass=" << m_Mass << ","
      << "DW=" << DW << ","
      << "k2E(Q_l)/abs(omega)=" << conversion::k2E(Q_l)/std::abs(omega) << ","
      << "m_dos( abs(omega) )=" << (*m_dos)( std::abs(omega) ) << ","
      << "therm_factor=" << therm_factor << ","
      << "Q=" << Q_l << ", "
      << "omega=" << omega << ", "
      << std::endl;
    throw;
  }
}


// version
// $Id: IncoherentInelastic.cc 603 2010-10-04 15:58:16Z linjiao $

// End of file 

