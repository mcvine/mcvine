// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 2004-2007  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#ifndef DANSE_PHONON_LINEARLYINTERPOLATEDDOS_H
#define DANSE_PHONON_LINEARLYINTERPOLATEDDOS_H


#include <memory>

#include "exception.h"
#include "AbstractDOS.h"


namespace DANSE{ namespace phonon {

    class DOS_Init_Error: public Exception {
    public:
      DOS_Init_Error() : Exception( "DOS initialization error" ) {}
    };
    
    //! density of states
    /// This is an implementation of density of states interface
    /// defined in AbstractDOS.
    ///
    /// It is implemented by interpolating
    /// a histogram of DOS.
    ///
    /// Methods:
    ///  Constructor: takes one array of Z and (start, step, n) of E bin centers.
    /// normalization is
    ///     done here.
    ///  value (): use interpolation to calculate value of dos.
    ///  Other methods: for backward compatibility. should be 
    ///     moved to private section.
    template <typename FLT, typename Array_1D>
    class LinearlyInterpolatedDOS : public AbstractDOS<FLT>
    {

    public:
      // typedefs
      typedef Array_1D array_t;
      typedef FLT float_t;
      typedef AbstractDOS<FLT> base_t;
      typedef unsigned int index_t;
      typedef LinearlyInterpolatedDOS<FLT, Array_1D> this_t;

      // meta methods
      LinearlyInterpolatedDOS
      ( float_t e0, float_t de, index_t ne, const array_t &Z) ;
      ~LinearlyInterpolatedDOS();

      // methods
      FLT value( const FLT & e ) const;

    private:
      // data
      struct Details;
      std::auto_ptr< Details > m_details;
      array_t m_Z;
      float_t m_e0, m_de, m_n, m_e1;
    };

}} // DANSE::phonon




#include "LinearlyInterpolatedDOS.icc"

#endif // DANSE_PHONON_LINEARLYINTERPOLATEDDOS_H

// version
// $Id$

// End of file
