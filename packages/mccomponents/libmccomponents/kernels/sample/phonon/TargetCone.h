// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCCOMPONENT_TARGETCONE_H
#define MCCOMPONENT_TARGETCONE_H


#include "vector3.h"

namespace mccomponents { namespace kernels {

  /// target properties for a cone
  /// TargetCone describe a target for a scattering kernel
  /// Monte-carlo simulation is a process that consumes a lot of computing resources
  /// To reduce the computing time we could limit the scattering kernel to 
  /// only scatter neutrons into a small cone instead of the full 4pi solid angles.
  /// This class describe such a cone
  ///
  struct TargetCone{
    
    // types
    typedef double float_t;
    typedef mcni::Vector3<float_t> R_t;
    
    // ctors
    TargetCone( );
    TargetCone( const R_t & direction, float_t radius );

    // data
    R_t direction;
    float_t radius;
  };

  double choose_scattering_direction(TargetCone::R_t & dir, const TargetCone & cone);
  
}} // mccomponents::kernels


#endif // MCCOMPONENT_TARGETCONE_H


// version
// $Id$

// End of file 
