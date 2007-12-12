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

#ifndef MCCOMPOSITE_ABSTRACTNEUTRONSCATTERER_H
#define MCCOMPOSITE_ABSTRACTNEUTRONSCATTERER_H


namespace mccomposite{

  // forward declaration
  namespace Neutron {
    struct Event;
  }

  struct AbstractShape;

  
  //! base class for neutron scatterers.
  /*! abstract base. define the interface of a neutron 
    scatterer interacting with neutron(s).
   */
  class AbstractNeutronScatterer: public mcni::AbstractNeutronScatterer {
  public:

    typedef mcni::AbstractNeutronScatterer base_t;
    
    // meta-methods
    inline AbstractNeutronScatterer( const AbstractShape & );
    inline virtual ~AbstractNeutronScatterer();

    // methods
    inline const AbstractShape & shape() const;

  private:
    // data
    const AbstractShape & m_shape;
  };

} // mccomposite

#include "AbstractNeutronScatterer.icc"

#endif // MCCOMPOSITE_ABSTRACTNEUTRONSCATTERER_H


// version
// $Id$

// End of file 
