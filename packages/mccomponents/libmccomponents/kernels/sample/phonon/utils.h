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


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_PHONON_UTILS_H
#define MCCOMPONENTS_KERNELS_SAMPLE_PHONON_UTILS_H

namespace mccomponents { namespace kernels { namespace phonon {

      /// randomly pick a phonon branch
      unsigned int pick_phonon_branch( size_t n_br );

      /// bose distribution 
      double phonon_bose_factor( double omega, double T );

  
}}} // mccomponents::kernels::phonon

#endif // MCCOMPONENTS_KERNELS_SAMPLE_PHONON_UTILS_H


// version
// $Id: phonon.h 250 2005-09-21 22:12:36Z linjiao $

// End of file 
