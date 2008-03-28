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



#ifndef PHONON_SCATTERINGLENGTH_H
#define PHONON_SCATTERINGLENGTH_H


namespace mccomponents{

  namespace kernels{

    namespace phonon{

      template <typename complex_t, typename K_t, typename epsilon_t,
		typename atom_t, typename atoms_t,
		typename dispersion_t>
      complex_t sum_of_scattering_length
      ( const K_t & Q, 
	int branch,
	const atoms_t & atoms, 
	const dispersion_t & dispersion );

    }

  }

}


#include "scattering_length.icc"

#endif


// version
// $Id$

// End of file 

