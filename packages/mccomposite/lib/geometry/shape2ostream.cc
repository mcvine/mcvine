#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/geometry/visitors/Printer.h"


std::ostream & operator << 
( std::ostream & os, const mccomposite::geometry::AbstractShape & shape )
{
  mccomposite::geometry::Printer printer(os);
  shape.identify( printer );
  return os;
}
