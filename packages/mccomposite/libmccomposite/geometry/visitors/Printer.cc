#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/geometry/visitors/Printer.h"

mccomposite::geometry::Printer::Printer
( std::ostream & i_os )
  : os(i_os)
{
}


void
mccomposite::geometry::Printer::visit
( const Box * box ) 
{
  os << "Box("
     << "x=" << box->edgeX << ","
     << "y=" << box->edgeY << "," 
     << "z=" << box->edgeZ << ","  
     << ")" ;
}

void
mccomposite::geometry::Printer::visit
( const Cylinder * cylinder ) 
{
  os << "Cylinder("
     << "radius=" << cylinder->radius << ","
     << "height=" << cylinder->height << "," 
     << ")" ;
}

void
mccomposite::geometry::Printer::visit
( const Sphere * sphere ) 
{
  os << "Sphere("
     << "radius=" << sphere->radius
     << ")" ;
}

void
mccomposite::geometry::Printer::visit
( const Difference * difference ) 
{
  os << "(" 
     << difference->body1 
     << " - "
     << difference->body2
     << ")"
    ;
}

void
mccomposite::geometry::Printer::visit
( const Intersection * intersection ) 
{
  os << "("  
     << intersection->body1 
     << " and "
     << intersection->body2
     << ")"
    ;
}

void
mccomposite::geometry::Printer::visit
( const Union * aunion ) 
{
  os << "("
     << aunion->body1 
     << " or "
     << aunion->body2
     << ")"
    ;
}

void
mccomposite::geometry::Printer::visit
( const Dilation * dilation ) 
{
  os << "("
     << dilation->scale 
     << " * "
     << dilation->body
     << ")"
    ;
}


void
mccomposite::geometry::Printer::visit
( const Reflection * reflection ) 
{
  os << "("
     << "reflection of "
     << reflection->body
     << " about "
     << reflection->vector
     << ")"
    ;
}

void
mccomposite::geometry::Printer::visit
( const Translation * translation ) 
{
  os << "("
     << translation->body
     << " translated to "
     << translation->vector
     << ")"
    ;
}

void
mccomposite::geometry::Printer::visit
( const Rotation * rotation )
{
  os << "("
     << rotation->body
     << " rotation by "
     << rotation->rotmat
     << ")"
    ;
}

