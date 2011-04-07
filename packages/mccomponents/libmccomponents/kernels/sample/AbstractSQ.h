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
    struct AbstractSQ
    {
      virtual double operator () ( double Q ) const = 0;
      virtual ~AbstractSQ() {}
    } ;

    /// identity S(scalar Q)
    struct IdentitySQ : public AbstractSQ {
      virtual double operator() (double Q) const { return 1.; }
      virtual ~IdentitySQ() {};
    };

  } // sample::

} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SAMPLE_SQ_H

// version
// $Id$

// End of file 
