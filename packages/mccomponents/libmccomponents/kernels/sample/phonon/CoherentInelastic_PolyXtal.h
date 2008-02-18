// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef PHONON_COHERENTINELASTIC_POLYXTAL_H
#define PHONON_COHERENTINELASTIC_POLYXTAL_H


#include "AbstractScatteringKernel.h"
#include "AtomicScatterer.h"
#include "vector3.h"

//forward declaration
namespace DANSE{
  namespace phonon{
    class AbstractDispersion_3D;
    template <typename Float> 
    class AbstractDebyeWallerFactorCalculator;
  }
}

namespace mccomponents{
  
  namespace kernels{

    namespace phonon{

      //! coherent inelastic phonon scattering. polycrystalline sample.
      class CoherentInelastic_PolyXtal : public AbstractScatteringKernel {
      public:
	// typedefs
	typedef double float_t;
	typedef mcni::Vector3<float_t> R_t;
	typedef mcni::Vector3<float_t> K_t;
	typedef mcni::Vector3<float_t> V_t;
	typedef DANSE::phonon::AbstractDispersion_3D dispersion_t;
	typedef AtomicScatterer atom_t;
	typedef std::vector< atom_t >  atoms_t;
	typedef DANSE::phonon::AbstractDebyeWallerFactorCalculator<float_t> dwcalculator_t;
	typedef mcni::Neutron::Event neutron_t;
	
	//! ctor
	/*!
	  parameters
	   Ei          incident neutron energy
	   max_omega   maximum phonon energy
	   max_Q       maximum phonon Q
	   unitcell_vol volume of unitcell, units: AA**3
	   dw_calctor  debye waller factor calculator
	   temperature temperature. unit: K
	   nMCsteps_to_calc_RARV 
	*/
	CoherentInelastic_PolyXtal
	( const dispersion_t &disp,
	  const atoms_t &atoms,
	  float_t unitcell_vol,
	  dwcalculator_t & dw_calctor,
	  float_t temperature,
	  float_t Ei, float_t max_omega, 
	  float_t max_Q,
	  size_t nMCsteps_to_calc_RARV) ;
	
	virtual float_t absorption_coefficient( const neutron_t & ev );
	virtual float_t scattering_coefficient( const neutron_t & ev );
	virtual void scatter( neutron_t & ev );
	virtual void absorb( neutron_t & ev );

      private:
	
	void   pick_v_f
	(float_t & prob, 
	 V_t & v_f,
	 float_t v_i_l, float_t v_f_l, float_t v_Q_l) const;
	
	void   pick_a_valid_Q_vector
	(K_t &Q, float_t &v_Q_l, float_t &E_f, float_t &v_f_l,
	 float_t Qcutoff, float_t E_i, float_t v_i_l, unsigned int branch) const;

	// data
	const dispersion_t & m_disp;
	atoms_t m_atoms;
	dwcalculator_t *m_DW_calc;
	float_t m_Temperature;
	float_t m_uc_vol;
	
	float_t m_Ei, m_max_omega;
	std::vector <float_t> m_relAccessibleReciVol_arr;
	float_t m_Qcutoff;

	float_t m_tot_scattering_cross_section;
	
	size_t m_nMCsteps_to_calc_RARV;
      };

    } // phonon::
  } // kernels::
} // mccomponents::

#endif//  PHONON_COHERENTINELASTIC_POLYXTAL_H



// version
// $Id: Phonon_CoherentInelastic_Poly.h 327 2005-11-27 05:40:42Z linjiao $

// End of file 
