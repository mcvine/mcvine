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

#ifndef MCCOMPOSITE_GEOMETRY_OPERATIONS_ROTATION_H
#define MCCOMPOSITE_GEOMETRY_OPERATIONS_ROTATION_H


#include "mccomposite/geometry/RotationMatrix.h"
#include "Transformation.h"


namespace mccomposite {
  
  namespace geometry {
    
    struct Rotation: public Transformation {
      
      //meta methods
      Rotation( const AbstractShape & i_body, const RotationMatrix & i_rotmat)
	: Transformation( i_body), rotmat(i_rotmat)
      {}
      virtual ~Rotation( ) {};
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const 
      {
	visitor.onRotation( *this );
      }

      //data
      RotationMatrix rotmat;
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 
