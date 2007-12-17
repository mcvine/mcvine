#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/geometry/visitors/Printer.h"

mccomposite::geometry::Printer::Printer
( std::ostream & i_os )
  : os(i_os)
{
}


void
mccomposite::geometry::Printer::onBox
( const Box & box ) 
{
  os << "Box("
     << "x=" << box.edgeX << ","
     << "y=" << box.edgeY << "," 
     << "z=" << box.edgeZ << ","  
     << ")" ;
}

void
mccomposite::geometry::Printer::onDifference
( const Difference & difference ) 
{
  os << "(" 
     << difference.body1 
     << " - "
     << difference.body2
     << ")"
    ;
}

void
mccomposite::geometry::Printer::onIntersection
( const Intersection & intersection ) 
{
  os << "("  
     << intersection.body1 
     << " and "
     << intersection.body2
     << ")"
    ;
}

void
mccomposite::geometry::Printer::onUnion
( const Union & aunion ) 
{
  os << "("
     << aunion.body1 
     << " or "
     << aunion.body2
     << ")"
    ;
}

void
mccomposite::geometry::Printer::onDilation
( const Dilation & dilation ) 
{
  os << "("
     << dilation.scale 
     << " * "
     << dilation.body
     << ")"
    ;
}


void
mccomposite::geometry::Printer::onReflection
( const Reflection & reflection ) 
{
  os << "("
     << "reflection of "
     << reflection.body
     << " about "
     << reflection.vector
     << ")"
    ;
}

void
mccomposite::geometry::Printer::onTranslation
( const Translation & translation ) 
{
  os << "("
     << translation.body
     << " translated to "
     << translation.vector
     << ")"
    ;
}

void
mccomposite::geometry::Printer::onRotation
( const Rotation & rotation )
{
  os << "("
     << rotation.body
     << " rotation by "
     << rotation.rotmat
     << ")"
    ;
}

