// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2007-2014  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


/// Given a 3-dimensional Grid Data, classes in this file provide a
/// functor-like interface.
/// In other words, given start, step, and number of steps for 
/// x,y,z axes, and a (1+nx) X (1+ny) X (1+nz) value array,
/// we can calculate (by nearest neighbor) value of f(x,y,z).
/// No extrapolation however!
/// This is an approximation. will used by polarizations


#ifndef NNGRIDDATA_3D_H
#define NNGRIDDATA_3D_H


#include "exception.h"
#include "LinearlyInterpolatableAxis.h"


namespace DANSE { 
  
  namespace phonon {

  /// template arguments:
  ///   Float: float type
  ///   Array_3D: an array type. must define operator[] which takes a Size[3]
  ///   Size: unsigned integer
  template < typename Array_3D, typename FloatType,
	     typename Size = unsigned int>
  class NNGridData_3D {

  public:

    // types  
    typedef Array_3D  dataarray_t;
    typedef LinearlyInterpolatableAxis< FloatType, Size > axis_t;
    typedef Size index_t;

    // meta methods
    /// ctor.
    NNGridData_3D
    ( const axis_t & x, const axis_t & y, const axis_t & z,
      const dataarray_t & dataarray );
    
    /// function-like interface. get value.
    ///  f(x,y,z) --> v
    FloatType operator ()
    ( const FloatType & x, const FloatType & y, const FloatType & z ) const;
    
  private:
    const axis_t & m_xaxis, m_yaxis, m_zaxis;
    const dataarray_t & m_dataarray;
  };
  
  }
} // DANSE::phonon


#include "NNGridData_3D.icc"

#endif //NNGRIDDATA_3D_H



// version
// $Id$

// End of file 
