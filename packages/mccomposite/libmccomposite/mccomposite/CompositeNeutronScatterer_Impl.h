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



#ifndef MCCOMPOSITE_COMPOSITENEUTRONSCATTERER_IMPL_H
#define MCCOMPOSITE_COMPOSITENEUTRONSCATTERER_IMPL_H

#include <vector>
#include "AbstractNeutronScatterer.h"
#include "Geometer.h"
#include "geometry/operations/Union.h"


namespace mccomposite{
  
  /// implementation class of CompositeNeutronScatterer. almost all methods
  /// directly comes from CompositeNeutronScatterer.
  struct CompositeNeutronScatterer_Impl{

    // types
    typedef AbstractNeutronScatterer scatterer_interface;
    typedef scatterer_interface::InteractionType InteractionType;
    typedef Geometer<AbstractNeutronScatterer> geometer_t;
    typedef std::vector<AbstractNeutronScatterer *> scatterercontainer_t;
    
    // meta-methods
    CompositeNeutronScatterer_Impl
    ( const AbstractShape & shape, const scatterercontainer_t & scatterers, 
      const geometer_t & geometer);
    ~CompositeNeutronScatterer_Impl();
    
    void scatter(mcni::Neutron::Event &);
    void scatterM(const mcni::Neutron::Event &, mcni::Neutron::Events &);
    InteractionType interact_path1(mcni::Neutron::Event &ev);
    InteractionType interactM_path1(const mcni::Neutron::Event &, mcni::Neutron::Events &);
    
    double calculate_attenuation
    ( const mcni::Neutron::Event &ev, const geometry::Position &end);
    
    // data
    const AbstractShape &m_shape;
    const scatterercontainer_t & m_scatterers;
    std::vector< const AbstractShape * > m_shapes;
    geometry::Union m_union_of_all_shapes;
    geometer_t m_geometer;
    struct Details;
    std::auto_ptr<Details> m_details;
    
  };
  
} // mccomposite


#endif // MCCOMPOSITE_COMPOSITENEUTRONSCATTERER_IMPL_H


// version
// $Id$

// End of file 
