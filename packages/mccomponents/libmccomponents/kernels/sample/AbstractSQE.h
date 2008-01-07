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


#ifndef MCCOMPONENTS_KERNELS_SAMPLE_SQE_H
#define MCCOMPONENTS_KERNELS_SAMPLE_SQE_H


namespace mccomponents {

  namespace sample {
    
    /// S(scalar Q, E )
    class AbstractSQE
    {
    public:
      
      virtual double operator () ( double Q, double E ) const = 0;
      virtual ~AbstractSQE() {}
    } ;
    
    
  } // sample::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQE_H

// version
// $Id$

// End of file 
