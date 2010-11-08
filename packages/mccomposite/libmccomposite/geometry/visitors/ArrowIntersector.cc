#include <algorithm>
#include <sstream>

#include "mccomposite/geometry/visitors/ArrowIntersector.h"
#include "mccomposite/geometry/visitors/Locator.h"
#include "mccomposite/geometry/intersect.h"
#include "mccomposite/geometry/locate.h"
#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/geometry/tolerance.h"

#include "mccomposite/geometry/exception.h"

#include "journal/debug.h"


namespace ArrowIntersector_impl{

  char * jrnltag = "mccomposite.geometry.ArrowIntersector";
  
}


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



namespace {
  using mccomposite::geometry::Position;
  using mccomposite::geometry::Direction;

  bool isInvaildDirection( const Direction & direction )
  {
    return (direction[0] == 0 && direction[1] == 0 && direction[2] == 0 );
  }


  // calculate the time an arrow intersecting a rectangle centered at origin
  // the rectangle is on the x-y plane and its size is (X,Y)
  // The arrow starts at "r" and has a "velocity" "v"
  // if there is an intersection, the "time" of the intersection
  // will be pushed into the result array "ts". if not, nothing will happen
  void intersectRectangle
  (double rx, double ry, double rz, 
   double vx, double vy, double vz,
   double X, double Y, 
   std::vector<double> &ts)
  {
    double t = (0-rz)/vz;
    double r1x = rx + vx*t, r1y = ry+vy*t;
    if (std::abs(r1x) < X/2 && std::abs(r1y) < Y/2) 
      ts.push_back(t);
  }

  
  // calculate the time an arrow intersecting 
  // the side of a cylinder.
  // the cylinder is decribed by equation
  //   x^2 + y^2 = r^2
  // and z is limited in (-h/2, h/2)
  void intersectCylinderSide
  (double x, double y, double z,
   double vx, double vy, double vz,
   double r, double h,
   std::vector<double> &ts)
  {
    double a = vx*vx + vy*vy;
    double b = x*vx + y*vy;
    double c = x*x+y*y - r*r;
    double k = b*b-a*c;
    double t, hh = h/2.;

    if (k<0) return;
    if (k==0) {
      t = -b/a;
      if (std::abs(z+vz*t)<hh)
	ts.push_back(t);
      return;
    }
    k = std::sqrt(k);    

    t = (-b+k)/a;
    if (std::abs(z+vz*t)<hh)
      ts.push_back(t);

    t = (-b-k)/a;
    if (std::abs(z+vz*t)<hh)
      ts.push_back(t);
  }

  // calculate the time an arrow intersecting 
  // the top/bottom of a cylinder.
  // the cylinder is decribed by equation
  //   x^2 + y^2 = r^2
  // and z is limited in (-h/2, h/2)
  void intersectCylinderTopBottom
  (double x, double y, double z,
   double vx, double vy, double vz,
   double r, double h,
   std::vector<double> &ts)
  {
    double hh = h/2, r2 = r*r;
    double t;
    double x1, y1;

    t = (hh-z)/vz;
    x1 = x + vx*t;
    y1 = y + vy*t;
    if (x1*x1 + y1*y1 <= r2) {
      ts.push_back(t);
    }

    t = (-hh-z)/vz;
    x1 = x + vx*t;
    y1 = y + vy*t;
    if (x1*x1 + y1*y1 <= r2)
      ts.push_back(t);
  }

  // 
  const double epsilon = 1.e-7;
  inline bool eq_withinepsilon(double x, double y)
  {
    return std::abs(x-y) < epsilon;
  }
}

