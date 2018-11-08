// -*- C++ -*-
//
//


#ifndef MCCOMPOSITE_GEOMETRY_PRIMITIVES_CONE_H
#define MCCOMPOSITE_GEOMETRY_PRIMITIVES_CONE_H


#include "AbstractShape.h"

namespace mccomposite{ namespace geometry {
    
    //! cone: a Shape
    /// a cone. its axis is along z direction
    /// its tip is at the origin. its base is at negative z
    struct Cone : public AbstractShape {
      
      //meta methods
      Cone( double radius, double height);
      ~Cone() ;
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const;
      
      //data
      double radius, height;
    };
    
  }
}

#endif //MCCOMPOSITE_GEOMETRY_PRIMITIVES_CONE_H

// End of file 

