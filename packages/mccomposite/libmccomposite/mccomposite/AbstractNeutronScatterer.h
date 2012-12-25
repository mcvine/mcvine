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

#include <memory>
#include "mcni/neutron.h"
#include "mcni/AbstractNeutronScatterer.h"
#include "mccomposite/geometry/AbstractShape.h"
#include "mccomposite/geometry/Position.h"

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

    /// scatterer interacts with a neutron in its first section of continuous path thru the scatterer.
    /// for most scatterer, a neutron will pass it in one continuous path.
    /// but sometimes a scatterer will be passed in more than one paths.
    /// Think about a hollow cylinder, for example.
    /// This method calculates the interaction between a neutron and the
    /// scatterer in the first path.
    /// Note: neutron must be propagated out to the first out-surface it intersects.
    virtual InteractionType interact_path1(mcni::Neutron::Event &ev) = 0;
    /// scatterer interacts with a neutron and possibly create a lot of neutrons
    /// in its first continous path through this scatterer.
    /// This is the multiple-scattering version of interact_path1.
    /// The default implementation just does single-scattering.
    virtual InteractionType interactM_path1(const mcni::Neutron::Event &, mcni::Neutron::Events &);

    ///calculate attenuation of a neutron done by this scatterer.
    ///The neutron event is given, and also the end point of the neutron would go.
    ///The end point must be on the path where the neutron event is flying.
    virtual double calculate_attenuation
    ( const mcni::Neutron::Event &ev, const geometry::Position & end ) const;

    /// my shape
    const AbstractShape & shape() const;
    
    virtual void print(std::ostream &os) const;
    
  private:
    // data
    const AbstractShape & m_shape;
    // 
    struct Details;
    std::auto_ptr< Details > m_details;
  };

} // mccomposite

std::ostream & operator<< (std::ostream &os, const mccomposite::AbstractNeutronScatterer & scatterer);
  

#include "AbstractNeutronScatterer.icc"

#endif // MCCOMPOSITE_ABSTRACTNEUTRONSCATTERER_H


// version
// $Id$

// End of file 
