// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//

#include "mccomposite/geometry/AbstractShapeVisitor.h"
#include "mccomposite/geometry/primitives/Pyramid.h"


mccomposite::geometry::Pyramid::Pyramid
( double i_edgeX, double i_edgeY, double i_height)
  :edgeX(i_edgeX), edgeY(i_edgeY), height(i_height)
{
}


mccomposite::geometry::Pyramid::~Pyramid
()
{
}

void mccomposite::geometry::Pyramid::identify( AbstractShapeVisitor & visitor ) const 
{
  visitor.visit( this );
}


// End of file 
