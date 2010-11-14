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


#ifndef MCCOMPONENTS_ABSTRACTSCATTERINGKERNEL_H
#define MCCOMPONENTS_ABSTRACTSCATTERINGKERNEL_H


#include "mcni/neutron.h"

namespace mccomponents {

  class AbstractScatteringKernel {

  public:

    // meta methods
    virtual ~AbstractScatteringKernel() {};

    // methods
    /// absorption coefficent
    /// calculates the absorption coefficient for the given neutron event
    /// unit: 1/meter
    virtual double absorption_coefficient( const mcni::Neutron::Event & ev ) = 0;
    /// scattering coefficient
    /// calculates the scattering coefficient for the given neutron event
    /// unit: 1/meter
    virtual double scattering_coefficient( const mcni::Neutron::Event & ev ) = 0;
    
    /// scatter the given neutron
    /// note: 
    ///  - probability: should adjust the probability of the neutron
    ///                 event depending on the direction of scattering.
    ///                 The scattering coefficient is already considered in
    ///                 HomogeneousNeutronScatterer, so here we are only
    ///                 concerned with directional distribution of neutron events.
    virtual void scatter( mcni::Neutron::Event & ev ) = 0;

    /// absorb the neutron
    virtual void absorb( mcni::Neutron::Event & ev ) = 0;

  };

}


#endif


// version
// $Id$

// End of file 
