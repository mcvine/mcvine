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

#ifndef MCCOMPOSITE_GEOMETRY_LOCATOR_H
#define MCCOMPOSITE_GEOMETRY_LOCATOR_H

#include <iostream>
#include "mccomposite/geometry/Position.h"
#include "AbstractShapeVisitor.h"
#include "shapes.h"
#include "tolerance.h"


namespace mccomposite {
  namespace geometry {

    /// Determine if a point is inside or outside of a shape
    struct Locator: public AbstractShapeVisitor {
      
      //types
      enum Location {inside, onborder, outside};

      //meta methods
      Locator( double roundingErrorTolerance = tolerance );
      virtual ~Locator( ) {};

      //methods
      void setPoint( const Position & point );
      Location locate( const AbstractShape & s );

      //visiting methods
      // for primitives
      void visit( const Box * box );
      void visit( const Cylinder * cylinder );
      void visit( const Pyramid * pyramid );
      void visit( const Sphere * sphere );
      // for operations      // for operations
      void visit( const Difference * difference );
      void visit( const Dilation * dilation );
      void visit( const Intersection * intersection );
      void visit( const Reflection * reflection );
      void visit( const Rotation * rotation );
      void visit( const Translation * translation );
      void visit( const Union * adunion );
      
      //data
      Position point;
      Location location;
      double roundingErrorTolerance;
    };
    
  }
}

#endif


// version
// $Id$

// End of file 
