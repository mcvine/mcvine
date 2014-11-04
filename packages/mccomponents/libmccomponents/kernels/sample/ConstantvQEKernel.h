// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2014  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


// kernel that has constant energy transfer and constant 
// vector Q transfer.
// this is a trivial kernel for instrument resolution study


#ifndef MCCOMPONENTS_KERNELS_CONSTANTVQEKERNEL_H
#define MCCOMPONENTS_KERNELS_CONSTANTVQEKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {

  namespace kernels {


    class ConstantvQEKernel : public KernelBase {
    public:

      // types
      typedef double float_t;
      typedef mcni::Vector3<float_t> Q_t;
      
      // meta methods
      //! ctor
      ConstantvQEKernel
      ( double Qx, double Qy, double Qz, double E, double dE,
	double absorption_coefficient,
	double scattering_coefficient);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // data
      Q_t m_Q;
      double m_E, m_dE, m_absorption_coefficient, m_scattering_coefficient;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class ConstantvQEKernel
    
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_CONSTANTVQEKERNEL_H

// version
// $Id$

// End of file 
