// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2010 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

//! deal with function omega(q)-abs(Ei-Ef)
/// this function is useful for some phonon scattering kernels
/// for neutron scattering by phonons, this function represents the energy
/// conservation condition


#ifndef H_OMEGA_MINUS_DELTAE
#define H_OMEGA_MINUS_DELTAE

#include <cmath>
#include <vector>
#include <iostream>
#include "mccomponents/math/Functor.h"


// forward declarations
namespace mcni {
  template <typename NumType> class Vector3;
}
namespace DANSE{ 
  namespace phonon{
    class AbstractDispersion_3D;
  }
}


//
namespace mccomponents{ namespace kernels{ namespace phonon{

  //! functor that returns w(q) - abs(Ei-Ef)
  /// with this functor, RootFinding routines can be used to find phonons
  /// that satisfy both the energy and momentum conservation conditions
  class Omega_q_minus_deltaE: public math::Functor{
    
    typedef double float_t;
    typedef mcni::Vector3<float_t> V_t;
    typedef mcni::Vector3<float_t> K_t;
    typedef DANSE::phonon::AbstractDispersion_3D dispersion_t;
    
  public:
    //! ctor
    /// branch.......phonon branch id
    /// vf_dir.......neutron final direction
    /// vi...........neutron initial velocity vector
    /// abs_vi.......neutron initial velocity
    /// disp.........phonon dispersion
    inline Omega_q_minus_deltaE
    (int branch,
     const V_t &vf_dir, const V_t &vi,
     float_t abs_vi, const dispersion_t &disp);
    float_t evaluate(float_t vf) const;

  private:
    int _branch;
    const V_t *_vf_direction;
    const V_t *_vi;
    float_t _abs_vi;
    const dispersion_t *_disp;
  };

}}} // mccomponents::kernels::phonon


#endif // H_OMEGA_MINUS_DELTAE


// version
// $Id: Omega_minus_deltaE.h 270 2005-09-22 05:31:19Z linjiao $

// End of file 
