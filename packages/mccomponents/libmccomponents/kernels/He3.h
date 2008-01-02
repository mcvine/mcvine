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


#ifndef MCCOMPONENTS_KERNELS_HE3_H
#define MCCOMPONENTS_KERNELS_HE3_H

#include "AbstractScatteringKernel.h"


namespace mccomponents {

  namespace kernels {

    /// base class from He3 related kernel
    class He3: public AbstractScatteringKernel {

    public:

      // meta methods
      /// ctor
      /// pressure: pascal
      He3( double pressure );

      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void scatter( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev ) = 0;

    
    private:
      // data
      /// pressure
      double m_pressure;
    
      /// absorption x-section of He3 in cm^2 at ref. wavelength (actual
      /// number stored is divided by ref wavelength for convenience)
      double m_refAbsXS;
      double m_refWavelength;
    
      /// Number density of He3. Computed from pressure
      double m_N;
    };

  } // kernels::

} // mccomponents::


#endif


// version
// $Id$

// End of file 
