#include "mccomposite/geometry/locate.h"

mccomposite::geometry::Locator::Location locate
( const mccomposite::geometry::Position & position, 
  const mccomposite::geometry::AbstractShape & shape )
{
  static mccomposite::geometry::Locator locator;
  locator.setPoint( position );
  return locator.locate( shape );
}
