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

#ifndef MCCOMPOSITE_GEOMETRY_OPERATIONS_COMPOSITION_H
#define MCCOMPOSITE_GEOMETRY_OPERATIONS_COMPOSITION_H

#include <vector>
#include "mccomposite/geometry/AbstractShape.h"
#include "AbstractShapeVisitor.h"

namespace mccomposite {
  
  namespace geometry {
    
    struct Composition: public AbstractShape {
      //types
      typedef std::vector<const AbstractShape *> shapecontainer_t;

      //meta methods
      ///ctor.
      ///general ctor that take a list of shapes
      Composition( const shapecontainer_t & i_shapes)
	: shapes(i_shapes)
      {}
      Composition( const AbstractShape & shape1, const AbstractShape & shape2)
      {
	shapes.push_back( &shape1 );
	shapes.push_back( &shape2 );
      }
      virtual ~Composition( ) {};
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const = 0;

      //data
      shapecontainer_t shapes;
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 
