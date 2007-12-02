// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef MCNI_ABSTRACTNEUTRONSCATTERER_H
#define MCNI_ABSTRACTNEUTRONSCATTERER_H


namespace mcni{

  // forward declaration
  namespace Neutron {
    struct Event;
  }

  //! base class for neutron scatterers.
  /*! abstract base. define the interface of a neutron 
    scatterer interacting with neutron(s).
   */
  class AbstractNeutronScatterer {
  public:

    // meta-methods
    virtual ~AbstractNeutronScatterer() {}

    // methods
    // interactions with neutron
    /// absorb a neutron.
    virtual void absorb(Neutron::Event &);
    /// scatter a neutron
    virtual void scatter(Neutron::Event &) = 0;
  };


  // convenient methods
  void inline absorb( Neutron::Event &);
  bool inline invalid( const Neutron::Event & );

} // mcni

#include "AbstractNeutronScatterer.icc"

#endif // MCNI_ABSTRACTNEUTRONSCATTERER_H


// version
// $Id$

// End of file 
