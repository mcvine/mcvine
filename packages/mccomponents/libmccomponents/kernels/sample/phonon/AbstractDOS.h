// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                          (C) 2007  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#ifndef DANSE_PHONON_ABSTRACTDOS_H
#define DANSE_PHONON_ABSTRACTDOS_H


#include "journal/debug.h"
#include "journal/warning.h"


namespace DANSE{ namespace phonon {

  //! abstract base class for density of states
  /// The abstract base class for phonoon DOS defines
  /// the interface to the DOS data structure.
  /// Methods:
  ///   emin(), emax(): return the minimumn and maximum of 
  ///        possible phonon energies. These limits make 
  ///        it easier to compute integrations of DOS curve.
  ///   operator() (w): return value of dos at the given
  ///        energy. w is in unit of meV. The dos curve
  ///        must be normalized. If w is given out of range,
  ///        should return zero and print a warning.
  ///   value(w): implementation method. return value of
  ///        dos inside the range defined by emin and emax.
  ///        This method should not be exposed to the world.
  template <typename FLT>
  struct AbstractDOS {

    AbstractDOS( const FLT & emin, const FLT & emax ) :
      m_emin( emin ),
      m_emax( emax )
    {
      assert( emin < emax); 
    }
    
    virtual ~AbstractDOS() {}

    /// minimum of phonon energy
    FLT emin() const { return m_emin; }
    FLT emax() const { return m_emax; }

    // 
    FLT operator () ( const FLT & e ) const {
      if (e<m_emin or e> m_emax) {
#ifdef DEBUG
	journal::debug_t debug("phonon::DOS");
	debug << journal::at(__HERE__)
	      << FLT(e) << " is out of range: (" << m_emin
	      << ", " << m_emax << ")" << journal::endl;
#endif 
	return 0.0;
      }
      return value( e );
    }

  protected:
    virtual FLT value (const FLT & e) const = 0;

  private:

    FLT m_emin, m_emax;

  };

}} // DANSE::Simulation


#endif // DANSE_PHONON_ABSTRACTDOS_H

// version
// $Id$

// End of file
