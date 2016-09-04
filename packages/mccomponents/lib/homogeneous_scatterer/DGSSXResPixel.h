// -*- C++ -*-
//
//

#ifndef MCCOMPONENTS_DGSSXRESPIXEL_H
#define MCCOMPONENTS_DGSSXRESPIXEL_H


#include "mccomposite/mccomposite.h"

namespace mccomponents{

  typedef mccomposite::AbstractNeutronScatterer AbstractNeutronScatterer;
  typedef mccomposite::AbstractShape AbstractShape;

  class AbstractScatteringKernel;


  //! specialized scatterer for resolution calculation
  class DGSSXResPixel: public AbstractNeutronScatterer {
  public:

    typedef AbstractNeutronScatterer base_t;
    
    // meta-methods
    DGSSXResPixel
    (double tof, double pressure,
     const AbstractShape & shape);
    virtual ~DGSSXResPixel();

    virtual InteractionType interact_path1(mcni::Neutron::Event &ev);
    virtual InteractionType interactM_path1(const mcni::Neutron::Event &, mcni::Neutron::Events &);

    virtual void print(std::ostream &os) const;

  private:
    
    // data
    double m_tof;
    // AbstractScatteringKernel & m_kernel;
    class Kernel;
    std::auto_ptr<Kernel> m_kernel;
  };


} // mccomponents


#endif // MCCOMPONENTS_DGSSXRESPIXEL_H


// End of file 
