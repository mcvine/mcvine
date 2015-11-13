// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved 
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <cmath>

#include "mccomponents/math/random.h"

#include "mccomponents/physics/constants.h"
#include "mccomponents/physics/statistics.h"
#include "mccomponents/kernels/sample/phonon/utils.h"


unsigned int mccomponents::kernels::phonon::pick_phonon_branch( size_t n_br )
{
  return (unsigned int)(math::random(size_t(0), n_br) );
}

double mccomponents::kernels::phonon::phonon_bose_factor(double energy, double T)
{
  using physics::BoseEinsteinDistribution;
  double bose_factor;
  if (energy == 0.0) bose_factor = 1;
  else {
    if (energy>0.0) bose_factor = 1.0;
    else bose_factor = 0.0;
    bose_factor += BoseEinsteinDistribution(std::abs(energy),T);
  }
  return bose_factor;
}

// version
// $Id$

// End of file 
