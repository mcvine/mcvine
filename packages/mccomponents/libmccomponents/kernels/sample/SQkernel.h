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


#ifndef MCCOMPONENTS_KERNELS_SQKERNEL_H
#define MCCOMPONENTS_KERNELS_SQKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {


  namespace sample {
    // forward declaration
    class AbstractSQ;
  }

  namespace kernels {


    /// scattering kernel of S(Q,E).
    /// S(Q,E) kernel where Q is scalar.
    class SQkernel : public KernelBase {
    public:
      
      // meta methods
      //! ctor
      SQkernel( double absorption_coefficient,
		double scattering_coefficient,
		const sample::AbstractSQ & sq, 
		double Qmin, double Qmax);
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // data
      double m_absorption_coefficient, m_scattering_coefficient;
      double m_epsilon;
      double m_Qmin, m_Qmax, m_DQ;
      const sample::AbstractSQ & m_sq;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class SQkernel
    
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SQKERNEL_H

// version
// $Id$

// End of file 