// visiting methods
void
mccomposite::geometry::ArrowIntersector::visit
( const Box * boxptr )
{
#ifdef DEBUG
  journal::debug_t debug( ArrowIntersector_impl::jrnltag );
#endif
  m_distances.clear();
  
  const Box & box = *boxptr;
  
  const Position & start = m_arrow.start;
  const Direction & direction = m_arrow.direction;
  if (isInvaildDirection(direction)) return;
  
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< "box: "<< *boxptr << journal::newline
	<< "start: " << start << journal::newline
	<< "direction: " << direction
	<< journal::endl
    ;
#endif
  
  double x = start.x; 
  double y = start.y;
  double z = start.z;
  
  double vx = direction.x;
  double vy = direction.y;
  double vz = direction.z;
  
  double X = box.edgeX, Y = box.edgeY, Z = box.edgeZ;
  std::vector<double> ts;
  if (vz!=0) {
    intersectRectangle(x,y,z-Z/2, vx,vy,vz, X, Y, ts);
    intersectRectangle(x,y,z+Z/2, vx,vy,vz, X, Y, ts);
  }
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< ts << journal::endl
    ;
#endif
  if (vx!=0) {
    intersectRectangle(y,z,x-X/2, vy,vz,vx, Y, Z, ts);
    intersectRectangle(y,z,x+X/2, vy,vz,vx, Y, Z, ts);
  }
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< ts << journal::endl
    ;
#endif
  if (vy!=0) {
    intersectRectangle(z,x,y-Y/2, vz,vx,vy, Z, X, ts);
    intersectRectangle(z,x,y+Y/2, vz,vx,vy, Z, X, ts);
  }
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< ts << journal::endl
    ;
#endif
  
  if (!ts.size()) return;
  if (ts.size() == 1) {
    // this is usually due to numerical errors
#ifdef DEBUG
    debug
      << journal::at(__HERE__)
      << "number of intersections between a line and a box should be 0 or 2, "
      << "we got " << ts.size() << ". " << journal::newline
      << "box: " << box << ", "
      << "arrow: " << m_arrow
      << journal::endl;
#endif
    return;
  }
  if (ts.size()!=2) {
    std::ostringstream oss;
    oss << "number of intersections between a line and a box should be 0 or 2, "
	<< "we got " << ts.size() << ". "
	<< "box: " << box << ", "
	<< "arrow: " << m_arrow
      ;
    throw Exception(oss.str());
  }
  
  if (ts[0] < ts[1]) {
    m_distances.push_back(ts[0]);
    m_distances.push_back(ts[1]);
  } else {
    m_distances.push_back(ts[1]);
    m_distances.push_back(ts[0]);
  }
  
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< m_distances << journal::endl
    ;
#endif

  return ;
}


void
mccomposite::geometry::ArrowIntersector::visit
( const Cylinder * cylptr )
{
#ifdef DEBUG
  journal::debug_t debug( ArrowIntersector_impl::jrnltag );
#endif

  m_distances.clear();
  
  const Cylinder & cylinder = *cylptr;

  const Position & start = m_arrow.start;
  const Direction & direction = m_arrow.direction;
  if (isInvaildDirection(direction)) return;
  
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< "cylinder: "<< cylinder << journal::newline
	<< "start: " << start << journal::newline
	<< "direction: " << direction
	<< journal::endl
    ;
#endif
  
  double x = start.x; 
  double y = start.y;
  double z = start.z;
  
  double vx = direction.x;
  double vy = direction.y;
  double vz = direction.z;

  const double &r = cylinder.radius;
  const double &h = cylinder.height;

  std::vector<double> ts;
  // side
  intersectCylinderSide(x,y,z, vx,vy,vz, r, h, ts);
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< ts << journal::endl
    ;
#endif

  // top/bottom
  intersectCylinderTopBottom(x,y,z, vx,vy,vz, r, h, ts);
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< ts << journal::endl
    ;
#endif
  
  if (ts.size()==0) return;
  
  if (ts.size()!=2) {
    if (ts.size()==1)
      throw Exception("number of intersections between a line and a cylinder should be 0 or 2");
    // there might be duplicates
    std::vector<double>::iterator new_end = std::unique
      (ts.begin(), ts.end(), eq_withinepsilon);
    if (new_end-ts.begin()!=2) 
      throw Exception("number of intersections between a line and a cylinder should be 0 or 2");
  }

  if (ts[0]<ts[1]) {
    m_distances.push_back(ts[0]);
    m_distances.push_back(ts[1]);
  } else {
    m_distances.push_back(ts[1]);
    m_distances.push_back(ts[0]);
  }
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
  
//   double acc = 1.e-20;
  
//   if (b2m4ac < acc ) {
//     roots.push_back( - r0dotv/v2);
//     return;
//   }
  
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
  m_distances.clear();
  
  const Sphere & sphere = *sphereptr;
  
  const Position & start = m_arrow.start;
  const Direction & direction = m_arrow.direction;
  if (isInvaildDirection(direction)) return;
  
  calc_intersects_line_sphere( start, direction, sphere.radius, m_distances );
  //
  //  if (m_distances.size()%2==1) throw Exception("odd number of intersections");
  return;
}



namespace ArrowIntersector_impl{
  
  using namespace mccomposite::geometry;

  struct isNotOnBorder : public std::unary_function<double, bool> {

