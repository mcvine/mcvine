// -*- C++ -*-
//
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQ_GRIDSvQ_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQ_GRIDSvQ_H


#include <vector>
#include "AbstractSvQ.h"
#include "fxyz.h"

namespace mccomponents {

  namespace sample {

    /// S(scalar Q)
    class GridSvQ: public mccomponents::sample::AbstractSvQ
    {

    public:

      // meta methods
      GridSvQ ( const fxyz & fxyz );

      // methods
      virtual inline double operator () (const V3d & Q ) const
      {return m_fxyz( Q.x, Q.y, Q.z );}

      virtual inline double operator () (const V3d & Q )
      {return m_fxyz( Q.x, Q.y, Q.z );}

    private:
      const fxyz & m_fxyz;

    } ;

  } // Simulation::

} // DANSE::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQ_GRIDSvQ_H

// End of file
