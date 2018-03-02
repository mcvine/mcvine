// -*- C++ -*-
//
//


#include <cassert>
#include <iostream>
#include <vector>
#include "mcni/geometry/Vector3.h"


namespace {
  typedef mcni::Vector3<double> V3d;
  
  // calculate the time an arrow intersecting a triangle
  // the triangle is specified by coordinates of its 3 vertices (a,b,c)
  // The arrow starts at "r" and has a "velocity" "v"
  // if there is an intersection, the "time" of the intersection
  // will be pushed into the result array "ts". if not, nothing will happen
  void intersectTriangle
  (const V3d & r, const V3d & v,
   const V3d & A, const V3d & B, const V3d &C,
   std::vector<double> &ts)
  {
    // calculate normal
    V3d AB = B-A, AC = C-A;
    V3d N = AB*AC;
    N.normalize();
    double d = (N|A);   // distance from origin to the triangle plane along its normal
    double v_p = (N|v); // velocity along the normal
    // std::cout << "v_p=" << v_p << std::endl;
    if (std::abs(v_p) < 1e-10) return; // speed mostly parallel to the plane of the triangle
    double t = ( d - (N|r) ) / (N|v); // time is distance / velocity
    // std::cout << "t=" << t << std::endl;
    // the intersection of the plane of the triangle and the ray
    V3d P = r + v*t, AP=P-A;
    // AP = c1 * AB + c2 * AC
    // the condition for P to be inside ABC is c1>0, c2>0, c1+c2<1.
    // need to calculate c1 and c2
    // c1 = (AP dot AC*) / (AB dot AC*) where AC* = N X AC
    V3d AC_ = N * AC; double c1 = (AP|AC_)/(AB|AC_);
    if (c1<=0) return;
    // c2 = (AP dot AB*) / (AC dot AB*) where AB* = N X AB
    V3d AB_ = N * AB; double c2 = (AP|AB_)/(AC|AB_);
    if (c2<=0) return;
    if (c1+c2>=1) return;
    // 
    ts.push_back(t);
  }
}
  
void test1()
{
  std::vector<double> ts;
  intersectTriangle(V3d(0, 0, 0), V3d( 0, 0, 1),
		    V3d(0, 1, 1), V3d(1, -1, 1), V3d(-1, -1, 1),
		    ts);
  assert (ts.size()==1);
  assert (ts[0]==1.);
}

void test1a()
{
  std::vector<double> ts;
  intersectTriangle(V3d(0, 0, 0), V3d( 0, 0, -1),
		    V3d(0, 1, 1), V3d(1, -1, 1), V3d(-1, -1, 1),
		    ts);		    
  assert (ts.size()==1);
  assert (ts[0]==-1.);
}

void test1b()
{
  std::vector<double> ts;
  intersectTriangle(V3d(0, 0, 0), V3d( 1, 0, 0),
		    V3d(0, 1, 1), V3d(1, -1, 1), V3d(-1, -1, 1),
		    ts);		    
  assert (ts.size()==0);
}

void test1c()
{
  std::vector<double> ts;
  intersectTriangle(V3d(0, 0, 0), V3d( 0, 0, 10.),
		    V3d(0, 1, 1), V3d(1, -1, 1), V3d(-1, -1, 1),
		    ts);		    
  assert (ts.size()==1);
  assert (ts[0]==.1);
}

void test2()
{
  std::vector<double> ts;
  intersectTriangle(V3d(0, 0, 0), V3d( 1, 1, 1),
		    V3d(0, 0, 1), V3d(0, 1, 0), V3d(1, 0, 0),
		    ts);		    
  assert (ts.size()==1);
  assert (ts[0]==1./3);
}


void test2a()
{
  std::vector<double> ts;
  intersectTriangle(V3d(0, 0, 0), V3d( -1e-5, -1e-5, 1),
		    V3d(0, 0, 1), V3d(0, 1, 0), V3d(1, 0, 0),
		    ts);		    
  assert (ts.size()==0);
}

void test2b()
{
  std::vector<double> ts;
  intersectTriangle(V3d(0, 0, 0), V3d( -1e-5, 1, -1e-5),
		    V3d(0, 0, 1), V3d(0, 1, 0), V3d(1, 0, 0),
		    ts);		    
  assert (ts.size()==0);
}


int main()
{
  test1();
  test1a();
  test1b();
  test1c();
  test2();
  test2a();
  test2b();
}

// version
// $Id$

// End of file 
