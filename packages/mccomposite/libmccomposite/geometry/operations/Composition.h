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


#include "mccomposite/geometry/AbstractShape.h"
#include "AbstractShapeVisitor.h"

namespace mccomposite {
  
  namespace geometry {
    
    struct Composition: public AbstractShape {
      
      //meta methods
      Composition( const AbstractShape & i_body1, const AbstractShape & i_body2)
	: body1(i_body1), body2(i_body2) 
      {}
      virtual ~Composition( ) {};
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const = 0;

      //data
      const AbstractShape & body1;
      const AbstractShape & body2;
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 
