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
    /// absorption coefficen
    virtual double absorption_coefficient( const mcni::Neutron::Event & ev ) = 0;
    virtual double scattering_coefficient( const mcni::Neutron::Event & ev ) = 0;
    virtual void scatter( mcni::Neutron::Event & ev ) = 0;
    virtual void absorb( mcni::Neutron::Event & ev ) = 0;

  };

}


#endif


// version
// $Id$

// End of file 
