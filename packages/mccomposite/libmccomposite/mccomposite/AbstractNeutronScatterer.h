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

#include "mcni/neutron.h"
#include "mcni/AbstractNeutronScatterer.h"
#include "mccomposite/geometry/AbstractShape.h"

namespace mccomposite{
  
  using geometry::AbstractShape;
  
  //! base class for neutron scatterers.
  /*! abstract base. define the interface of a neutron 
    scatterer interacting with neutron(s).
    This scatterer class is different from mcni::AbstractNeutronScatterer
    in that it must have a shape.
    Another difference is that this class delegates "scatter" methods to
    "interact" methods.
    "interact" methods return the type of interaction. It could be one
    of the following:
    - absorption: neutron is absorbed
    - scatter: neutron is scattered
    - none: no interaction
    This class also has an additional method, "attenuate", to calcualte
    attenuation solely. This is useful for simulating the single-scattering 
    case.
  */
  class AbstractNeutronScatterer: public mcni::AbstractNeutronScatterer {
  public:
    //types
    typedef mcni::AbstractNeutronScatterer base_t;
    enum InteractionType {absorption, scattering, none};
    
    // meta-methods
    AbstractNeutronScatterer( const AbstractShape & );
    virtual ~AbstractNeutronScatterer();
    
    // methods
    virtual void scatter(mcni::Neutron::Event &);
    virtual void scatterM(const mcni::Neutron::Event &, mcni::Neutron::Events &);
    /// scatterer interacts with a neutron. 
    /// Scatterer could absorb, scatter, or do nothing to the given neutron.
    /// note: neutron must be propagate out of the scatterer!
    virtual InteractionType interact(mcni::Neutron::Event &ev) = 0;
    /// scatterer interacts with a neutron with the probability of
    /// multiple scattering.
    /// Scatterer could absorb, scatter, or do nothing to the given neutron.
    /// Multiple scattering is possible.
    /// note: neutrons must be propagate out of the scatterer!
    virtual InteractionType interactM(const mcni::Neutron::Event &, mcni::Neutron::Events &);
    /// attenuate a neutron event.
    /// this method reduce the incident neutron is probability by
    /// calculating the attenuation along its path through the scatterer.
    /// Please notice that the attenuation could be due to both the absorption
    /// and the scattering.
    /// note: neutron must be propagated out of the scatterer!
    virtual void attenuate(mcni::Neutron::Event & );
    const AbstractShape & shape() const;
    
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
