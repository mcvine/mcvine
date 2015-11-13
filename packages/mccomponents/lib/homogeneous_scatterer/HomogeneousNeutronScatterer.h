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

#ifndef MCCOMPONENTS_HOMOGENEOUSNEUTRONSCATTERER_H
#define MCCOMPONENTS_HOMOGENEOUSNEUTRONSCATTERER_H


#include "mccomposite/mccomposite.h"


namespace mccomponents{

  typedef mccomposite::AbstractNeutronScatterer AbstractNeutronScatterer;
  typedef mccomposite::AbstractShape AbstractShape;

  class AbstractScatteringKernel;


  //! class for homogeneous neutron scatterers.
  /*! objects of this class are homogeneous neutron scaterers, for example,
    aluminum can, ni powder sample, He3 detector tube.
    A homogeneous scatterer is a scatterer in which the scattering
    property is all the same everywhere.
   */
  class HomogeneousNeutronScatterer: public AbstractNeutronScatterer {
  public:

    // data
    static const double minimum_neutron_event_probability;
    
    // properties
    int max_scattering_loops;
    double min_neutron_probability;
    float packing_factor;

    //types
    typedef AbstractNeutronScatterer base_t;
    struct Weights {
      double absorption, scattering, transmission;
      Weights() 
	: absorption(1), scattering(1), transmission(1)
      {}
      Weights(double i_absorption, 
	      double i_scattering, 
	      double i_transmission) 
	: absorption(i_absorption), 
	  scattering(i_scattering), 
	  transmission(i_transmission)
      {}
    };
    
    // meta-methods
    HomogeneousNeutronScatterer
    ( const AbstractShape & shape, AbstractScatteringKernel & kernel,
      const Weights & weights );
    HomogeneousNeutronScatterer
    ( const AbstractShape & shape, AbstractScatteringKernel & kernel,
      const Weights & weights, double seed);
    virtual ~HomogeneousNeutronScatterer();

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
    ( const mcni::Neutron::Event &ev, const mccomposite::geometry::Position &end) const;

    virtual void print(std::ostream &os) const;

  private:
    
    // helpers
    /// helper for interactM_path1. 
    /// the only difference between this method and interactM_path1 is that 
    /// it does not propagate neutron to the surface.
    void _interactM1(const mcni::Neutron::Event &, mcni::Neutron::Events &);
    // data
    AbstractScatteringKernel & m_kernel;
    Weights m_weights;
  };


} // mccomponents


#endif // MCCOMPONENTS_HOMOGENEOUSNEUTRONSCATTERER_H


// version
// $Id$

// End of file 
