// -*- C++ -*-
// 


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_ATOMICSCATTERER_H
#define MCCOMPONENTS_KERNELS_SAMPLE_ATOMICSCATTERER_H


#include <iostream>
#include "vector3.h"


namespace mccomponents { namespace kernels {

  /// information holder for an atom in a unit cell
  struct AtomicScatterer{

    // types
    typedef double float_t;
    typedef mcni::Vector3<float_t> R_t; // type of position vector

    // meta methods

    /// ctor.
    /// Scattering properties of an atom or partial atom (atom+vacancy)
    /// or mix of atoms.
    /// Units: 
    ///   scattering length: fm (1e-15 m)
    ///   cross section: barn (1e-24 cm^2 or 1e-28m^2)
    ///   mass: atomic weight
    ///   position: angstrom
    AtomicScatterer() :
      position( R_t( 0,0,0 ) ),
      mass( 10 ),
      coherent_scattering_length( sqrt(5) ),
      coherent_cross_section( 5 )
    {}

    AtomicScatterer( const R_t & pos,
	  double m,
	  double coh_sc_len,
	  double coh_xsec) 
      :
      position( pos ),
      mass( m ),
      coherent_scattering_length( coh_sc_len ),
      coherent_cross_section( coh_xsec )
    {}	  

    // data
    R_t position; // position 
    double mass; // mass
    double coherent_scattering_length; // coherent scattering length
    double coherent_cross_section; // cross section
    
  };

}} // namespace mccomponents:kernels


std::ostream &  operator <<  ( std::ostream & os, const  mccomponents::kernels::AtomicScatterer & atom );



#endif // MCCOMPONENTS_KERNELS_SAMPLE_ATOMICSCATTERER_H
