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


#ifndef PHONON_LINEARLYINTERPOLATEDPOLARIZATIONONGRID_3D_H
#define PHONON_LINEARLYINTERPOLATEDPOLARIZATIONONGRID_3D_H


#include <complex>
#include "mcni/geometry/Vector3.h"
#include "histogram/NdArraySlice.h"
#include "LinearlyInterpolatedGridData_3D.h"


namespace DANSE { 
  namespace phonon {

    /// Linearly interpolate polarization grid data
    /// suppose we have an 5D array of polarization pol[ qx, qy, qz, (x|y|z), (real|imag) ]
    /// this class has a way to calculate pol( q ) --> complex 3d vector
    template <typename Array_5D>
    class LinearlyInterpolatedPolarizationOnGrid_3D {
    public:
      // types
      typedef Array_5D array_t;
      typedef double float_t;
      typedef unsigned int index_t;
      typedef LinearlyInterpolatableAxis<float_t> axis_t;
      typedef std::complex< float_t > complex_t;
      typedef mcni::Vector3< complex_t > epsilon_t;
      typedef mcni::Vector3< float_t > K_t;

      // meta methods
      LinearlyInterpolatedPolarizationOnGrid_3D
      ( const axis_t & QX, const axis_t & QY, const axis_t &QZ, array_t & data );
      ~LinearlyInterpolatedPolarizationOnGrid_3D();
      
      // methods
      epsilon_t operator() (const K_t &q) const;

    private:
      // data
      typedef Histogram::NdArraySlice< array_t > slice_t;
      typedef LinearlyInterpolatedGridData_3D< slice_t, float_t, index_t> interp_t; 
      ///interp_t1 that holds a slice_t and a interp_t
      struct interp_t1 {
	slice_t slice;
	interp_t interpolated;
	interp_t1( const axis_t & Qx, const axis_t & Qy, const axis_t &Qz,
		   array_t & data, const std::vector<int> & indexes )
	  : slice( data, indexes ),
	    interpolated( Qx, Qy, Qz, slice )
	{}	
      };
      interp_t1 *m_xr, *m_xi, *m_yr, *m_yi, *m_zr, *m_zi;
      
    };

  } // phonon::
} // DANSE::


#include "LinearlyInterpolatedPolarizationOnGrid_3D.icc"

#endif //PHONON_LINEARLYINTERPOLATEDPOLARIZATIONONGRID_3D_H

// version
// $Id$

// End of file 
