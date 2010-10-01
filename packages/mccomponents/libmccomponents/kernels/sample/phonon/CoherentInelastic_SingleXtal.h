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


#ifndef PHONON_COHERENETINELATIC_SINGLEXTAL_H
#define PHONON_COHERENETINELATIC_SINGLEXTAL_H


#include <memory>
#include "AbstractScatteringKernel.h"
#include "AtomicScatterer.h"
#include "vector3.h"


// forward declarations
namespace mcni {
  template <typename NumType> class Vector3;
}

namespace DANSE{ 
  namespace phonon{
    class AbstractDispersion_3D;
    template <typename Float> 
    class AbstractDebyeWallerFactorCalculator;
  }
}

namespace mccomponents{
  namespace kernels{
    class TargetCone;
  }
}


namespace mccomponents{
  
  namespace kernels{

    namespace phonon{

      //! coherent inelastic phonon scattering. single crystal sample.
      class CoherentInelastic_SingleXtal : public AbstractScatteringKernel {
      public:
	
	// typedefs
	typedef double float_t;
	typedef mcni::Vector3<float_t> R_t;
	typedef mcni::Vector3<float_t> K_t;
	typedef mcni::Vector3<float_t> V_t;
	typedef DANSE::phonon::AbstractDispersion_3D dispersion_t;
	typedef std::complex<float_t> complex_t;
	typedef mcni::Vector3< complex_t > epsilon_t;
	typedef AtomicScatterer atom_t;
	typedef std::vector< atom_t >  atoms_t;
	typedef DANSE::phonon::AbstractDebyeWallerFactorCalculator<float_t> dwcalculator_t;
	typedef mcni::Neutron::Event neutron_t;
	typedef mccomponents::math::RootsFinder rootsfinder_t;
	typedef TargetCone target_region_t;

	//! ctor
	/*!
	  constructor
	*/
	CoherentInelastic_SingleXtal
	( const dispersion_t &disp,
	  const atoms_t &atoms,
	  float_t unitcell_vol,
	  dwcalculator_t & dw_calctor,
	  float_t temperature,
	  float_t deltaV_Jacobi, 
	  const rootsfinder_t & roots_finder,
	  const target_region_t & target_region,
	  float_t epsilon = 1.e-10 ) ;

	virtual float_t absorption_coefficient( const neutron_t & ev );
	virtual float_t scattering_coefficient( const neutron_t & ev );
	virtual void scatter( neutron_t & ev );
	virtual void absorb( neutron_t & ev );
	
      private:

	virtual void pick_a_final_state( neutron_t & ) const;

	void   pick_v_f
	(std::vector<float_t> & prob, V_t & v_f, int branch, 
	 const V_t & v_i, float_t v_i_l) const;

	// data
	const dispersion_t & m_disp;
	atoms_t m_atoms;
	dwcalculator_t *m_DW_calc;
	float_t m_Temperature;
	float_t m_uc_vol;
	float_t m_tot_scattering_cross_section;
    
	// root finding facility
	const rootsfinder_t & m_roots_finder;
	// delta v (velocity) for calculating Jacobi factor
	float_t m_DV;

	// target region
	const target_region_t *m_target_region;
      };

    }
  }
}

#endif//  PHONON_COHERENETINELATIC_SINGLEXTAL_H



// version
// $Id: Phonon_CoherentInelastic_SC.h 543 2006-04-28 00:52:08Z jiao $

// End of file 
