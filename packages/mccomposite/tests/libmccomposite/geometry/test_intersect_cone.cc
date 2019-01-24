// -*- C++ -*-
//
//

#include <cstdlib>
#include <cassert>
#include <iostream>
#include <cmath>
#include "mcni/test/assert.h"
#include "mccomposite/geometry/shapes.h"
#include "mccomposite/geometry/intersect.h"

#include "journal/debug.h"

using namespace std;
using namespace mccomposite::geometry;


namespace {
  double random( double min, double max )
  {
    using namespace std;
    return rand()*1./RAND_MAX*(max-min) + min;
  }
}

// special case where cone intersection has failed
void test1()
{
  Cone cone(0.00914101, 0.523688);
  Position start(-0.002106752520420636203,-0.014995300371214700941,-0.47812284760090373315);
  Direction direction(-191.69,-1150.83,2190.32);
  Arrow arrow(start, direction);
  ArrowIntersector::distances_t dists = intersect( arrow, cone );
}


// run a Monte Carlo
void test2()
{
  Cone cone(0.,1.);
  
  int N = 20000000;
  for (int i=0; i<N; i++) {
    cone.radius = exp(random(-3, 0));
    cone.height = exp(random(-3, 1));
    double x = random(-.2,.2), y = random(-.2,.2), z = random(-.2,.2);
    Position start(x,y,z);
    double vx = random(-1.,1.), vy = random(-1.,1.), vz = random(-1.,1.);
    Direction direction(vx,vy,vz);
    Arrow arrow(start, direction);
    ArrowIntersector::distances_t dists = intersect( arrow, cone );
    dists = intersect( arrow, cone );
  }
  // std::cout << dists << std::endl;
}


int main()
{
#ifdef DEBUG
//  journal::debug_t("mccomposite.geometry.ArrowIntersector").activate();
//   journal::debug_t("mccomposite.geometry.Locator").activate();
//   journal::debug_t("mccomposite.geometry.intersect").activate();
#endif
  test1();
  test2();
}

// End of file 
