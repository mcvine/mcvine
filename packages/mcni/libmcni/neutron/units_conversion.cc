#include <cmath>
#include <iostream>
#include <cassert>

#include "mcni/neutron/units_conversion.h"


namespace mcni{
  
  namespace neutron_units_conversion{
    
    using std::sqrt;
    
    //! neutron energy (meV) to velocity (m/s)
    double E2v( double energy ) {
      return sqrt(energy)*437.3949;
    }
    //! neutron velocity to energy 
    double v2E( double velocity) {
      return velocity*velocity*5.227e-6;
    }
    //! square of neutron velocity to energy
    double vsquare2E( double vsquare) {
      return vsquare*5.227e-6;
    }
    //! square of neutron k vector to energy
    double ksquare2E( double ksquare) {
      return vsquare2E(k2v*k2v*ksquare);
    }
    //!  neutron k vector to energy
    double k2E( double k)
    {
      return ksquare2E(k*k);
    }
    //!  neutron energy to k
    double E2k( double E)
    {
      return E2v(E)*v2k;
    }

  } // neutron_units_conversion::
  
} // mcni::
