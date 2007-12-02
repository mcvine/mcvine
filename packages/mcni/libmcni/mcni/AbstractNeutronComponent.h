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

#ifndef MCNI_ABSTRACTNEUTRONCOMPONENT_H
#define MCNI_ABSTRACTNEUTRONCOMPONENT_H

#include <string>
#include "AbstractNeutronScatterer.h"

namespace mcni{

  //! base class for neutron components.
  /*! abstract base. define the interface of a neutron component 
    interacting with neutron(s).
   */
  class AbstractNeutronComponent: public AbstractNeutronScatterer {
  public:

    // meta-methods
    AbstractNeutronComponent( const char * i_name ) : name(i_name) {}
    virtual ~AbstractNeutronComponent() {}

    // data
    std::string name;
  };


} // mcni

#endif // MCNI_ABSTRACTNEUTRONCOMPONENT_H


// version
// $Id$

// End of file 
