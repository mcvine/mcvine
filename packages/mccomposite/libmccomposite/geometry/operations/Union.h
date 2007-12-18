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
      Union( const AbstractShape & body1, const AbstractShape & body2 )
	: Composition( body1, body2 )
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
