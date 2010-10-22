// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2010 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include "mccomponents/math/random.h"
#include "mccomponents/math/random/geometry.h"
#include "mcni/geometry/utils.h"


#ifdef DEEPDEBUG
#define DEBUG
#endif

#ifdef DEEPDEBUG
#define DEBUG
#endif

#ifdef DEBUG
#include "journal/debug.h"
#endif


double 
mccomponents::math::choose_direction
( mcni::Vector3<double> & dir, const mcni::Vector3<double> & target_dir,
  double target_radius)
{
  using mcni::PI;
  typedef mcni::Vector3<double> V3;

  // square of distance
  double l2 = target_dir.length2();
  double costheta_max = sqrt(l2/(target_radius*target_radius+l2));
  if (target_radius < 0) costheta_max *= -1;

  double solidangle = 2*PI*(1 - costheta_max);

  // choose theta and phi
  double theta = acos (random(costheta_max, 1));
  double phi = random(0, 2 * PI);

  // choose normal vector
  V3 n;
  if(target_dir.x == 0 && target_dir.z == 0)
    n = V3(1,0,0);
  else
    n = V3(-target_dir.z, 0, target_dir.x);
  
  V3 u = target_dir * n;
  
  dir = target_dir;
  rotate(dir, u, theta);
  rotate(dir, target_dir, phi);

  return solidangle;
}


void 
mccomponents::math::choose_direction
( mcni::Vector3<double> & dir )
{
  using mcni::PI;
  using namespace std;
  double costheta = random(-1, 1);
  double theta = acos(costheta);
  double sintheta = sin(theta);
  double phi = random(0, 2 * PI);
  dir.x = sintheta*cos(phi);
  dir.y = sintheta*sin(phi);
  dir.z = costheta;
}


// version
// $Id$

// End of file 
