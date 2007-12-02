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

#ifndef MCNI_DUMMYCOMPONENT_H
#define MCNI_DUMMYCOMPONENT_H


#include "AbstractNeutronComponent.h"

namespace mcni{

  //! base class for neutron components.
  /*! abstract base. define the interface of a neutron component 
    interacting with neutron(s).
   */
  class DummyComponent: public AbstractNeutronComponent {
  public:

    // meta-methods
    DummyComponent( const char *name) : AbstractNeutronComponent(name) {}
    virtual ~DummyComponent() {}

    // methods
    virtual void scatter(Neutron::Event &) {}
  };


} // mcni

#endif // MCNI_DUMMYCOMPONENT_H


// version
// $Id$

// End of file 
