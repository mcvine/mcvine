// -*- C++ -*-
//
//


#ifndef MCCOMPONENTS_KERNELS_SANSSPHERESKERNEL_H
#define MCCOMPONENTS_KERNELS_SANSSPHERESKERNEL_H

#include <memory>
#include "KernelBase.h"

namespace mccomponents {

  namespace kernels {

    class SANSSpheresKernel : public KernelBase {
    public:
      // types
      typedef double float_t;
      typedef mcni::Vector3<float_t> X_t;
      typedef mcni::Vector3<float_t> K_t;
      // meta methods
      //! ctor
      SANSSpheresKernel
      (float_t absorption_coefficient,
       float_t R, // AA
       float_t phi,
       float_t delta_rho, // fm/AA^3
       float_t max_angle // degree
       );
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
    private:
      // data
      float_t m_absorption_coefficient;
      float_t m_R, m_phi, m_delta_rho;
      float_t m_max_angle; // radian
      float_t m_max_angle_tan;
      float_t m_solidangle;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;
    }; // class SANSSpheresKernel
  } // kernels::
} // mccomponents::

#endif // MCCOMPONENTS_KERNELS_SANSSPHERESKERNEL_H

// End of file
