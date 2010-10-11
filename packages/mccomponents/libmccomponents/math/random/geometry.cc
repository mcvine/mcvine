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


#include "mccomponents/math/random/geometry.h"


// temporarily we still need mcstas_compact
#include "mcstas_compact/randvec.h"

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
  double solid_angle;
  McStas::randvec_target_circle(&(dir.x), &(dir.y), &(dir.z),
				&solid_angle, 
				target_dir.x, target_dir.y, target_dir.z,
				target_radius);
  return solid_angle;
}


void 
mccomponents::math::choose_direction
( mcni::Vector3<double> & dir )
{
#ifdef DEEPDEBUG
  journal::debug_t debug("Random");
#endif
  double solid_angle;
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< dir
	<< journal::endl;
#endif
  McStas::randvec_target_circle(&(dir.x), &(dir.y), &(dir.z),
				&solid_angle, 
				0,0,1, 0);
#ifdef DEEPDEBUG
  debug << journal::at(__HERE__)
	<< dir
	<< journal::endl;
#endif
}


// version
// $Id$

// End of file 
