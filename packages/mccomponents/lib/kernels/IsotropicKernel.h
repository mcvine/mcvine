// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


// ideal isotropic kernel 
// this is a trivial kernel for test purpose

#ifndef MCCOMPONENTS_KERNELS_ISOTROPICKERNEL_H
#define MCCOMPONENTS_KERNELS_ISOTROPICKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {

  namespace kernels {


    class IsotropicKernel : public KernelBase {
    public:
      
      // meta methods
      //! ctor
      IsotropicKernel( double absorption_cross_section,
		       double scattering_cross_section);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // data
      double m_absorption_cross_section, m_scattering_cross_section;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class IsotropicKernel
    
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_ISOTROPICKERNEL_H

// version
// $Id$

// End of file 
