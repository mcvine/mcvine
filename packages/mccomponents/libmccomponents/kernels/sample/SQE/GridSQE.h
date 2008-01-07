// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQE_GRIDSQE_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQE_GRIDSQE_H


#include <vector>
#include "AbstractSQE.h"
#include "fxy.h"

namespace mccomponents {

  namespace sample {

    /// S(scalar Q, E )
    class GridSQE: public mccomponents::sample::AbstractSQE
    {

    public:

      // meta methods
      GridSQE ( const fxy & fxy );
      
      // methods
      virtual inline double operator () ( double Q, double E ) const
      {return m_fxy( Q, E );}


    private:
      const fxy & m_fxy;

    } ;
        
  } // Simulation::

} // DANSE::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQE_GRIDSQE_H

// version
// $Id$

// End of file 
