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

#ifndef DANSE_PHONON_DWFROMDOS_H
#define DANSE_PHONON_DWFROMDOS_H


#include "mcni/geometry/Vector3.h"

#include "AbstractDebyeWallerFactor.h"
#include "AbstractDOS.h"


namespace DANSE{ namespace phonon {
  
  //! calculate Debye-Waller factor from give density of states
  template <typename FloatType>
  class DWFromDOS : public AbstractDebyeWallerFactorCalculator<FloatType> {
  public:

    // types
    typedef FloatType float_t;
    typedef AbstractDOS<float_t> dos_t;
    typedef mcni::Vector3<float_t> K_t;

    // ctor
    DWFromDOS( const dos_t & dos, size_t nSample = 100) 
      : m_dos(dos), m_nSample(nSample) {}
    
    // calculate the core
    void calc_DW_core( float_t atom_mass, float_t temperatureInK);

    // report the value of core
    float_t core() const { return m_core; }

    // calculate and return the Debye Waller factor
    float_t DW( const K_t & Q_vec) const;
    float_t DW( float_t Q_mag) const ;

  private:
    
    // data
    const dos_t &m_dos;
    float_t m_core;
    size_t m_nSample; // number of sampling points
  };

}}

#include "DWFromDOS.icc"

#endif // DANSE_PHONON_DWFROMDOS_H

// version
// $Id: DWFromDOS.h 635 2007-08-02 20:12:47Z linjiao $

// End of file
