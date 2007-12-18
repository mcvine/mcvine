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
( const AbstractShape * shape ) 
{
  shape->identify( *this );
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

