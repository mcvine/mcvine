// -*- C++ -*-
//


#ifndef MCCOMPONENTS_KERNELS_DGSSXRESKERNEL_H
#define MCCOMPONENTS_KERNELS_DGSSXRESKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {

  namespace kernels {

    /*
      A kernel shoots neutrons to a small region and arrive
      in a small tof window.
      This is useful for resolution calculation.
     */
    class DGSSXResKernel : public KernelBase {
    public:

      // types
      typedef double float_t;
      typedef mcni::Vector3<float_t> X_t;
      
      // meta methods
      //! ctor
      DGSSXResKernel
      ( const X_t &target_position, float_t target_radius,
	float_t tof_at_target, float_t dtof,
	double absorption_coefficient,
	double scattering_coefficient);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // data
      X_t m_target_position;
      float_t m_target_radius, m_tof_at_target, m_dtof;
      double m_absorption_coefficient, m_scattering_coefficient;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class DGSSXResKernel
    
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_DGSSXRESKERNEL_H

// End of file 
