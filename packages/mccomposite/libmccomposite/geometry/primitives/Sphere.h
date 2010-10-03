// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCCOMPOSITE_GEOMETRY_PRIMITIVES_SPHERE_H
#define MCCOMPOSITE_GEOMETRY_PRIMITIVES_SPHERE_H


#include "AbstractShape.h"

namespace mccomposite{ 

  namespace geometry {
    
    //! sphere: a Shape
    /// a sphere. 
    struct Sphere : public AbstractShape {
      
      //meta methods
      Sphere( double radius );
      ~Sphere() ;
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const;
      
      //data
      double radius;
    };
    
  }

}

#endif //MCCOMPOSITE_GEOMETRY_PRIMITIVES_SPHERE_H

// version
// $Id$

// End of file 

