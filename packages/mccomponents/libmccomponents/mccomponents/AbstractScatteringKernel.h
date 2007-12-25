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

  };

}



// version
// $Id$

// End of file 
