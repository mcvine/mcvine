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
#include <memory>

#include "AbstractNeutronScatterer.h"
#include "Geometer.h"


namespace mccomposite{


  struct CompositeNeutronScatterer_Impl;

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

    //types
    typedef AbstractNeutronScatterer base_t;
    typedef std::vector<AbstractNeutronScatterer *> scatterercontainer_t;
    typedef Geometer<AbstractNeutronScatterer> geometer_t;
    
    // meta-methods
    CompositeNeutronScatterer
    ( const AbstractShape & shape, const scatterercontainer_t & scatterers, const geometer_t & geometer);
    virtual ~CompositeNeutronScatterer();

    /// override method scatter of base class AbstractNeutronScatterer
    virtual void scatter(mcni::Neutron::Event &);
    /// override method scatterM of base class AbstractNeutronScatterer
    virtual void scatterM(const mcni::Neutron::Event &, mcni::Neutron::Events &);

    /// scatterer interacts with a neutron in its first section of continuous path thru the scatterer.
    /// for most scatterer, a neutron will pass it in one continuous path.
    /// but sometimes a scatterer will be passed in more than one paths.
    /// Think about a hollow cylinder, for example.
    /// This method calculates the interaction between a neutron and the
    /// scatterer in the first path.
    virtual InteractionType interact_path1(mcni::Neutron::Event &ev);
    /// scatterer interacts with a neutron and possibly create a lot of neutrons
    /// in its first continous path through this scatterer.
    /// This is the multiple-scattering version of interact_path1.
    /// The default implementation just does single-scattering.
    virtual InteractionType interactM_path1(const mcni::Neutron::Event &, mcni::Neutron::Events &);

    /// calculate attenuation of a neutron event that will done by this scatterer.
    /// this method calculates the attenuation along its path.
    /// Please notice that the attenuation could be due to both the absorption
    /// and the scattering.
    virtual double calculate_attenuation
    ( const mcni::Neutron::Event &ev, const geometry::Position &end);

    virtual void set_max_multiplescattering_loops_among_scatterers(unsigned int N);

    virtual void print(std::ostream &os) const;

  private:

    std::auto_ptr<CompositeNeutronScatterer_Impl> m_impl;

  };

} // mccomposite


#endif // MCCOMPOSITE_COMPOSITENEUTRONSCATTERER_H


// version
// $Id$

// End of file 
