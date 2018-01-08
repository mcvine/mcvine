// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>


#ifndef MCCOMPONENTS_CONSULTSCATTERINGKERNEL_H
#define MCCOMPONENTS_CONSULTSCATTERINGKERNEL_H


#include <stdexcept>
#include "AbstractAbsorptionCoefficientCalculator.h"

namespace mccomponents {

  class ConsultScatteringKernel: public AbstractAbsorptionCoefficientCalculator {
    // this class is just for alerting HomogeneousScatterer to ask its kernel
    // for absorption coefficient.
  public:
    virtual double operator() (const mcni::Neutron::Event &ev) const {
      // should not be called, so throw an exception
      throw std::runtime_error("Scattering kernel should calculates the absorption coefficient!");
    }
  };

}

#endif


// version
// $Id$

// End of file 
