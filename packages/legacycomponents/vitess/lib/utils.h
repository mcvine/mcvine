// -*- c++ -*-

#ifndef MCVINE_VITESS_UTILS_H
#define MCVINE_VITESS_UTILS_H

#include <iostream>
#include <cmath>

#include "mcni/math/number.h"
#include "mcni/neutron/units_conversion.h"

namespace vitess {

  template <typename V3>
  double wavelength(const V3& velocity)
  {
    double v = std::sqrt(velocity[0]*velocity[0] 
			 +velocity[1]*velocity[1]
			 +velocity[2]*velocity[2]);
    using namespace mcni::neutron_units_conversion;
    return 2*mcni::PI/(v2k*v);
  }
  
  template <typename V3a, typename V3b>
  void convertV3
  (const V3a & invec, V3b & outvec)
  {
    for (unsigned int i=0; i<3; i++) 
      outvec[i] = invec[i];
  }

} // vitess

#endif
