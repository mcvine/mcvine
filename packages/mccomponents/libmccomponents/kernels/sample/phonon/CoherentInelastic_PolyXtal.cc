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
#include "mccomponents/kernels/sample/phonon/CoherentInelastic_PolyXtal.h"
#include "mccomponents/kernels/sample/phonon/utils.h"
#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"
#include "mccomponents/kernels/sample/phonon/scattering_length.h"
#include "mccomponents/kernels/sample/phonon/generateQ.h"


// all methods that are only to help implementation are in class "Details"
struct mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::Details {

  // types
  typedef CoherentInelastic_PolyXtal w_t;

  // global const data
  static const char * jrnltag;

  // meta methods
  Details( w_t & kernel );

  // methods
  /// knowing vi, and vf's length, and vQ's length, decide vf vector
  void pick_v_f
  (float_t & prob, 
   V_t & v_f,
   V_t v_i, float_t v_f_l, float_t v_Q_l) const;

  /// knowing vi's length, having chosen the phonon branch,
  /// choose a Q so that the phonon in the chose branch at Q can scatter 
  /// the incident neutron. This is only good for polycrystal
  void   pick_a_valid_Q_vector
  (K_t &Q, float_t &v_Q_l, float_t &E_f, float_t &v_f_l,
   float_t Qcutoff, float_t E_i, float_t v_i_l, unsigned int branch) const;

  /// calculate relative acceisible reciprocal volumn
  std::vector<float_t> 
  calc_relAccessibleReciVol_MC
  (size_t numMCsteps, const dispersion_t &disp, float_t Qcutoff, float_t E_i) const;


  // data
  w_t & kernel;

private:

  /// Ei+omega or Ei-omega?
  float_t
  pick_Ef( float_t Ei, float_t omega) const;
};


const char * mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::
Details::jrnltag 
= "phonon_coherent_inelastic_polyxtal_kernel";


mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::
Details::Details( w_t & i_kernel )
  : kernel(i_kernel)
{
}


void
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::
Details::pick_v_f
(float_t & prob, 
 V_t & v_f,
 V_t v_i, float_t v_f_l, float_t v_Q_l)
const
{
  namespace conversion = mcni::neutron_units_conversion;

  float_t v_i_l = v_i.length();
#ifdef DEEPDEBUG
  journal::debug_t debug(jrnltag);
  debug << journal::at(__HERE__)
	<< "vi length = " << v_i_l
	<< journal::endl;
#endif

  // == theta ==
  float_t cos_theta = (v_i_l*v_i_l+v_f_l*v_f_l - v_Q_l*v_Q_l)
    /(2*v_i_l*v_f_l);
  float_t cos_theta_sq = cos_theta*cos_theta;
  if (cos_theta_sq>1.) {
    std::cerr << "In file " << __FILE__ << " line " << __LINE__ << "; "
	      << "cos_theta = " << cos_theta << "; "
	      << "which is greater than 1!!!"
	      << std::endl;
    //throw;
    cos_theta_sq = 1.;
  }
  float_t sin_theta = sqrt(1-cos_theta_sq);
  // == phi ==
  float_t phi = math::random(0, 2*physics::pi);

  // == coordinate system ==
  K_t e1 = v_i; e1.normalize();
  // if e1 is not in z-direction
  // we set e2 to be the cross product of e1 and (0,0,1)
  // if e1 is right on the z-direction, that means e1 = (0,0,1)
  // and we set e2 = (1,0,0) or whatever
  K_t e2;
  if (std::abs(e1.x)>kernel.m_epsilon || std::abs(e1.y)>kernel.m_epsilon) { 
    e2 = K_t(0,0,1) * e1; e2.normalize();
  } else {
    e2 = K_t(1,0,0);
  }
  K_t e3 = e1 * e2;

  // == v_f ==
  v_f = sin_theta*cos(phi) * e2 
    + sin_theta*sin(phi) * e3
    + cos_theta * e1;
  v_f = v_f *  v_f_l;
  //  prob *= ??? // need a factor here
}


