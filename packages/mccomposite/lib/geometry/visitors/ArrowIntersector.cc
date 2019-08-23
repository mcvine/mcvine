#include <algorithm>
#include <sstream>
#include <iomanip>

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

namespace mccomposite{ namespace geometry{
    /*
    inline bool eq_double( double a, double b ) 
    {
      double max = std::max(std::abs(a), std::abs(b));
      return max < tolerance || std::abs((a-b)/max) < tolerance ;
    }
    */
    
    inline bool eq_withinepsilon(double x, double y)
    {
      return std::abs(x-y) < tolerance/5.;
    }
  }
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

  // calculate the time an arrow intersecting a triangle
  // the triangle is specified by coordinates of its 3 vertices (a,b,c)
  // The arrow starts at "r" and has a "velocity" "v"
  // if there is an intersection, the "time" of the intersection
  // will be pushed into the result array "ts". if not, nothing will happen
  void intersectTriangle
  (const Position & r, const Direction & v,
   const Position & A, const Position & B, const Position &C,
   std::vector<double> &ts)
  {
    // calculate normal
    Position AB = B-A, AC = C-A;
    Position N = AB*AC;
    N.normalize();
    double d = (N|A);   // distance from origin to the triangle plane along its normal
    double v_p = (N|v); // velocity along the normal
    // std::cout << "v_p=" << v_p << std::endl;
    if (std::abs(v_p) < 1e-10) return; // speed mostly parallel to the plane of the triangle
    double t = ( d - (N|r) ) / (N|v); // time is distance / velocity
    // std::cout << "t=" << t << std::endl;
    // the intersection of the plane of the triangle and the ray
    Position P = r + v*t, AP=P-A;
    // AP = c1 * AB + c2 * AC
    // the condition for P to be inside ABC is c1>0, c2>0, c1+c2<1.
    // need to calculate c1 and c2
    // c1 = (AP dot AC*) / (AB dot AC*) where AC* = N X AC
    Position AC_ = N * AC; double c1 = (AP|AC_)/(AB|AC_);
    if (c1<0) return;
    // c2 = (AP dot AB*) / (AC dot AB*) where AB* = N X AB
    Position AB_ = N * AB; double c2 = (AP|AB_)/(AC|AB_);
    if (c2<0) return;
    if (c1+c2>1) return;
    // 
    ts.push_back(t);
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


// visiting methods
void
mccomposite::geometry::ArrowIntersector::visit
( const Pyramid * pyramidptr )
{
#ifdef DEBUG
  journal::debug_t debug( ArrowIntersector_impl::jrnltag );
#endif
  m_distances.clear();
  
  const Pyramid & pyramid = *pyramidptr;
  
  const Position & start = m_arrow.start;
  Direction direction = m_arrow.direction;
  if (isInvaildDirection(direction)) return;
  double length = direction.length();
  direction= direction * (1./length); // normalize
  
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< "pyramid: "<< *pyramidptr << journal::newline
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
  
  double X = pyramid.edgeX, Y = pyramid.edgeY, H = pyramid.height;
  std::vector<double> ts;

  // base
  if (vz!=0) {
    intersectRectangle(x,y,z+H, vx,vy,vz, X, Y, ts);
  }

  // 4 triangles as sides
  intersectTriangle(start, direction,
		    Position(0, 0, 0), Position(X/2, Y/2, -H), Position(X/2, -Y/2, -H),
		    ts);
  intersectTriangle(start, direction,
		    Position(0, 0, 0), Position(X/2, -Y/2, -H), Position(-X/2, -Y/2, -H),
		    ts);
  intersectTriangle(start, direction,
		    Position(0, 0, 0), Position(-X/2, -Y/2, -H), Position(-X/2, Y/2, -H),
		    ts);
  intersectTriangle(start, direction,
		    Position(0, 0, 0), Position(-X/2, Y/2, -H), Position(X/2, Y/2, -H),
		    ts);

#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< ts << journal::endl
    ;
#endif

  if (!ts.size()) return;
  // remove duplicates
  std::sort(ts.begin(), ts.end());  // have to sort otherwise unique does not work well
  std::vector<double>::iterator new_end = std::unique
    (ts.begin(), ts.end(), eq_withinepsilon);
  int N = new_end-ts.begin();
  //
  if (N == 1) {
    // this is usually due to numerical errors
#ifdef DEBUG
    debug
      << journal::at(__HERE__)
      << "number of intersections between a line and a pyramid should be 0 or 2, "
      << "we got " << N << ". " << journal::newline;
    for (std::vector<double>::iterator it=ts.begin(); it!=new_end; it++) oss << *it << ", ";
    oss << std::endl
      << "pyramid: " << pyramid << ", "
      << "arrow: " << m_arrow
      << journal::endl;
#endif
    return;
  }
  if (N!=2) {
    std::ostringstream oss;
    oss << "number of intersections between a line and a pyramid should be 0 or 2, "
	<< "we got " << N << ": " ;
    for (std::vector<double>::iterator it=ts.begin(); it!=new_end; it++) oss << *it << ", ";
    oss << std::endl
	<< pyramid << ", "
	<< m_arrow << std::endl
      ;
    oss << std::scientific << ts[2] - ts[0] << std::endl;
    throw Exception(oss.str());
  }
  
  if (ts[0] < ts[1]) {
    m_distances.push_back(ts[0]/length);
    m_distances.push_back(ts[1]/length);
  } else {
    m_distances.push_back(ts[1]/length);
    m_distances.push_back(ts[0]/length);
  }
  
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< m_distances << journal::endl
    ;
#endif
  return ;
}


// visiting methods
void
mccomposite::geometry::ArrowIntersector::visit
( const Cone * coneptr )
{
#ifdef DEBUG
  journal::debug_t debug( ArrowIntersector_impl::jrnltag );
#endif
  m_distances.clear();
  
  const Cone & cone = *coneptr;
  
  const Position & start = m_arrow.start;
  Direction direction = m_arrow.direction;
  if (isInvaildDirection(direction)) return;
  double length = direction.length();
  direction = direction * (1./length); // normalize
  
#ifdef DEBUG
  debug << journal::at(__HERE__) 
	<< "cone: "<< *coneptr << journal::newline
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
  double vl = direction.length();
  
  double R = cone.radius, H = cone.height;
  std::vector<double> ts;

  //
  Direction D = direction; D.normalize();
  Direction V(0, 0, -1);
  Direction CO(x, y, z);
  double cos_theta_sq = H*H/(R*R+H*H);
  // at^2+bt+c=0
  // a = (D . V)^2 - cos^2(theta)
  // b = 2( (D.V) (CO.V) - (D.CO) cos^2(theta) )
  // c = (CO.V)^2 - (CO.CO)cos^2(theta)
  double DdotV = (D|V);
  double COdotV = (CO|V);
  double DdotCO = (D|CO);
  double a = DdotV*DdotV - cos_theta_sq;
  double b = 2 * (DdotV*COdotV - DdotCO * cos_theta_sq);
  double c = COdotV*COdotV - (CO|CO)  * cos_theta_sq;
  double t1[2]; int N=0;  // temp array to hold t values for the infinite cone
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "DdotV=" << DdotV << ", COdotV=" << COdotV << ", DdotCO=" << DdotCO << journal::newline
	<< "a=" << a << ", b=" << b << ", c=" << c << journal::newline
	<< journal::endl
    ;
#endif
  
  if (eq_withinepsilon(a, 0.)) {
    if (eq_withinepsilon(b, 0.)) {
      // infinity solutions or no solutions. ingore this
    } else {
      t1[0] = -c/b /vl; N = 1; // one solution
    }
  } else {
    // a is not zero
    double delta = b*b-4*a*c;
    if (delta >= 0) {
      // two solutions
      N = 2;
      t1[0] = (-b-std::sqrt(delta))/2./a/vl;
      t1[1] = (-b+std::sqrt(delta))/2./a/vl;
    }
  }
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "t1=" << journal::newline;
  for (int i=0; i<N; i++) debug << t1[i] << ", ";
  debug << journal::endl;
#endif
  // limit the cone to be between z=0 and z=-H
  for (int i=0; i<N; i++) {
    // compute z
    double z1 = z+t1[i]*vz;
    if (z1<tolerance/10 && z1>=-H-tolerance/10) ts.push_back(t1[i]);
  }
  
  // base
  double t2 = (-H-z)/vz;
  double x2 = x + vx*t2, y2 = y + vy*t2;
  if (x2*x2+y2*y2 < R*R) ts.push_back(t2);
  
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "ts=" << journal::newline;
  for (int i=0; i<ts.size(); i++) debug << ts[i] << ", ";
  debug << journal::endl;
#endif
  
  if (!ts.size()) return;
  // remove duplicates
  std::sort(ts.begin(), ts.end());  // have to sort otherwise unique does not work well
  std::vector<double>::iterator new_end = std::unique
    (ts.begin(), ts.end(), eq_withinepsilon);
  N = new_end-ts.begin();

  //
  if (N==2) ;
  else {
    //
    std::ostringstream oss;
    oss << "number of intersections between a line and a cone should be 0 or 2, "
	<< "we got " << N << ": " ;
    oss << std::setprecision(20);
    for (std::vector<double>::iterator it=ts.begin(); it!=new_end; it++) oss << *it << ", ";
    oss << std::endl
	<< cone << ", "
	<< m_arrow << std::endl
      ;
    std::cout << oss.str();
    
    if (N == 1) {
      // this is usually due to numerical errors
      return;
    } else if (N==3) {
      // most likely the line crosses an edge and duplicated intersections were recorded
      // both for the infinite cone and the base.
      // just merge the two that are closer together
      // since ts array is already sorted, this is easy.
      // we will return ts[0] and ts[1] later. so only when ts[0] and ta[1] is closer, we
      // need to move ts[2] up.
      if (ts[1]<(ts[0]+ts[2])/2.) {
	ts[1] = ts[2];
      }
    } else {
      throw Exception("Something went wrong. Max number of intersections between a line and a cone is 3");
    }
  }
  
  if (ts[0] < ts[1]) {
    m_distances.push_back(ts[0]/length);
    m_distances.push_back(ts[1]/length);
  } else {
    m_distances.push_back(ts[1]/length);
    m_distances.push_back(ts[0]/length);
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

