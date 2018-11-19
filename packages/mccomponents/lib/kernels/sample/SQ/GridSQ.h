// -*- C++ -*-
//
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQ_GRIDSQ_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQ_GRIDSQ_H


#include <vector>
#include "AbstractSQ.h"
#include "fx.h"

namespace mccomponents {

  namespace sample {

    /// S(scalar Q)
    class GridSQ: public mccomponents::sample::AbstractSQ
    {

    public:

      // meta methods
      GridSQ ( const fx & fx );
      
      // methods
      virtual inline double operator () ( double Q ) const
      {return m_fx( Q );}

      virtual inline double operator () ( double Q ) 
      {return m_fx( Q );}

    private:
      const fx & m_fx;

    } ;
        
  } // Simulation::

} // DANSE::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQ_GRIDSQ_H

// End of file 
