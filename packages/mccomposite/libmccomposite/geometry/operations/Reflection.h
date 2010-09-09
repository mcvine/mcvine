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

#ifndef MCCOMPOSITE_GEOMETRY_OPERATIONS_REFLECTION_H
#define MCCOMPOSITE_GEOMETRY_OPERATIONS_REFLECTION_H


#include "mccomposite/geometry/Vector.h"
#include "Transformation.h"


namespace mccomposite {
  
  namespace geometry {
      
    struct Reflection: public Transformation {
      
      //meta methods
      Reflection( const AbstractShape & i_body, const Vector & i_vector)
	: Transformation( i_body), vector(i_vector)
      {}
      virtual ~Reflection( ) {};
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const 
      {
	visitor.visit( this );
      }

      //data
      Vector vector;
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 
