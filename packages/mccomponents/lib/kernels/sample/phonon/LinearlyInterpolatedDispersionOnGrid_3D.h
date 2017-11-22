// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef PHONON_LINEARLYINTERPOLATEDDISPERSIONONGRID_3D_H
#define PHONON_LINEARLYINTERPOLATEDDISPERSIONONGRID_3D_H


#include <complex>
#include "mcni/geometry/Vector3.h"
#include "histogram/NdArraySlice.h"
#include "LinearlyInterpolatedGridData_3D.h"
#include "LinearlyInterpolatedPolarizationOnGrid_3D.h"
#include "AbstractDispersion_3D.h"


namespace DANSE { 
  namespace phonon {

    /// Linearly interpolate dispersion grid data
    /// suppose we have an 7D array of polarization:
    ///   pol[ qx, qy, qz, branch, atom, (x|y|z), (real|imag) ]
    /// and a 4D array for phonon energies
    ///   omega[ qx, qy, qz, branch ]
    template <typename Array_7D, typename Array_4D>
    class LinearlyInterpolatedDispersionOnGrid_3D: public AbstractDispersion_3D {
    public:
      // types
      typedef double float_t;
      typedef AbstractDispersion_3D::n_t n_t;
      typedef Array_7D epsilonarray_t;
      typedef Array_4D Earray_t;
      typedef LinearlyInterpolatableAxis<float_t> axis_t;
      typedef std::complex< float_t > complex_t;
      typedef mcni::Vector3< complex_t > epsilon_t;
      typedef mcni::Vector3< float_t > K_t;

      // meta methods
      LinearlyInterpolatedDispersionOnGrid_3D
      ( n_t nAtoms,
	const axis_t & QX, const axis_t & QY, const axis_t &QZ, 
	epsilonarray_t & epsilon_data, Earray_t & E_data );
      ~LinearlyInterpolatedDispersionOnGrid_3D();
      
      // methods
      virtual float_t energy(n_t branch_id, const K_t &k) const;
      virtual epsilon_t polarization(n_t branch_id, n_t atom_id, const K_t &k) const;
      virtual float_t max_energy(n_t branch_id) const {return m_max_energy[branch_id];}
      virtual float_t min_energy(n_t branch_id) const {return m_min_energy[branch_id];}

    private:
      // data
      typedef Histogram::NdArraySlice< Earray_t > Earray_slice_t;
      typedef LinearlyInterpolatedGridData_3D< Earray_slice_t, float_t, n_t> interp_Earray_t; 
      ///interp_Earray_t1 that holds a Earray_slice_t and a interp_Earray_t
      struct interp_Earray_t1 {
	Earray_slice_t slice;
	interp_Earray_t interpolated;
	interp_Earray_t1
	( const axis_t & Qx, const axis_t & Qy, const axis_t &Qz,
	  Earray_t & E_data, const std::vector<int> & indexes )
	  : slice( E_data, indexes ),
	    interpolated( Qx, Qy, Qz, slice )
	{}	
      };
      std::vector<interp_Earray_t1 *> m_Evsbranch;

      typedef Histogram::NdArraySlice< epsilonarray_t > epsilonarray_slice_t;
      typedef LinearlyInterpolatedPolarizationOnGrid_3D< epsilonarray_slice_t > interp_polarray_t;
      struct interp_polarray_t1 {
	epsilonarray_slice_t slice;
	interp_polarray_t interpolated;
	interp_polarray_t1
	( const axis_t & Qx, const axis_t & Qy, const axis_t &Qz,
	  epsilonarray_t & epsilon_data, const std::vector<int> & indexes )
	  : slice( epsilon_data, indexes ),
	    interpolated( Qx, Qy, Qz, slice )
	{}
      };

      std::vector<interp_polarray_t1 *> m_polvsbranchatom;
      std::vector<float_t> m_max_energy, m_min_energy; // energy limits for each branch
    };

  } // phonon::
} // DANSE::


#include "LinearlyInterpolatedDispersionOnGrid_3D.icc"

#endif //PHONON_LINEARLYINTERPOLATEDDISPERSIONONGRID_3D_H

// version
// $Id$

// End of file 
