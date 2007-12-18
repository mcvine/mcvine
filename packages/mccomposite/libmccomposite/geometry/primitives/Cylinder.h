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


#ifndef MCCOMPOSITE_GEOMETRY_PRIMITIVES_CYLINDER_H
#define MCCOMPOSITE_GEOMETRY_PRIMITIVES_CYLINDER_H


#include "AbstractShape.h"

namespace mccomposite{ namespace geometry {
    
    //! cylinder: a Shape
    /// a cylinder. its axis is along z direction
    struct Cylinder : public AbstractShape {
      
      //meta methods
      Cylinder( double radius, double height);
      ~Cylinder() ;
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const;
      
      //data
      double radius, height;
    };
    
  }
}

#endif //MCCOMPOSITE_GEOMETRY_PRIMITIVES_CYLINDER_H

// version
// $Id: Cylinder.h 505 2006-04-10 06:13:56Z jiao $

// End of file 

