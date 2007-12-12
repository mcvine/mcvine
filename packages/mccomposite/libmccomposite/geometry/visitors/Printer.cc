#include "mccomposite/geometry/shapes.h"
#include "mccomposite/geometry/visitors/Printer.h"

mccomposite::Printer::Printer
( std::ostream & i_os )
  : os(i_os)
{
}


void
mccomposite::Printer::onBox
( const Box & box ) 
{
  os << "Box("
     << "x=" << box.edgeX << ","
     << "y=" << box.edgeY << "," 
     << "z=" << box.edgeZ << ","  
     << ")" ;
}


