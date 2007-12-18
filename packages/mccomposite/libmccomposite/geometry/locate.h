#include <iostream>
#include "AbstractShape.h"
#include "Position.h"
#include "visitors/Locator.h"

mccomposite::geometry::Locator::Location locate
( const mccomposite::geometry::Position & position, 
  const mccomposite::geometry::AbstractShape & shape );
