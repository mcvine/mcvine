// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2008  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQAdaptor_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQAdaptor_H

#include "AbstractSQ.h"

namespace mccomponents {

  namespace sample {

    // convert an object any class that has a operator()(Q) to an instance
    // acceptable by SQkernel
    template <typename SQ>
    struct SQAdaptor: public AbstractSQ
    {
      SQAdaptor( const SQ & sq ): core( sq ) 
      {}

      inline virtual double operator () ( double Q ) const
      {
	return core(Q);
      }

      inline virtual double operator () ( double Q )
      {
	return core(Q);
      }

      const SQ & core;
    } ;
    
    
  } // sample::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQAdaptor_H

// version
// $Id$

// End of file 
