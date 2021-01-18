// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2010 All Rights Reserved 
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <cmath>
#include <complex>
//#include <portinfo>
#include "journal/warning.h"

#ifdef DEEPDEBUG
#define DEBUG
#endif

#ifdef DEBUG
#include "journal/debug.h"
#endif

#include "mccomponents/kernels/sample/phonon/scattering_length.h"
#include "mcni/exceptions.h"
#include "mcni/neutron/units_conversion.h"
#include "mccomponents/math/random.h"
#include "mccomponents/math/misc.h"
#include "mccomponents/math/rootfinding.h"
#include "mccomponents/physics/constants.h"
#include "mccomponents/kernels/sample/phonon/vector3.h"
#include "mccomponents/kernels/sample/phonon/CoherentInelastic_SingleXtal.h"
#include "mccomponents/kernels/sample/phonon/utils.h"
#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"
#include "mccomponents/kernels/sample/phonon/TargetCone.h"
// #include "mccomponents/kernels/sample/phonon/generateQ.h"

#include "mccomponents/kernels/sample/phonon/Omega_minus_deltaE.h"



namespace{
  const char * phonon_cohinel_sc_journal_channel = "CoherentInelastic_SingleXtal";
}

/*
  Notes about probability factors in pick_a_final_state and pick_v_f.
  
  The probability of the neutron is adjusted in a series of 
  steps, and it can be confusing.

  In pick_v_f:
    prob_factors.push_back(nf); // easy
    float_t Jacobi = std::abs(f2-f1)/(2*delta_v);
    prob_factors.push_back(2*vsq2e*v_f_l/Jacobi);

   Since f2,f1 are in meV, 2*vsq2e*v_f_l/Jacobi) has dimension 1:
    f1, f2: energy in mev
    delta_v: velocity in m/s
    v_f_l/Jacobi: v/(E/v) = v^2/E
    2*vsq2e*v_f_l/Jacobi: 1.

  In pick_a_final_state, there are some simple ones:

    prob_factors.push_back(solid_angle): 1
    prob_factors.push_back( m_disp.nBranches() ): 1
    prob_factors.push_back( k_f_l/k_i_l ): 1.
    prob_factors.push_back( DW ):  1.
    prob_factors.push_back( therm_factor ): 1.

   all of them have dimension 1.

  The difficult one is here:
    prob_factors.push_back(neutron_units_conversion::ksquare2E( norm_of_slsum )/std::abs(omega));

    and norm_of_slsum is
      float_t norm_of_slsum = std::norm(sclen);
      norm_of_slsum /= 1e30;
      // divide this quautity by \sigma_coh because we want a normalized
      // value
      norm_of_slsum /= (m_tot_scattering_xs*1e-28);

    and sclen is

      complex_t sclen = sum_of_scattering_length
        <complex_t, K_t, epsilon_t, atom_t, atoms_t, dispersion_t>
	(Q, branch, m_atoms, m_disp );

    and sum_of_scattering_length is a result of sum of terms like this

      complex_t c1 = atom.coherent_scattering_length/std::sqrt(atom.mass) \
        * std::exp( cI * qdotd ) * qdote;

   So the dimension is (L*Q)**2/m / L**2 / E * Qsq2E = 1 if m is in unit of atomic mass

 */

mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::CoherentInelastic_SingleXtal
( const dispersion_t &disp,
  const atoms_t &atoms,
  float_t unitcell_vol,
  dwcalculator_t & dw_calctor,
  float_t temperature,
  float_t deltaV_Jacobi, 
  const rootsfinder_t & roots_finder,
  const target_region_t & target_region,
  float_t epsilon) 
  : m_disp(disp),
    m_atoms(atoms),
    m_DW_calc( &dw_calctor ),
    m_Temperature( temperature ),
    m_uc_vol( unitcell_vol ),
    m_roots_finder( roots_finder ),
    m_target_region( &target_region),
    m_DV( deltaV_Jacobi )
{
#ifdef DEBUG
  journal::debug_t debug(phonon_cohinel_sc_journal_channel);
  debug << "m_disp=" << &m_disp << ","
	<< "m_DW_calc=" << m_DW_calc << ","
	<< "m_Temperature=" << m_Temperature << ","
	<< "m_uc_vol=" << m_uc_vol << ","
	<< journal::endl;
#endif
  
  // calculate the total scattering cross section  
  m_tot_scattering_xs = 0;
  for (size_t i=0; i<m_atoms.size(); i++) {
    m_tot_scattering_xs += m_atoms[i].coherent_cross_section;
  }
  
  m_tot_absorption_xs = 0;
  for (size_t i=0; i<m_atoms.size(); i++) {
    m_tot_absorption_xs += m_atoms[i].absorption_cross_section;
  }
}


