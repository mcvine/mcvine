#include "mccomposite/geometry/visitors/Locator.h"
#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/exception.h"

#include "journal/debug.h"


namespace Locator_impl{

  char * jrnltag = "mccomposite.geometry.Locator";
  
}



mccomposite::geometry::Locator::Locator
(double i_roundingErrorTolerance)
  : point(0,0,0),
    roundingErrorTolerance(i_roundingErrorTolerance)
{
}


void
mccomposite::geometry::Locator::setPoint
( const Position & i_point )
{
  point = i_point;
}


mccomposite::geometry::Locator::Location
mccomposite::geometry::Locator::locate
( const AbstractShape & shape )
{
  shape.identify( *this );
  return location;
}

void
mccomposite::geometry::Locator::visit
( const Box * box )
{ 
  const double & X = box->edgeX;
  const double & Y = box->edgeY;
  const double & Z = box->edgeZ;

  const double & x = point.x;
  const double & y = point.y;
  const double & z = point.z;

  const double & ret = roundingErrorTolerance;
  
  using std::abs;
  
  if (abs(x) > (X+ret)/2. || abs(y) > (Y+ret)/2. || abs(z) > (Z+ret)/2.)
    { location = outside; return; }
  if (abs(abs(x) - X/2.) < ret || abs(abs(y) - Y/2.) < ret || abs(abs(z) - Z/2.) < ret) 
    { location = onborder; return; }

  location = inside; return;
}

void
mccomposite::geometry::Locator::visit
( const Cylinder * cylinder ) 
{
  const double & radius = cylinder->radius;
  const double & height = cylinder->height;

  const double & z = point.z;

  const double & ret = roundingErrorTolerance;

  using std::abs;
  if ( abs(z)-height/2. > ret ) { location = outside; return; }
  
  const double & x = point.x;
  const double & y = point.y;
  double r = std::sqrt(x*x+y*y);

  if ( r-radius > ret ) { location = outside; return; }

  if ( height/2.-abs(z) > ret && radius-r > ret ) { location = inside; return; }

  location = onborder; return;

}

void
mccomposite::geometry::Locator::visit
( const Pyramid * pyramid ) 
{
  const double & X = pyramid->edgeX;
  const double & Y = pyramid->edgeY;
  const double & height = pyramid->height;

  const double & z = point.z;
  const double & rtol = roundingErrorTolerance;
  using std::abs;

  // z too large or negative, outside
  if ( z > rtol || z<-height-rtol) { location = outside; return; }
  
  const double & x = point.x;
  const double & y = point.y;
  double ratio = -z/height;
  double X1 = ratio*X, Y1 = ratio*Y;
  // x, y too large, outside
  if ( std::abs(x) > X1/2 + rtol || std::abs(y) > Y1/2 + rtol) { location = outside; return; }
  // z inside
  if ( z < - rtol && z > -height+rtol ) {
    // z inside, x, y inside, so inside
    if ( std::abs(x) < X1/2 - rtol && std::abs(y) < Y1/2 - rtol) { location = inside; return; }
  } 
  // z at border, x,y inside or border, so it is border
  location = onborder; return;
}

void
mccomposite::geometry::Locator::visit
( const Cone * cone ) 
{
  const double & R = cone->radius;
  const double & height = cone->height;

  const double & z = point.z;
  const double & rtol = roundingErrorTolerance;
  using std::abs;

  // z too large or negative, outside
  if ( z > rtol || z<-height-rtol) { location = outside; return; }
  
  const double & x = point.x;
  const double & y = point.y;
  double r = std::sqrt(x*x + y*y);
  double ratio = -z/height;
  double R1 = ratio*R;
  // x, y too large, outside
  if ( r > R1 + rtol) { location = outside; return; }
  // z inside
  if ( z < - rtol && z > -height+rtol ) {
    // z inside, x, y inside, so inside
    if ( r < R1 - rtol) { location = inside; return; }
  } 
  // z at border, x,y inside or border, so it is border
  location = onborder; return;
}

void
mccomposite::geometry::Locator::visit
( const Sphere * sphere ) 
{
  const double & radius = sphere->radius;
  double R2 = radius * radius;

  const double & x = point.x;
  const double & y = point.y;
  const double & z = point.z;
  double r2 = x*x + y*y + z*z;
  
  const double & ret = roundingErrorTolerance;

  if (r2 - R2 > ret) { location = outside; return; }
  if (R2 - r2 > ret) { location = inside; return; }
  location = onborder; return;
}

void
mccomposite::geometry::Locator::visit
( const Difference * difference ) 
{
  const AbstractShape &body1 = *(difference->shapes[0]) ; 
  const AbstractShape &body2 = *(difference->shapes[1]) ;
  Location p1 = locate( body1 );
  Location p2 = locate( body2 );
  if (p1 == outside || p2 == inside) {location = outside;}
  else if (p1 == onborder || p2 == onborder) {location = onborder;}
  else location = inside; 
  return;
}

void
mccomposite::geometry::Locator::visit
( const Intersection * intersection ) 
{
  const Composition::shapecontainer_t & shapes = intersection->shapes;

  bool isinside = 1;
  for (size_t i=0; i<shapes.size(); i++) {
    Location p = locate( *(shapes[i]) );
    if (p == outside) {location = outside; return;}
    isinside &= p==inside;
  }

  if (isinside) {location = inside; return;}

  location = onborder; return;
}

void
mccomposite::geometry::Locator::visit
( const Union * aunion ) 
{
  const Composition::shapecontainer_t & shapes = aunion->shapes;

  bool isoutside = 1;
  for (size_t i=0; i<shapes.size(); i++) {
    Location p = locate( *(shapes[i]) );
    if (p == inside) {location = inside; return;}
    isoutside &= p==outside;
  }

  if (isoutside) {location = outside; return;}

  location = onborder; return;
}

void
mccomposite::geometry::Locator::visit
( const Dilation * dilation ) 
{
  const AbstractShape &body = dilation->body ; 
  const double &scale = dilation->scale ;
  Vector save = point;
  point = point * (1./scale);
  body.identify( *this );
  point = save;
}


void
mccomposite::geometry::Locator::visit
( const Reflection * reflection ) 
{
  throw Exception("handler for Reflection not implemented");
}

void
mccomposite::geometry::Locator::visit
( const Translation * translation ) 
{
  const AbstractShape &body = translation->body ; 
  const Vector &vector = translation->vector ;
  Vector save = point;
  point -= vector;
  body.identify( *this );
  point = save;
}

void
mccomposite::geometry::Locator::visit
( const Rotation * rotation )
{
  const AbstractShape &body = rotation->body ; 
  RotationMatrix rotationMatrix = rotation->rotmat ;
  Vector save = point;
  rotationMatrix.transpose();
  point = rotationMatrix * point;
  body.identify( *this );
  point = save;
}

