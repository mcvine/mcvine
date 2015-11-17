// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCCOMPOSITE_GEOMETRY_PRIMITIVES_BOX_H
#define MCCOMPOSITE_GEOMETRY_PRIMITIVES_BOX_H


#include "AbstractShape.h"

namespace mccomposite{ 

  namespace geometry{

    //! box: a Shape
    struct Box : public AbstractShape {
      
      // meta-methods
      Box( double edgeX, double edgeY, double edgeZ);
      ~Box();
      
      //methods
      virtual void identify( AbstractShapeVisitor & visitor ) const;

      // data
      double edgeX, edgeY, edgeZ;
    };

  }

}


#endif //MCCOMPOSITE_GEOMETRY_PRIMITIVES_BOX_H

// version
// $Id$

// End of file 