bool
mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::pick_v_f
(std::vector<float_t> & prob_factors, 
 V_t & v_f,
 int branch,
 const V_t & v_i,
 float_t v_i_l)
const
  /// given the final direction of neutron is fixed, choose the magnitute of the final velocity
  /// of the neutron by solving the equations of energy and momentum conservation
  /// the choice is done randomly
  /// the probability should be updated according to freedom of selection and the Jacobi, which we call probability factors. These factors are stored into prob_factors so that the main function can use them to update the probability.
  /// the chosen magnitude of final velocity is applied to v_f
  /// branch.......phonon branch id. fixed
  /// v_i..........neutron initial velocity
  /// v_i_l........magnitude of neutron initial velocity
{
#ifdef DEBUG
  journal::debug_t debug(phonon_cohinel_sc_journal_channel);
  debug << journal::at(__HERE__)
	<< "entering pick_v_f" 
	<< journal::endl;
#endif

#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "create function omega(q)-dE" 
	<< journal::endl;
#endif
  // function omega(Q)-dE
  Omega_q_minus_deltaE omq_m_dE(branch, v_f, v_i, v_i_l, m_disp);

#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "find roots of function omega(Q)-dE" 
	<< journal::endl;
#endif
  // find roots of function omega(Q)-dE
  std::vector<float_t> vf_list;
  // number of roots
  vf_list = m_roots_finder.solve( 0, v_i_l*2, omq_m_dE );
  size_t nf = vf_list.size(); 

#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "found " << nf << "roots." 
	<< journal::endl;
#endif

  if (nf<1) {
    std::cerr << "** Unable to find solution for function omega(Q)-dE";
    omq_m_dE.print(std::cerr, 0, v_i_l*2, v_i_l/10);
    std::cerr << std::endl;
    return true;
    /*
    mcni::throw_fatal_path_error
      ( phonon_cohinel_sc_journal_channel,
        journal::at(__HERE__),
        "Unable to find solution for function omega(Q)-dE");
    */
  }
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "choose a root from the roots" 
	<< journal::endl;
#endif
  // choose a root (length of vf)
  size_t index=mccomponents::math::random(size_t(0), nf);
  float_t v_f_l = vf_list[index];
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "chose root #" << index
	<< ": " << v_f_l
	<< journal::endl;
#endif
  // adjust v_f
  v_f.normalize(); v_f = v_f * v_f_l;
  // adjust prob
  prob_factors.push_back(nf);

  // calculate Jacobi factor
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "calculate Jacobi factor near " << v_f_l
	<< journal::endl;
#endif
  float_t f1, f2;
  float_t delta_v = m_DV*v_i_l; // m_DV is fractional change
  f1 = omq_m_dE.evaluate( v_f_l-delta_v );
  f2 = omq_m_dE.evaluate( v_f_l+delta_v );
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "f1=" << f1
	<< ", f2=" << f2
	<< journal::endl;
#endif
  using namespace mcni::neutron_units_conversion;
  // adjust prob
  // float_t Jacobi = std::abs(f2-f1)/(2*delta_v*k2v);
  float_t Jacobi = std::abs(f2-f1)/(2*delta_v);
  // prob_factors.push_back(2*vsquare2E( v_f_l/Jacobi ));
  using mcni::neutron_units_conversion::vsq2e;
  prob_factors.push_back(2*vsq2e*v_f_l/Jacobi);
  
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "probability factors" << prob_factors
	<< journal::endl;
#endif
  return false;
}


void
mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::pick_a_final_state
( neutron_t & ev ) const
{
#ifdef DEBUG
  journal::debug_t debug(phonon_cohinel_sc_journal_channel);
#endif
  
  // init an array of probability factors which could result from various random-selection processes. 
  std::vector<float_t> prob_factors;

  using mccomponents::math::random;
  using namespace mcni;

  // input neutron states
  const neutron_t::state_t    &ns  = ev.state;
  V_t   v_i = ns.velocity;

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__) << "v_i = " << v_i << journal::endl;
#endif
  
  /* initial velocity magnitude */
  float_t v_i_l = v_i.length();
  // initial energy
  float_t E_i = neutron_units_conversion::v2E( v_i_l );

#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "E_i =" << E_i << ","
	<< journal::endl;
#endif

  // establish "good" branches (not too higher than Ei)
#ifdef DEEPDEBUG
  std::cout << "Total number of branches: " << m_disp.nBranches() << std::endl;
  std::cout << "Good branches: ";
