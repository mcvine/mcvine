// -*- C++ -*-
//
// Li Li
// Jiao Lin
//


// kernel of simple powder diffraction


#ifndef MCCOMPONENTS_KERNELS_SIMPLEPOWDERDIFFRACTIONKERNEL_H
#define MCCOMPONENTS_KERNELS_SIMPLEPOWDERDIFFRACTIONKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {

  namespace kernels {

    class SimplePowderDiffractionData;
    
    class SimplePowderDiffractionKernel : public KernelBase {
    public:
      
      // typedefs
      typedef double float_t;
      typedef mcni::Vector3<float_t> R_t;
      typedef mcni::Vector3<float_t> K_t;
      typedef mcni::Vector3<float_t> V_t;
      
      // meta methods
      //! ctor
      SimplePowderDiffractionKernel
      ( const SimplePowderDiffractionData &data, double d_phi=0);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;
      double m_d_phi;

    }; // class SimplePowderDiffractionKernel
    
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SIMPLEPOWDERDIFFRACTIONKERNEL_H

// version
// $Id$

// End of file 

