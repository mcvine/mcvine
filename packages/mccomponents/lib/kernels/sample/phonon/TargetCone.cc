// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include "mcni/math/number.h"
#include "mccomponents/math/random/geometry.h"
#include "mccomponents/kernels/sample/phonon/TargetCone.h"


namespace mccomponents { namespace kernels {


  TargetCone::TargetCone()
    : direction( 0,0,0 ), radius( -1 )
  {
  }

  TargetCone::TargetCone( const R_t & dir, float_t r )
    : direction(dir), radius(r)
  {
  }


  double choose_scattering_direction
  (TargetCone::R_t & dir, const TargetCone & target_props)
  {
    if ( target_props.radius <= 0 ) {
      math::choose_direction( dir );
      return 4*mcni::PI;
    } else {
      return math::choose_direction( dir, target_props.direction, target_props.radius);
    }
  }

}} // mccomponents::kernels


// version
// $Id$

// End of file 
