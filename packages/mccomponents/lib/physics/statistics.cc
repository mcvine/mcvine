// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <cmath>

#include "mccomponents/physics/constants.h"
#include "mccomponents/physics/statistics.h"


double mccomponents::physics::BoseEinsteinDistribution
(double energy, double temperature)
{
  const double &T2E = Kelvin2meV;

  if (energy <0 ) {
    energy = std::abs( (double)energy );
  }
  
  return 1/(std::exp(energy/(temperature*T2E))-1);
}



// version
// $Id$

// End of file 
