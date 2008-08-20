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
    class SQAdaptor: public AbstractSQ
    {
    public:

      SQAdaptor( const SQ & sq ): m_sq( sq ) 
      {}

      inline virtual double operator () ( double Q ) const
      {
	return m_sq(Q);
      }

    private:
      const SQ & m_sq;
    } ;
    
    
  } // sample::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQAdaptor_H

// version
// $Id$

// End of file 
