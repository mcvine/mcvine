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

#include "mccomposite/geometry/AbstractShapeVisitor.h"
#include "mccomposite/geometry/primitives/Sphere.h"


mccomposite::geometry::Sphere::Sphere
( double i_radius )
  : radius(i_radius)
{
}


mccomposite::geometry::Sphere::~Sphere
()
{
}

void mccomposite::geometry::Sphere::identify( AbstractShapeVisitor & visitor ) const 
{
  visitor.visit( this );
}


// version
// $Id$

// End of file 
