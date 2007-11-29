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
  /*! abstract base. define the interface of a neutron scatterer with neutron(s).
   */
  class AbstractNeutronScatterer {
  public:

    // meta-methods
    virtual ~AbstractNeutronScatterer() {}

    // methods
    // interactions with neutron
    /// absorb a neutron.
    virtual inline void absorb(Neutron::Event &) const;
    /// scatter a neutron
    virtual void scatter(Neutron::Event &) const = 0;
    /// scatter a neutron
    /// method for a neutron component that will change its own state when doing
    /// scattering. this is more useful for detectors.
    virtual inline void scatter(Neutron::Event &);
  };


  // convenient methods
  void inline absorb( Neutron::Event &);
  bool inline invalid( const Neutron::Event & );

} // mcni

#include "AbstractNeutronScatterer.icc"

#endif // MCNI_ABSTRACTNEUTRONSCATTERER_H


// version
// $Id: AbstractNeutronScatterer.h 591 2006-09-25 07:17:26Z linjiao $

// End of file 
