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
// $Id: Sphere.h 505 2006-04-10 06:13:56Z jiao $

// End of file 

