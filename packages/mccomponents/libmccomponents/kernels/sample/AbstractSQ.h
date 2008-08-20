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


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQ_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQ_H


namespace mccomponents {

  namespace sample {
    
    /// S(scalar Q)
    class AbstractSQ
    {
    public:
      
      virtual double operator () ( double Q ) const = 0;
      virtual ~AbstractSQ() {}
    } ;
    
    
  } // sample::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQ_H

// version
// $Id$

// End of file 