    isNotOnBorder( const Arrow & arrow, const AbstractShape & shape )
      : m_arrow(arrow), m_shape(shape)
    {}
    bool operator() (double distance) 
    {
      bool ret = locate( m_arrow.start + distance * m_arrow.direction, m_shape ) != Locator::onborder;

#ifdef DEBUG
      journal::debug_t debug( ArrowIntersector_impl::jrnltag );
      
      debug << journal::at(__HERE__) 
	    << "start = " << m_arrow.start << journal::newline
	    << "direction = " << m_arrow.direction << journal::newline
	    << "distance = " << distance << journal::newline
	    << "point = " << m_arrow.start + distance * m_arrow.direction << journal::newline
	    << "shape = " << m_shape << journal::newline
	    << "isNotOnBorder = " << ret
	    << journal::endl;
      ;
#endif
      return ret;
    }
    
  private:
    const Arrow & m_arrow;
    const AbstractShape & m_shape;
  };
  
  
  typedef ArrowIntersector::distances_t distances_t;
  
  // clean up intersection list (distances) so that only 
  // points on border are reserved
  void remove_points_not_on_border
  ( distances_t & dists,
    const Arrow & arrow, const AbstractShape & shape,
    distances_t & ret)
  {
    using namespace std;
    isNotOnBorder isnotonborder( arrow, shape );
    
    remove_copy_if( dists.begin(), dists.end(), back_inserter( ret ),
		    isnotonborder); 
  }

}

namespace mccomposite{ namespace geometry{
    inline bool eq_double( double a, double b ) 
    {
      double max = std::max(std::abs(a), std::abs(b));
      return max < tolerance || std::abs((a-b)/max) < tolerance ;
    }
  }
}

void 
mccomposite::geometry::ArrowIntersector::visit_composition
(const Composition * composition)
{
  const std::vector< const AbstractShape * > & shapes = composition->shapes;
  using namespace ArrowIntersector_impl;

  // gather intersections and remove intersections that are not on border
  distances_t distances;  
  for (size_t i=0; i<shapes.size(); i++) {
    distances_t dists = intersect( m_arrow, *(shapes[i]) );
    remove_points_not_on_border( dists, m_arrow, *composition, distances );
  }
  
  // sort intersections
  std::sort( distances.begin(), distances.end() );

  // this turns out to be more troublesome than not doing it.
  // so let us comment it out:
//   // removed repeated intersection
//   distances_t::iterator newend = std::unique
//     ( distances.begin(), distances.end(), eq_double);

  // copy to result container
  m_distances.clear();
//   copy( distances.begin(), newend, std::back_inserter(m_distances) );
  copy( distances.begin(), distances.end(), std::back_inserter(m_distances) );

#ifdef DEBUG
  journal::debug_t debug( ArrowIntersector_impl::jrnltag );

  debug << journal::at(__HERE__) 
	<< "intersections between " 
	<< "arrow(" << m_arrow.start << "," << m_arrow.direction << ")"
	<< " and shape (" << *composition << ")"
	<< " are "
	<< m_distances << journal::endl
    ;
#endif

  //
  //  if (m_distances.size()%2==1) throw Exception("odd number of intersections");
}


void
mccomposite::geometry::ArrowIntersector::visit
( const Difference * difference ) 
{
  visit_composition( difference );
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Intersection * intersection ) 
{
  visit_composition( intersection );
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Union * aunion ) 
{
  visit_composition( aunion );
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Dilation * dilation ) 
{
  const AbstractShape &body = dilation->body ; 
  const double &scale = dilation->scale ;
  
  Arrow save = m_arrow;
  m_arrow.start = m_arrow.start *(1./scale);
  m_arrow.direction = m_arrow.direction * (1./scale);
  
  body.identify( *this );

#ifdef DEBUG
  journal::debug_t debug( ArrowIntersector_impl::jrnltag );

  debug << journal::at(__HERE__) 
	<< m_distances << journal::endl
    ;
#endif

  m_arrow = save;
  //
  //  if (m_distances.size()%2==1) throw Exception("odd number of intersections");
}


void
mccomposite::geometry::ArrowIntersector::visit
( const Reflection * reflection ) 
{
  throw Exception("not implemented");
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Translation * translation ) 
{
  const AbstractShape &body = translation->body ; 
  const Vector &vector = translation->vector ;

  Arrow save = m_arrow;
  m_arrow.start = m_arrow.start - vector;
  
  body.identify( *this );

  m_arrow = save;
  //
  //  if (m_distances.size()%2==1) throw Exception("odd number of intersections");
}

void
mccomposite::geometry::ArrowIntersector::visit
( const Rotation * rotation )
{
  const AbstractShape &body = rotation->body ; 
  
  RotationMatrix rotmat = rotation->rotmat;

  rotmat.transpose();

  Arrow save = m_arrow;
  m_arrow.start = rotmat * m_arrow.start;
  m_arrow.direction = rotmat * m_arrow.direction;

  body.identify( *this );

  m_arrow = save;
  //
  //  if (m_distances.size()%2==1) throw Exception("odd number of intersections");
}

