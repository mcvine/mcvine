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


/// Given a 1-dimensional Grid Data, classes in this file provide a
/// functor-like interface.
/// In other words, given start, step, and number of steps for 
/// x axes, and a (1+nx) value array,
/// we can calculate (by linear interpolation) value of f(x).
/// No extrapolation however!


#ifndef LINEARLYINTERPOLATEDGRIDDATA_1D_H
#define LINEARLYINTERPOLATEDGRIDDATA_1D_H


#include "exception.h"
#include "LinearlyInterpolatableAxis.h"


namespace DANSE { 
  
  namespace phonon {

  /// template arguments:
  ///   Float: float type
  ///   Array_1D: an array type. must define operator[] which takes an integer
  template < typename Array_1D, typename FloatType,
	     typename IndexType = unsigned int>
  class LinearlyInterpolatedGridData_1D {

  public:

    // types  
    typedef Array_1D  dataarray_t;
    typedef LinearlyInterpolatableAxis< FloatType, IndexType > axis_t;
    typedef IndexType index_t;
    typedef FloatType float_t;

    // meta methods
    /// ctor.
    LinearlyInterpolatedGridData_1D
    ( const axis_t & x, const dataarray_t & dataarray );

    /// function-like interface. get value.
    ///  f(x,y,z) --> v
    FloatType operator ()
    ( const FloatType & x ) const;

  private:
    const axis_t & m_xaxis;
    const dataarray_t & m_dataarray;
  };
  
  }
} // DANSE::phonon


#include "LinearlyInterpolatedGridData_1D.icc"

#endif //LINEARLYINTERPOLATEDGRIDDATA_1D_H




// version
// $Id$

// End of file 
