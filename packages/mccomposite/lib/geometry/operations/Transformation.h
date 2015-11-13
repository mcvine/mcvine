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

#ifndef MCCOMPOSITE_GEOMETRY_TRANSFORMATION_H
#define MCCOMPOSITE_GEOMETRY_TRANSFORMATION_H


#include "AbstractShapeVisitor.h"
#include "AbstractShape.h"


namespace mccomposite {
  
  namespace geometry {
    
    struct Transformation: public AbstractShape {
      
      //meta methods
      Transformation( const AbstractShape & i_body ) 
	: body( i_body )
      {}
      virtual ~Transformation( ) {};
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const = 0;

      //data
      const AbstractShape & body;
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 

