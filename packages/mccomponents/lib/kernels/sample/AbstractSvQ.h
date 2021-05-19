// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SvQ_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SvQ_H

#include "mcni/geometry/Vector3.h"

namespace mccomponents {
  namespace sample {

    /// S(scalar Q)
    struct AbstractSvQ
    {
      typedef mcni::Vector3<double> V3d;
      virtual double operator () ( const V3d & Q ) = 0;
      virtual ~AbstractSvQ() {}
    } ;

    /// identity S(scalar Q)
    struct IdentitySvQ : public AbstractSvQ {
      virtual double operator() ( const V3d & Q ) { return 1.; }
      virtual ~IdentitySvQ() {};
    };

  } // sample::
} // mccomponents::

#endif // MCCOMPONENTS_KERNELS_SAMPLE_SvQ_H

// End of file
