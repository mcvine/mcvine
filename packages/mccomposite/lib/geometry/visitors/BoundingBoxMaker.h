// -*- C++ -*-
//
//

#ifndef MCCOMPOSITE_GEOMETRY_BOUNDINGBOX_MAKER_H
#define MCCOMPOSITE_GEOMETRY_BOUNDINGBOX_MAKER_H

#include <iostream>
#include "AbstractShapeVisitor.h"
#include "shapes.h"
#include "../BoundingBox.h"


namespace mccomposite {
  namespace geometry {

    struct BoundingBoxMaker: public AbstractShapeVisitor {
      
      //meta methods
      BoundingBoxMaker();
      virtual ~BoundingBoxMaker() {};

      //methods
      BoundingBox make( const AbstractShape & s );

      //visiting methods
      // for primitives
      void visit( const Box * box );
      void visit( const Cylinder * cylinder );
      void visit( const Pyramid * pyramid );
      void visit( const Cone * cone );
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
      BoundingBox bb;
    };
    
  }
}

#endif


// version
// $Id$

// End of file 
