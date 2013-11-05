// -*- C++ -*-
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                               Alex Dementsov
//                                 Jiao Lin
//                      California Institute of Technology
//                      (C) 2009-2013  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ifndef MCCOMPONENTS_KERNELS_EPSCDIFFRACTIONKERNEL_H
#define MCCOMPONENTS_KERNELS_EPSCDIFFRACTIONKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {

  namespace kernels {


    class EPSCDiffractionKernel : public KernelBase {
    public:

      // constructor
      EPSCDiffractionKernel( const EPSCDiffractionData &data);

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

    }; // class EPSCDiffractionKernel

  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_EPSCDIFFRACTIONKERNEL_H
