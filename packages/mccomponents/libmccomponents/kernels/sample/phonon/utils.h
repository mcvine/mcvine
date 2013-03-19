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

#include <cstring>

namespace mccomponents { namespace kernels { namespace phonon {

      /// randomly pick a phonon branch
      unsigned int pick_phonon_branch( size_t n_br );

      /// bose distribution 
      /// energy: unit meV
      /// T: unit kelvin
      /// phonon creation: e^(beta E)/(e^(beta E) - 1)
      /// phonon annhilation: 1/(e^(beta E) - 1)
      double phonon_bose_factor( double energy, double T );

  
}}} // mccomponents::kernels::phonon

#endif // MCCOMPONENTS_KERNELS_SAMPLE_PHONON_UTILS_H


// version
// $Id$

// End of file 
