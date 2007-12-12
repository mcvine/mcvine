#include <iostream>

#include "mccomposite/geometry/AbstractShape.h"
#include "mccomposite/geometry/shapes.h"
#include "mccomposite/geometry/visitors/LineIntersector.h"



// Arrow
template <typename Float>
mccomposite::Arrow<Float>::Arrow
(const position_t & i_start, const direction_t & i_direction )
  : start(i_start), 
    direction(i_direction)
{
}

template <typename Float>
mccomposite::Arrow<Float>::Arrow
()
  : start(0,0,0),
    direction(0,0,1)
{
}


template <typename Float>
void
mccomposite::Arrow<Float>::print
(std::ostream & os) const
{
  os << "an arrow starts at " << start << ", aims at " << direction;
}

// LineIntersector
mccomposite::LineIntersector::LineIntersector
()
{
}

mccomposite::LineIntersector::LineIntersector
(const arrow_t & arrow)
  : m_arrow( arrow )
{
}

mccomposite::LineIntersector::~LineIntersector
()
{
}

void mccomposite::LineIntersector::setArrow
(const arrow_t & arrow)
{
  m_arrow = arrow;
  reset();
}

void mccomposite::LineIntersector::setArrow
(const arrow_t::position_t & start, 
 const arrow_t::direction_t & direction)
{
  m_arrow.start = start;
  m_arrow.direction = direction;
  reset();
}

void mccomposite::LineIntersector::reset
()
{
  m_distances.clear();
}

mccomposite::LineIntersector::distances_t
mccomposite::LineIntersector::calculate_intersections
( const AbstractShape & shape ) 
{
  shape.identify( *this );
  return m_distances;
}



#include "mcstas_compact/mcstas_compact.h"

void
mccomposite::LineIntersector::onBox
( const Box & box ) 
{
  const arrow_t::position_t & start = m_arrow.start;
  const arrow_t::direction_t & direction = m_arrow.direction;

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

