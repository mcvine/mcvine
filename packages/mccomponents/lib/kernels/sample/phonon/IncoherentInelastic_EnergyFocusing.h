// -*- C++ -*-
//


#ifndef PHONON_INCOHERENTINELASTIC_ENERGYFOCUSING_H
#define PHONON_INCOHERENTINELASTIC_ENERGYFOCUSING_H

#include <memory>
#include "KernelBase.h"
#include "AtomicScatterer.h"
#include "vector3.h"

//forward declaration
namespace DANSE{
  namespace phonon{
    template <typename Float> 
    class AbstractDOS;
    template <typename Float> 
    class AbstractDebyeWallerFactorCalculator;
  }
}

namespace mccomponents{
  
  namespace kernels{

    namespace phonon{

      //! incoherent inelastic phonon scattering with energy focusing. only energy loss
      class IncoherentInelastic_EnergyFocusing : public KernelBase {
      public:
	// typedefs
	typedef double float_t;
	typedef mcni::Vector3<float_t> R_t;
	typedef mcni::Vector3<float_t> K_t;
	typedef mcni::Vector3<float_t> V_t;
	typedef AtomicScatterer atom_t;
	typedef std::vector< atom_t >  atoms_t;
	typedef DANSE::phonon::AbstractDOS<float_t> dos_t;
	typedef DANSE::phonon::AbstractDebyeWallerFactorCalculator<float_t> dwcalculator_t;
	typedef mcni::Neutron::Event neutron_t;
	
	//! ctor
	/*!
	  parameters
	   unitcell_vol  volume of unitcell, units: AA**3
	   dos           density of states
	   dw_calctor    debye waller factor calculator
	   temperature   temperature. unit: K
	   ave_mass      average mass of atoms in the unit cell. if 0, will compute from "atoms". unit: amu
	   scattering_xs total scattering cross section. if 0, will compute from "atoms". unit: barn
	   absorption_xs total absorption cross section. if 0, will compute from "atoms". unit: barn
	*/
	IncoherentInelastic_EnergyFocusing
	(const atoms_t &atoms,
	 float_t unitcell_vol,
	 float_t Ef, float_t dEf,
	 dos_t & dos,
	 dwcalculator_t & dw_calctor,
	 float_t temperature,
	 float_t ave_mass = 0., 
	 float_t scattering_xs = 0., float_t absorption_xs = 0.
	 ) ;
	
	virtual float_t absorption_coefficient( const neutron_t & ev );
	virtual float_t scattering_coefficient( const neutron_t & ev );
	virtual void S( neutron_t & ev );
	virtual void absorb( neutron_t & ev );

      private:
	
	// data
	atoms_t m_atoms;
	float_t m_Mass; // average mass in unit cell
	float_t m_uc_vol;
	float_t m_Ef, m_dEf;
	dos_t * m_dos;
	dwcalculator_t *m_DW_calc;
	float_t m_Temperature;
	float_t m_max_phonon_energy;
	float_t m_total_scattering_xs, m_total_absorption_xs;
	
	// implementation details
	struct Details;
	std::auto_ptr<Details> m_details;
      };

    } // phonon::
  } // kernels::
} // mccomponents::

#endif//  PHONON_INCOHERENTINELASTIC_ENERGYFOCUSING_H


// End of file 
