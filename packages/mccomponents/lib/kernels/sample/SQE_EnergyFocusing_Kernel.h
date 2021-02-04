// -*- C++ -*-
//
//


#ifndef MCCOMPONENTS_KERNELS_SQE_ENERGYFOCUSING_KERNEL_H
#define MCCOMPONENTS_KERNELS_SQE_ENERGYFOCUSING_KERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {


  namespace sample {
    // forward declaration
    class AbstractSQE;
  }

  namespace kernels {

    /// scattering kernel of S(Q,E).
    /// final energy has a focusing range
    /// S(Q,E) kernel where Q is scalar.
    class SQE_EnergyFocusing_Kernel : public KernelBase {
    public:
      // meta methods
      //! ctor
      SQE_EnergyFocusing_Kernel
      ( double absorption_cross_section,
        double scattering_cross_section,
        double unitcell_vol,
        sample::AbstractSQE & sqe, 
        double Qmin, double Qmax,
        double Emin, double Emax,
        double Ef, double dEf
        ) ;
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
    private:
      // data
      double m_absorption_cross_section, m_scattering_cross_section;
      double m_uc_vol;
      double m_epsilon;
      double m_Qmin, m_Qmax, m_DQ;
      double m_Emin, m_Emax, m_DE;
      double m_Ef, m_dEf;
      sample::AbstractSQE & m_sqe;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class SQE_EnergyFocusing_Kernel
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SQE_ENERGYFOCUSING_KERNEL_H

// End of file 
