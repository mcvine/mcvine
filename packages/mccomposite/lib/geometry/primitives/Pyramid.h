// -*- C++ -*-
//
//


#ifndef MCCOMPOSITE_GEOMETRY_PRIMITIVES_PYRAMID_H
#define MCCOMPOSITE_GEOMETRY_PRIMITIVES_PYRAMID_H


#include "AbstractShape.h"

namespace mccomposite{ namespace geometry {
    
    //! pyramid: a Shape
    /// a pyramid. its axis is along z direction
    /// its base is on the xy plane at z=0
    /// edgeX and edgeY are its dimensions at x and y directions
    struct Pyramid : public AbstractShape {
      
      //meta methods
      Pyramid( double edgeX, double edgeY, double height);
      ~Pyramid() ;
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const;
      
      //data
      double edgeX, edgeY, height;
    };
    
  }
}

#endif //MCCOMPOSITE_GEOMETRY_PRIMITIVES_PYRAMID_H

// End of file 