#endif
  std::vector<unsigned int> good_branches;
  for (int br=0; br<m_disp.nBranches(); br++) {
    // if a branch is too high compared to Ei, it rarely will make contributions to
    // scattering.
    if (m_disp.min_energy(br)<E_i*1.5) {
      good_branches.push_back((unsigned int)br);
    }
  }
  V_t v_f;
  float_t solid_angle;
  bool pick_vf_failed;
  int Niters = 100, iteration;
  unsigned int branch;
  for (iteration=0; iteration<Niters; iteration++) {
    // pick direction of scattered neutron
    solid_angle = kernels::choose_scattering_direction(v_f, *m_target_region); 
    v_f.normalize();
    // pick branch
    branch = good_branches[(int)math::random(size_t(0), good_branches.size())];
    // old implementation: unsigned int branch = pick_phonon_branch(m_disp.nBranches());
    // pick the final velocity of neutron
    pick_vf_failed = pick_v_f(prob_factors, v_f, branch, v_i, v_i_l);
    if (!pick_vf_failed) break;
  }
  if (pick_vf_failed) {
#ifdef DEEPDEBUG
    std::cout << "Failed to find a good scattering direction in " << Niters << " iterations." << std::endl;
#endif
    return;
  } else {
#ifdef DEEPDEBUG
    std::cout << "Found solution at iteration " << iteration << std::endl;
#endif
  }
  prob_factors.push_back(solid_angle);
  prob_factors.push_back( good_branches.size() );
#ifdef DEEPDEBUG
    debug << journal::at(__HERE__) << "v_i = " << v_i << journal::endl;
#endif
  
  float_t v_f_l = v_f.length();
  float_t E_f = neutron_units_conversion::v2E( v_f_l );  
  
  // phonon energy
  float_t  omega = E_i - E_f;
  
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< "omega =" << omega << ","
	<< "E_f =" << E_f << ","
	<< journal::endl;
#endif
  // Q vector
  K_t Q = neutron_units_conversion::v2k*(v_i-v_f);

  // change the velocity of neutron. other things stay put
  ev.state.velocity = v_f;
  
  // now we have the velocity representation of k_i, k_f, and Q, we want to know
  // the wave vector representation
  float_t k_i_l = neutron_units_conversion::v2k * v_i_l;
  float_t k_f_l = neutron_units_conversion::v2k * v_f_l;
  float_t Q_l   = Q.length();

  // prob *= m_sigma_coh/m_Mass; //should be \sum{sigma_inc/M}
  //
  // This term is the term of |\sum\frac{b_d}{M_d} exp(i\kappa\dot d) (\kappa \dot e) |^2 of page 46 of Squires.
  // It should include the debye-waller factor
  // but for now, we will consider dw factor to be constant
  // and put it in later.
  complex_t sclen = sum_of_scattering_length
    <complex_t, K_t, epsilon_t, atom_t, atoms_t, dispersion_t>
    (Q, branch, m_atoms, m_disp );
  float_t norm_of_slsum = std::norm(sclen);
  // convert unit of scattering length to meter from fm
  norm_of_slsum /= 1e30;
  // divide this quautity by \sigma_coh because we want a normalized
  // value
  norm_of_slsum /= (m_tot_scattering_xs*1e-28);
  // convert the q**2 in that term to be in energy unit (meV), which
  // will cancel with meV unit of phonon energy
  prob_factors.push_back(neutron_units_conversion::ksquare2E( norm_of_slsum )/std::abs(omega));

  // thermal factor
  float_t therm_factor = kernels::phonon::phonon_bose_factor(omega, m_Temperature);

  // debye waller factor
  float_t DW = exp( -m_DW_calc->DW( Q_l ) );

  prob_factors.push_back( k_f_l/k_i_l );
  prob_factors.push_back( DW );
  prob_factors.push_back( therm_factor );

  float_t prob_factor = mccomponents::math::product<float_t>( prob_factors );
  // we need to manipulate the neutron probability. get the reference here.
  float_t               &prob = ev.probability; 
#ifdef DEEPDEBUG
  if (prob_factor>100000) {
    debug << journal::at(__HERE__)
	  << "prob = " << prob << "\n"
	  << "Q = " << Q << "\n"
	  << "omega = " << omega << "\n"
	  << "k_i = " << v_i* neutron_units_conversion::v2k << "\n"
	  << "k_f = " << v_f* neutron_units_conversion::v2k << 
      journal::endl;
    for (int i=0; i<prob_factors.size(); i++) {
      debug << " p[" << i << "] = " << prob_factors[i] << "\n";
    }
    debug << journal::endl;
  }
#endif
  prob *= prob_factor;
}


void
mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::absorb
( neutron_t & ev )
{
}


mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::float_t
mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::absorption_coefficient
( const neutron_t & ev )
{
  float_t ret = m_tot_absorption_xs/m_uc_vol*1.e2;
  float_t v = ev.state.velocity.length();
  return ret * (2200/v);
}


mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::float_t
mccomponents::kernels::phonon::CoherentInelastic_SingleXtal::scattering_coefficient
( const neutron_t & ev )
{
  float_t ret = m_tot_scattering_xs/m_uc_vol;
  // convert to m**-1
  return ret * 1.e2;
}



// version
// $Id$

// End of file 
