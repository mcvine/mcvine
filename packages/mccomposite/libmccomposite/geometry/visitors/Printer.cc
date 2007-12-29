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
     << *(difference->shapes[0])
     << " - "
     << *(difference->shapes[1])
     << ")"
    ;
}

void
mccomposite::geometry::Printer::visit
( const Intersection * intersection ) 
{
  const Composition::shapecontainer_t & shapes = intersection->shapes;
  os << "(" ;
  for (size_t i=0; i<shapes.size(); i++)  {
    os << (*shapes[i]);
    if (i!= shapes.size()-1) os << " ^ ";
  }
  os << ")" ;
}

void
mccomposite::geometry::Printer::visit
( const Union * aunion ) 
{
  const Composition::shapecontainer_t & shapes = aunion->shapes;
  os << "(" ;
  for (size_t i=0; i<shapes.size(); i++)  {
    os << (*shapes[i]);
    if (i!= shapes.size()-1) os << " + ";
  }
  os << ")" ;
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

