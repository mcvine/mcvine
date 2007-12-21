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

#ifndef MCCOMPOSITE_COMPOSITENEUTRONSCATTERER_H
#define MCCOMPOSITE_COMPOSITENEUTRONSCATTERER_H

#include <vector>
#include "AbstractNeutronScatterer.h"


namespace mccomposite{

  //! class for composite neutron scatterers.
  /*! objects of this class are composite neutron scaterers, for example,
    sample assembly or detector system.
    A composite scatterer is a container of neutron scatterers.
    Each scatterer has a shape.
    When a neutron comes in, this composite will look for the scatterer
    that is going to be first hit by the neutron, and ask the scatterer
    to do scattering. If it is absorbed, than it is done. If it is 
    scattered, we should or should not allow multiple-scattering to
    happen. If we don't allow multiple-scattering, we will simply
    do one scattering and call it done. If we do allow multiple-scattering,
    we will need to ask the neutron to be scattered again, until either
    1. there is no scatter on the path
    2. the probability of neutron is too small
   */
  class CompositeNeutronScatterer: public AbstractNeutronScatterer {
  public:

    typedef AbstractNeutronScatterer base_t;
    typedef std::vector<AbstractNeutronScatterer *> scatterercontainer_t;
    
    // meta-methods
    CompositeNeutronScatterer
    ( const AbstractShape & shape, const scatterercontainer_t & scatterers);
    virtual ~CompositeNeutronScatterer();

    /// scatterer interacts with a neutron. 
    /// Scatterer could absorb, scatter, or do nothing to the given neutron.
    virtual InteractionType interact(mcni::Neutron::Event &ev);
    /// scatterer interacts with a neutron with the probability of
    /// multiple scattering.
    /// Scatterer could absorb, scatter, or do nothing to the given neutron.
    /// Multiple scattering is possible.
    virtual InteractionType interactM(const mcni::Neutron::Event &, mcni::Neutron::Events &);
    /// attenuate a neutron event.
    /// this method reduce the incident neutron is probability by
    /// calculating the attenuation along its path through the scatterer.
    /// Please notice that the attenuation could be due to both the absorption
    /// and the scattering.
    virtual void attenuate(mcni::Neutron::Event & );

  private:
    // data
    //all scatterers in this composite
    const scatterercontainer_t & m_scatterers;
    //shapes of all scatterers
    std::vector< const AbstractShape * > m_shapes;
  };

} // mccomposite


#endif // MCCOMPOSITE_COMPOSITENEUTRONSCATTERER_H


// version
// $Id$

// End of file 
