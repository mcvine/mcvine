// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#ifndef MCCOMPONENTS_KERNELS_SVQKERNEL_H
#define MCCOMPONENTS_KERNELS_SVQKERNEL_H


#include <memory>
#include "KernelBase.h"


namespace mccomponents {


  namespace sample {
    // forward declaration
    class AbstractSvQ;
  }

  namespace kernels {


    /// S(Q) kernel where Q is vector.
    class SvQkernel : public KernelBase {
    public:

      // meta methods
      //! ctor
      SvQkernel( double absorption_coefficient,
                 double scattering_coefficient,
                 sample::AbstractSvQ & sq);

      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      virtual void S( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );

    private:
      // data
      double m_absorption_coefficient, m_scattering_coefficient;
      double m_epsilon;
      sample::AbstractSvQ & m_sq;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class SvQkernel
  } // kernels::
} // mccomponents::

#endif // MCCOMPONENTS_KERNELS_SVQKERNEL_H

// End of file
