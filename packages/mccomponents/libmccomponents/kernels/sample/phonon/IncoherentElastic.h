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


#ifndef PHONON_INCOHERENTELASTIC_H
#define PHONON_INCOHERENTELASTIC_H

#include <memory>
#include "AbstractScatteringKernel.h"
#include "AtomicScatterer.h"
#include "vector3.h"

//forward declaration
namespace DANSE{
  namespace phonon{
    /*
    template <typename Float> 
    class AbstractDebyeWallerFactorCalculator;
    */
  }
}

namespace mccomponents{
  
  namespace kernels{

    namespace phonon{

      //! incoherent elastic phonon scattering.
      class IncoherentElastic : public AbstractScatteringKernel {
      public:
	// typedefs
	typedef double float_t;
	typedef mcni::Vector3<float_t> R_t;
	typedef mcni::Vector3<float_t> K_t;
	typedef mcni::Vector3<float_t> V_t;
	typedef std::complex<float_t> complex_t;
	typedef mcni::Vector3< complex_t > epsilon_t;
	typedef AtomicScatterer atom_t;
	typedef std::vector< atom_t >  atoms_t;
	// typedef DANSE::phonon::AbstractDebyeWallerFactorCalculator<float_t> dwcalculator_t;
	typedef mcni::Neutron::Event neutron_t;
	
	//! ctor
	/*!
	  parameters
	   atoms: a list of atoms in the unitcell
	   unitcell_vol volume of unitcell, units: AA**3
	   dw_core: Debye Waller 2W = dw_core * Q**2
	   scattering_xs: total scattering cross section. if 0, will compute from "atoms". unit: barn
	   absorption_xs: total absorption cross section. if 0, will compute from "atoms". unit: barn
	*/
	IncoherentElastic
	(const atoms_t &atoms,
	 float_t unitcell_vol,
	 float_t dw_core, 
	 float_t scattering_xs = 0., float_t absorption_xs = 0.
	 );
	
	virtual float_t absorption_coefficient( const neutron_t & ev );
	virtual float_t scattering_coefficient( const neutron_t & ev );
	virtual void scatter( neutron_t & ev );
	virtual void absorb( neutron_t & ev );

      private:
	
	// data
	atoms_t m_atoms;
	float_t m_uc_vol;
	float_t m_dw_core;
	float_t m_total_scattering_xs, m_total_absorption_xs;

	// implementation details
	struct Details;
	std::auto_ptr<Details> m_details;
      };

    } // phonon::
  } // kernels::
} // mccomponents::

#endif//  PHONON_INCOHERENTELASTIC_H



// version
// $Id: IncoherentElastic.h 603 2010-10-04 15:58:16Z linjiao $

// End of file 
