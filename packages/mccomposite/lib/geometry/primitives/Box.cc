// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include "mccomposite/geometry/AbstractShapeVisitor.h"
#include "mccomposite/geometry/primitives/Box.h"

mccomposite::geometry::Box::Box
(double i_edgeX, double i_edgeY, double i_edgeZ )
  : edgeX(i_edgeX), edgeY(i_edgeY), edgeZ(i_edgeZ)
{
}

mccomposite::geometry::Box::~Box
()
{
}

void mccomposite::geometry::Box::identify( AbstractShapeVisitor & visitor ) const 
{
  visitor.visit( this );
}

// version
// $Id$

// End of file 
