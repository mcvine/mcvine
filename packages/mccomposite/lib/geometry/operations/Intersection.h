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

#ifndef MCCOMPOSITE_GEOMETRY_OPERATIONS_INTERSECTION_H
#define MCCOMPOSITE_GEOMETRY_OPERATIONS_INTERSECTION_H


#include "Composition.h"


namespace mccomposite {
  
  namespace geometry {
    
    struct Intersection: public Composition {
      
      //meta methods
      Intersection( const AbstractShape & shape1, const AbstractShape & shape2 )
	: Composition( shape1, shape2 )
      {}
      Intersection( const Composition::shapecontainer_t & shapes )
	: Composition( shapes )
      {}
      virtual ~Intersection( ) {};
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const 
      {
	visitor.visit( this );
      }
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 
