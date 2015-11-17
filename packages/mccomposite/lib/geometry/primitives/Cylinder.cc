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
#include "mccomposite/geometry/primitives/Cylinder.h"


mccomposite::geometry::Cylinder::Cylinder
( double i_radius, double i_height)
  : radius(i_radius), height(i_height)
{
}


mccomposite::geometry::Cylinder::~Cylinder
()
{
}

void mccomposite::geometry::Cylinder::identify( AbstractShapeVisitor & visitor ) const 
{
  visitor.visit( this );
}


// version
// $Id$

// Generated automatically by CxxMill on Sat Apr  9 19:21:43 2005

// End of file 
