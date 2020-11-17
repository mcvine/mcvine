// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


// kernel of single crystal diffraction


#ifndef MCCOMPONENTS_KERNELS_SINGLECRYSTALDIFFRACTIONKERNEL_H
#define MCCOMPONENTS_KERNELS_SINGLECRYSTALDIFFRACTIONKERNEL_H


#include <memory>
#include "KernelBase.h"
#include "SingleCrystalDiffractionData.h"

namespace mccomponents {

  namespace kernels {

    // class SingleCrystalDiffractionKernel : public KernelBase {
    // if we choose to subclass KernelBase, two extra computations of scattering_coefficient
    // will be done when scatter is called.
    // hence, it is more efficient to subclass the most base class AbstractScatteringKernel
    class SingleCrystalDiffractionKernel: public AbstractScatteringKernel{
    public:
      // typedefs
      typedef double float_t;
      typedef mcni::Vector3<float_t> R_t;
      typedef mcni::Vector3<float_t> K_t;
      typedef mcni::Vector3<float_t> V_t;
      typedef Lattice lattice_t;
      typedef HKL hkl_t; // minimal hkl data structure
      typedef std::vector<hkl_t> hkllist_t;
      // meta methods
      //! ctor
      SingleCrystalDiffractionKernel
      (const lattice_t &lattice, const hkllist_t &hkllist,
       float_t mosaic, // radian
       float_t delta_d_d,
       float_t absorption_cross_section // barn
       );
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev );
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev );
      // virtual bool total_scattering() const {return 1;} // this kernel is special
      virtual void scatter( mcni::Neutron::Event & ev );
      virtual void absorb( mcni::Neutron::Event & ev );
    private:
      const lattice_t *m_lattice;
      const hkllist_t *m_hkllist;
      float_t m_mosaic, m_delta_d_d, m_abs_xs, m_abs_coeff;
      // impl details
      struct Details;
      std::auto_ptr<Details> m_details;

    }; // class SingleCrystalDiffractionKernel
  } // kernels::
} // mccomponents::

#endif // MCCOMPONENTS_KERNELS_SINGLECRYSTALDIFFRACTIONKERNEL_H

// End of file