void
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::
Details::pick_a_valid_Q_vector
(K_t &Q, float_t &v_Q_l, float_t &E_f, float_t &v_f_l,
 float_t Qcutoff, float_t E_i, float_t v_i_l,  unsigned int branch) 
  const
{
  namespace conversion = mcni::neutron_units_conversion;

  float_t omega;
  do {
    // pick Q
    Q = Q_inCube<K_t, float_t>( Qcutoff );
    v_Q_l = conversion::k2v*Q.length();
    // == phonon energy  ==
    omega = kernel.m_disp.energy( branch, Q );
    // == gain energy or lose energy ==
    E_f = pick_Ef( E_i, omega);

    v_f_l = conversion::E2v(E_f);

    // debug
#ifdef DEEPDEBUG
    journal::debug_t debug(jrnltag);
    //    std::cout << "In file " << __FILE__ << " line " << __LINE__ << "; "
    debug << journal::at(__HERE__)
	  << "Q = " << Q << "; "
	  << "v_Q_l = " << v_Q_l << "; "
	  << "omega = " << omega << "; "
	  << "E_f = " << E_f << "; "
	  << "v_f_l = " << v_f_l << "; "
	  << journal::endl; 
#endif 
    //}
    // == make sure the Q is good ==
  } while ( v_Q_l<std::abs(v_i_l-v_f_l) || v_Q_l>v_i_l+v_f_l );
  //if ( v_Q_l<abs(v_i_l-v_f_l) || v_Q_l>v_i_l+v_f_l ) absorb(ev);

}

  
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::float_t
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::
Details::pick_Ef
( float_t Ei, float_t omega) const
{
  float_t Ef;
    
  if (omega < Ei) {
    if (math::random01()>=0.5) 
      Ef = Ei + omega;
    else 
      Ef = Ei - omega;
  } else {
    Ef = Ei + omega;
  }
  // debug
#ifdef DEEPDEBUG
  journal::debug_t debug(jrnltag);
  //    std::cout << "In file " << __FILE__ << " line " << __LINE__ << "; "
  debug << journal::at(__HERE__)
	<< "Ei = " << Ei << "; "
	<< "Ef = " << Ef << "; "
	<< journal::endl; 
#endif 
  
  return Ef;
}
  
  
std::vector<mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::float_t>
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::
Details::calc_relAccessibleReciVol_MC
(size_t numMCsteps,
 const dispersion_t &disp,
 float_t Qcutoff, float_t E_i) const
{
  if (numMCsteps<1000) {
    journal::warning_t warning(jrnltag);
    warning << journal::at(__HERE__)
	    << "*** Number of MC steps must be larger than 1000 to obtain reliable results!" 
	    << journal::endl;
    //throw;
  }
    
  float_t omega;
  K_t Q;
  float_t v_Q_l;
  float_t E_f, v_f_l;
  unsigned int branch;
  size_t n_brs = disp.nBranches();
  
  namespace conversion = mcni::neutron_units_conversion;
  float_t v_i_l = conversion::E2v(E_i);
  
  // simulation results to be saved in these arrays
  // the first dimension for the cases E_i > E_f and E_i < E_f
  // the second dimension for phonon branches
  std::vector<size_t> N(n_brs);
  std::vector<size_t> valid_N(n_brs);

  // the simulation loop
  for (size_t step = 0; step < numMCsteps; step++)  {
    // pick Q
    Q = Q_inCube<K_t, float_t>( Qcutoff );
    v_Q_l = conversion::k2v*Q.length();
    // pick branch
    branch = pick_phonon_branch( n_brs );
    // == phonon energy  ==
    omega = disp.energy( branch, Q );
    // == gain energy or lose energy ==
    E_f = pick_Ef( E_i, omega);
    
    v_f_l = conversion::E2v(E_f);
    
    // debug
#ifdef DEEPDEBUG
    journal::debug_t debug(jrnltag);
    debug << journal::at(__HERE__)
	  << "Q = " << Q << "; "
	  << "v_Q_l = " << v_Q_l << "; "
	  << "omega = " << omega << "; "
	  << "E_f = " << E_f << "; "
	  << "v_f_l = " << v_f_l << "; "
	  << journal::endl; 
#endif 
    // increment the cooresponding bins
    N[branch]++;
    
    // test if the selected Q vector is good
    if ( v_Q_l<std::abs(v_i_l-v_f_l) || v_Q_l>v_i_l+v_f_l ) {
      // not good
    } else {
      //good
      valid_N[branch]++;
    }
  }
  
  // results
  std::vector<float_t> res(n_brs);
  
  for (size_t br = 0; br<n_brs; br++) {
    res[br] = 1.0*valid_N[br]/N[br];
    
#ifdef DEEPDEBUG
    journal::debug_t debug(jrnltag);
    debug << journal::at(__HERE__)
	  << "phonon branch " << br
	  << "ratio = " << res[br] 
	  << journal::endl; 
#endif 
  }
  return res;
}


mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::
CoherentInelastic_PolyXtal
( const dispersion_t &disp,
  const atoms_t &atoms,
  float_t unitcell_vol,
  dwcalculator_t & dw_calctor,
  float_t temperature,
  float_t Ei, float_t max_omega, 
  float_t max_Q,
  size_t nMCsteps_to_calc_RARV,
  float_t epsilon) 

  : m_disp( disp ),
    m_atoms( atoms ),
    m_DW_calc( &dw_calctor ),
    m_Temperature( temperature ),
    m_uc_vol( unitcell_vol ),
    m_Ei(Ei),
    m_nMCsteps_to_calc_RARV(nMCsteps_to_calc_RARV),
    m_epsilon( epsilon ),
    m_details( new Details(*this) )
{
  
  assert ( atoms.size() == disp.nAtoms() );
#ifdef DEBUG
  journal::debug_t debug(m_details->jrnltag);
  debug << "m_disp=" << &m_disp << journal::newline;
  
  debug << "m_atoms=";
  for (size_t i = 0; i< m_atoms.size(); i++)
    debug  << m_atoms[i] << journal::newline;

  debug << "m_DW_calc=" << m_DW_calc << journal::newline;
  debug << "m_Temperature=" << m_Temperature << journal::newline
	<< "m_uc_vol=" << m_uc_vol << journal::newline;
  debug << journal::endl;
  
#endif

  // calculate the total scattering cross section
  m_tot_scattering_cross_section = 0;
  for (size_t i=0; i<m_atoms.size(); i++) {
    m_tot_scattering_cross_section += m_atoms[i].coherent_cross_section;
  }
  
  namespace conversion = mcni::neutron_units_conversion;

  if (max_Q>0) m_Qcutoff = max_Q;
  else m_Qcutoff = conversion::E2k( m_Ei )
	 +conversion::E2k( m_Ei + m_max_omega); 
  // initialize the array of relative accessible reciprocal space volume
  m_relAccessibleReciVol_arr = 
    m_details->calc_relAccessibleReciVol_MC
    ( m_nMCsteps_to_calc_RARV, m_disp, m_Qcutoff, m_Ei);
}


void
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::absorb
( neutron_t & ev )
{
}


mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::float_t
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::absorption_coefficient
( const neutron_t & ev )
{
  //!!!!!! must reimplement this !!!!
  return scattering_coefficient( ev );
}


mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::float_t
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::scattering_coefficient
( const neutron_t & ev )
{
  float_t ret = m_tot_scattering_cross_section/m_uc_vol;
  // convert to m**-1
  return ret * 1.e2;
}


