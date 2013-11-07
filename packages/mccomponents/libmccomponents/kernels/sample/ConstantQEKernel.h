// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2010  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


// isotropic kernel that has constant energy transfer and constant 
// scalar Q transfer.
// this is a trivial kernel for instrument resolution study


#ifndef MCCOMPONENTS_KERNELS_CONSTANTQEKERNEL_H
#define MCCOMPONENTS_KERNELS_CONSTANTQEKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {

  namespace kernels {


    class ConstantQEKernel : public KernelBase {
    public:
      
      // meta methods
      //! ctor
      ConstantQEKernel
      ( double Q, double E, 
	double absorption_coefficient,
	double scattering_coefficient);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // data
      double m_Q, m_E, m_absorption_coefficient, m_scattering_coefficient;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class ConstantQEKernel
    
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_CONSTANTQEKERNEL_H

// version
// $Id$

// End of file 
