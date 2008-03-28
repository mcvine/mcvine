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



#ifndef PHONON_GENERATEQ_H
#define PHONON_GENERATEQ_H


#include "mccomponents/math/random.h"


namespace mccomponents{

  namespace kernels{

    namespace phonon{

      /// randomly pick a Q inside a cube in reciprocal space
      /// The center of the cube is the origin. 
      /// The size of the cube is 2*Qcutoff.
      template <typename K_t, typename float_t>
      K_t
      Q_inCube
      (const float_t & Qcutoff, 
       mccomponents::random::Generator & random_number_generator);

    }

  }

}


#include "generateQ.icc"

#endif


// version
// $Id$

// End of file 