void
mccomponents::kernels::phonon::CoherentInelastic_PolyXtal::scatter
( neutron_t & ev ) 
{
  namespace conversion = mcni::neutron_units_conversion;

#ifdef DEEPDEBUG
  journal::debug_t debug(m_details->jrnltag);
#endif

  const mcni::Neutron::State  &ns  = ev.state;
  const V_t &v_i   = ns.velocity;
  
  // we need to manipulate the neutron probability. get the reference here.
  float_t               &prob = ev.probability; 

  /* initial velocity magnitude */
  float_t v_i_l = v_i.length();
  // initial energy
  float_t E_i = conversion::v2E( v_i_l );

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "E_i =" << E_i << ","
	<< journal::endl;
#endif

  // pick branch
  unsigned int branch = pick_phonon_branch( m_disp.nBranches());
  prob *= m_disp.nBranches();


  // pick a Q vector
  K_t Q;
  float_t v_Q_l, E_f, v_f_l;
  m_details->pick_a_valid_Q_vector
    ( Q, v_Q_l, E_f, v_f_l, m_Qcutoff, E_i, v_i_l, branch);
  float_t  omega = E_i - E_f;

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "omega =" << omega << ","
	<< "Q =" << Q << ","
	<< journal::endl;
#endif


  // = rotate the Q vector so that the energy relation is satistied =
  // = actually this is done by directly determine the direction of =
  // = final velocity of neutron =
  V_t v_f;
  m_details->pick_v_f( prob, v_f, v_i, v_f_l, v_Q_l);

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "vf =" << v_f
	<< journal::endl;
#endif


  // change the velocity of neutron. other things stay put
  ev.state.velocity = v_f;


  // now we have the velocity representation of k_i, k_f, and Q, we want to know
  // the wave vector representation
  using conversion::v2k;
  float_t k_i_l = v2k * v_i_l;
  float_t k_f_l = v2k * v_f_l;
  float_t Q_l = v2k * v_Q_l;
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "ki length = " << k_i_l << ", "
	<< "kf length = " << k_f_l << ", "
	<< "Q length = " << Q_l
	<< journal::endl;
#endif

  // thermal factor
  float_t therm_factor = phonon_bose_factor( omega, m_Temperature );
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "thermal factor = " << therm_factor
	<< journal::endl;
#endif

  // debye waller factor 
  float_t DW = m_DW_calc->DW( Q_l );
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "debye waller factor = " << DW
	<< journal::endl;
#endif
  DW = std::exp( -DW );
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "debye waller factor = " << DW
	<< journal::endl;
#endif

  if (E_i > omega) prob *= 2.0; // two choices of E_f: E_f>E_i or E_f<E_i

  prob /= m_uc_vol;
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  //prob *= m_sigma_coh/m_Mass; //should be \sum{sigma_inc/M}
  
  // This term is the term of |\sum\frac{b_d}{M_d} exp(i\kappa\dot d) (\kappa \dot e) |^2 of page 46 of Squires.
  // It should include the debye-waller factor
  // but for now, we will consider dw factor to be constant
  // and put it in later.
  float_t norm_of_slsum = std::norm
    (sum_of_scattering_length<complex_t, K_t, epsilon_t, atom_t, atoms_t, dispersion_t>
    ( Q, branch, m_atoms, m_disp ) );
  // convert unit of scattering length to meter from fm
  norm_of_slsum /= 1e30;
  // divide this quautity by \sigma_coh because we want a normalized
  // value
  norm_of_slsum /= (m_tot_scattering_cross_section*1e-28);
  // convert the q**2 in that term to be in energy unit (meV), which
  // will cancel with meV unit of phonon energy
  prob *= conversion::ksquare2E( norm_of_slsum );

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  
  prob *= DW;
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  prob *= k_f_l/k_i_l;
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  prob *= therm_factor;
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  prob /= std::abs(omega);
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  prob *= 1/(k_i_l)/(k_f_l)/(Q_l);
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  prob *= m_Qcutoff * m_Qcutoff * m_Qcutoff * 8.0;
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  prob *= m_relAccessibleReciVol_arr[branch];
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "prob = " << prob 
	<< journal::endl;
#endif
  prob /= 8*physics::pi;
#ifdef DEEPDEBUG
  debug << journal::endl;
#endif
  //prob *= (epsdotq2*K2V*K2V*VS2E)/std::abs(omega)*therm_factor;
}


// version
// $Id$

// End of file 

