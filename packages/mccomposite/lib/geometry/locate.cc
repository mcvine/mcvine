#include "mccomposite/geometry/locate.h"
#include "mccomposite/geometry/shape2ostream.h"

mccomposite::geometry::Locator::Location 
mccomposite::geometry::locate
( const mccomposite::geometry::Position & position, 
  const mccomposite::geometry::AbstractShape & shape )
{
  mccomposite::geometry::Locator locator;
  locator.setPoint( position );
  Locator::Location location = locator.locate( shape );
  return location;
}
