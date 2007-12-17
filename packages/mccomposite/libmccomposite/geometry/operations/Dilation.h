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

#ifndef MCCOMPOSITE_GEOMETRY_OPERATIONS_DILATION_H
#define MCCOMPOSITE_GEOMETRY_OPERATIONS_DILATION_H


#include "Transformation.h"


namespace mccomposite {
  
  namespace geometry {
    
    struct Dilation: public Transformation {
      
      //meta methods
      Dilation( const AbstractShape & i_body, const double &i_scale)
	: Transformation(i_body), scale( i_scale )
      {}
      virtual ~Dilation( ) {}
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const 
      {
	visitor.onDilation( *this );
      }

      //data
      double scale;
    };
    
  }
  
}


#endif

// version
// $Id$

// End of file 
