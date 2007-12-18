#include <algorithm>

#include "mccomposite/geometry/visitors/ArrowIntersector.h"


// meta-methods
mccomposite::geometry::ArrowIntersector::ArrowIntersector
()
{
}

mccomposite::geometry::ArrowIntersector::ArrowIntersector
(const arrow_t & arrow)
  : m_arrow( arrow )
{
}

mccomposite::geometry::ArrowIntersector::~ArrowIntersector
()
{
}


// methods
void mccomposite::geometry::ArrowIntersector::setArrow
(const arrow_t & arrow)
{
  m_arrow = arrow;
  reset();
}

void mccomposite::geometry::ArrowIntersector::setArrow
(const Position & start, 
 const Direction & direction)
{
  m_arrow.start = start;
  m_arrow.direction = direction;
  reset();
}


void mccomposite::geometry::ArrowIntersector::reset
()
{
  m_distances.clear();
}

mccomposite::geometry::ArrowIntersector::distances_t
mccomposite::geometry::ArrowIntersector::calculate_intersections
( const AbstractShape & shape ) 
{
  shape.identify( *this );
  return m_distances;
}



#include "mcstas_compact/mcstas_compact.h"

// visiting methods
void
mccomposite::geometry::ArrowIntersector::visit
( const Box * boxptr )
{
  const Box & box = *boxptr;

  const Position & start = m_arrow.start;
  const Direction & direction = m_arrow.direction;

  double dt_in, dt_out;

  double x = start.x; 
  double y = start.y;
  double z = start.z;

  double vx = direction.x;
  double vy = direction.y;
  double vz = direction.z;

  if ( ! McStas::box_intersect
       ( &dt_in,  &dt_out,  x,  y,  z,  vx,  vy,  vz,  
	 box.edgeX,  box.edgeY,  box.edgeZ) )
    return;

  // std::cout << dt_in << std::endl;
  //  std::cout << dt_out << std::endl;
  
  if (dt_in>0) m_distances.push_back( dt_in );
  if (dt_out>0) m_distances.push_back( dt_out );
  
  return ;
}


void
mccomposite::geometry::ArrowIntersector::visit
( const Cylinder * cylptr )
{
  const Cylinder & cylinder = *cylptr;

  const Position & start = m_arrow.start;
  const Direction & direction = m_arrow.direction;

  double dt_in, dt_out;

  double x = start.x; 
  double y = start.y;
  double z = start.z;

  double vx = direction.x;
  double vy = direction.y;
  double vz = direction.z;

  if ( ! McStas::cylinder_intersect
       ( &dt_in,  &dt_out,  x,  y,  z,  vx,  vy,  vz,  
	 cylinder.radius, cylinder.height) )
    return;

  // std::cout << dt_in << std::endl;
  //  std::cout << dt_out << std::endl;
  
  if (dt_in>0) m_distances.push_back( dt_in );
  if (dt_out>0) m_distances.push_back( dt_out );
  
  return;
}




/// calculate intersections of a line through a sphere
/*! the sphere is suppposed to centered in origin

    |r| = R

  the line is specified by its origin r0 and its direction vector v
  calculation results are specified with t, where t satisfied

    r - r0 = t*v

  the solution of these two equations is:

    t = - ( (r0.v) +/- sqrt( v^2 R^2 - |v X r0|^2 ) ) / v^2
 */
using mccomposite::geometry::Vector;
void calc_intersects_line_sphere
( const Vector & r0, const Vector & v, double R, 
  std::vector<double> & roots )
{
  double r0dotv = (r0|v);
  Vector r0Xv= r0*v;
  double v2 = (v|v);
  
  roots.clear();
  
  double b2m4ac = v2*R*R - (r0Xv|r0Xv);
  
  if (b2m4ac <0) return;
  
  double acc = 1.e-20;
  
  if (b2m4ac < acc ) {
    roots.push_back( - r0dotv/v2);
    return;
  }

  double sqrt_b2m4ac = sqrt( b2m4ac );
  roots.push_back( - (r0dotv + sqrt_b2m4ac )/v2 );
  roots.push_back( - (r0dotv - sqrt_b2m4ac )/v2 );
  //std::copy( roots.begin(), roots.end(), std::ostream_iterator<double>(std::cout, ",") );
  //std::cout << "\n";
}


void
mccomposite::geometry::ArrowIntersector::visit
( const Sphere * sphereptr )
{
  const Sphere & sphere = *sphereptr;

  const Position & start = m_arrow.start;
  const Direction & direction = m_arrow.direction;

  distances_t roots ;
  calc_intersects_line_sphere( start, direction, sphere.radius, roots );

  std::copy( roots.begin(), roots.end(), std::back_inserter( m_distances ) );
  return;
}


void
mccomposite::geometry::ArrowIntersector::visit
( const Difference * difference ) 
{
  const AbstractShape &body1 = difference->body1 ; 
  const AbstractShape &body2 = difference->body2 ;
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Intersection * intersection ) 
{
  const AbstractShape &body1 = intersection->body1 ; 
  const AbstractShape &body2 = intersection->body2 ;
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Union * aunion ) 
{
  const AbstractShape &body1 = aunion->body1 ; 
  const AbstractShape &body2 = aunion->body2 ;
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Dilation * dilation ) 
{
  const AbstractShape &body = dilation->body ; 
  const double &scale = dilation->scale ;
}


void
mccomposite::geometry::ArrowIntersector::visit
( const Reflection * reflection ) 
{
  throw;
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Translation * translation ) 
{
  const AbstractShape &body = translation->body ; 
  const Vector &vector = translation->vector ;
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Rotation * rotation )
{
  const AbstractShape &body = rotation->body ; 
}

