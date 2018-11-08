// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//

#include "mccomposite/geometry/AbstractShapeVisitor.h"
#include "mccomposite/geometry/primitives/Cone.h"


mccomposite::geometry::Cone::Cone
( double i_radius, double i_height)
  :radius(i_radius), height(i_height)
{
}


mccomposite::geometry::Cone::~Cone
()
{
}

void mccomposite::geometry::Cone::identify( AbstractShapeVisitor & visitor ) const 
{
  visitor.visit( this );
}


// End of file 
