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


#ifndef MCCOMPONENTS_RANDOM_GEOMETRY_H
#define MCCOMPONENTS_RANDOM_GEOMETRY_H


#include "mcni/geometry/Vector3.h"


namespace mccomponents{

  namespace math{

    // randomly choose a direction inside the solid angle 
    // bound by "target_radius" in the direction given by "target_dir"
    // return the size of solid angle
    double choose_direction( mcni::Vector3<double> & dir,
			     const mcni::Vector3<double> & target_dir,
			     double target_radius);

    // randomly choose a direction in the full 4pi solid angle
    void choose_direction( mcni::Vector3<double> & dir );

  } // math

} // mccomponents


#endif //MCCOMPONENTS_RANDOM_GEOMETRY_H


// version
// $Id$

// End of file 
