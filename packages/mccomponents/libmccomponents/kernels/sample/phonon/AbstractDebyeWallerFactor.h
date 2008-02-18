// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 2004-2008  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#ifndef PHONON_ABSTRACTDEBYEWLLERFACTORCALCULATOR_H
#define PHONON_ABSTRACTDEBYEWLLERFACTORCALCULATOR_H


#include "vector3.h"

namespace DANSE{ namespace phonon {

  // abstract base class for Debye-Walloer factor calculator
  template <typename FloatType>
  class AbstractDebyeWallerFactorCalculator {
  public:
    // types
    typedef FloatType float_t;
    typedef mcni::Vector3<float_t> K_t;

    // meta methods
    virtual ~AbstractDebyeWallerFactorCalculator() {}

    // methods
    virtual float_t DW( const K_t & ) const = 0;
    virtual float_t DW( float_t ) const = 0;
  };
  
}} // DANSE::phonon

#endif // PHONON_ABSTRACTDEBYEWLLERFACTORCALCULATOR_H

// version
// $Id$

// End of file
