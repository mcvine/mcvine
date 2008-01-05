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

#ifndef MCCOMPOSITE_GEOMETRY_OPERATIONS_UNION_H
#define MCCOMPOSITE_GEOMETRY_OPERATIONS_UNION_H


#include "Composition.h"


namespace mccomposite {
  
  namespace geometry {
    
    struct Union: public Composition {
      
      //meta methods
      Union( const AbstractShape & shape1, const AbstractShape & shape2 )
	: Composition( shape1, shape2 )
      {}
      Union( const Composition::shapecontainer_t & shapes )
	: Composition( shapes )
      {}
      Union() 
	: Composition()
      {}
      virtual ~Union( ) {};
      
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
