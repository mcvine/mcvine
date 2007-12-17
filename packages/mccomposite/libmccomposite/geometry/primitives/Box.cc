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
  visitor.onBox( *this );
}

// version
// $Id: Box.cc 225 2005-08-02 15:56:48Z linjiao $

// End of file 
