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

#ifndef MCCOMPONENTS_COMPOSITESCATTERINGKERNEL_H
#define MCCOMPONENTS_COMPOSITESCATTERINGKERNEL_H

#include <vector>
#include <memory>
#include "AbstractScatteringKernel.h"
#include "mccomposite/geometry/RotationMatrix.h"


namespace mccomponents{


  class CompositeScatteringKernel: public AbstractScatteringKernel {
  public:

    //types
    typedef AbstractScatteringKernel base_t;
    typedef std::vector<AbstractScatteringKernel *> kernels_t;
    typedef std::vector<double> weights_t;
    typedef mccomposite::geometry::RotationMatrix rotmat_t;
    typedef std::vector<rotmat_t> rotmats_t;
    
    // meta-methods
    // average: if set: average scattering and absorption coefficients instead of sum
    CompositeScatteringKernel 
    ( const kernels_t & kernels,
      const weights_t & weights,
      const rotmats_t & rotmats,
      bool average=0);
    virtual ~CompositeScatteringKernel();

    // methods
    virtual double absorption_coefficient( const mcni::Neutron::Event & ev ) ;
    virtual double scattering_coefficient( const mcni::Neutron::Event & ev ) ;
    virtual void scatter( mcni::Neutron::Event & ev ) ;
    virtual void absorb( mcni::Neutron::Event & ev ) ;

  private:

    // data
    const kernels_t & m_kernels;
    bool m_average;
    weights_t m_weights;
    rotmats_t m_rotmats;
    struct Details;
    std::auto_ptr<Details> m_details;
  };

} // mccomponents


#endif // MCCOMPONENTS_COMPOSITESCATTERINGKERNEL_H


// version
// $Id$

// End of file 
