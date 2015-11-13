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
    virtual bool total_scattering() const {return 0;}
    
    /// scatter the given neutron
    /// note: 
    ///  - probability: 
    ///    should adjust the probability of the neutron
    ///    event depending on the direction of scattering.
    ///    The scattering coefficient is already considered in
    ///    HomogeneousNeutronScatterer, so here we are only
    ///    concerned with directional distribution of
    ///    neutron events.
    ///    make sure that the avaraged value of probablility
    ///    factor applied in this method is consistent with
    ///    the scattering_coefficient method.
    ///    For example, in case of incoherent scattering, if method
    ///    scattering_coefficient returns \sigma_inc * \rho ,
    ///    where \rho is the density (# of nuclei per unit volume),
    ///    then in the scatter method here, the average probability
    ///    factor applied should be 1.
    virtual void scatter( mcni::Neutron::Event & ev ) = 0;

    /// absorb the neutron
    virtual void absorb( mcni::Neutron::Event & ev ) = 0;
  };

}


#endif


// version
// $Id$

// End of file 
