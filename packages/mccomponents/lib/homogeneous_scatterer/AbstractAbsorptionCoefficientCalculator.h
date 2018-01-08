// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>


#ifndef MCCOMPONENTS_ABSTRACTABSORPTIONCOEFFICIENTCALCULATOR_H
#define MCCOMPONENTS_ABSTRACTABSORPTIONCOEFFICIENTCALCULATOR_H


#include <stdexcept>
#include "mcni/neutron.h"

namespace mccomponents {

  class AbstractAbsorptionCoefficientCalculator{

  public:

    // meta methods
    virtual ~AbstractAbsorptionCoefficientCalculator() {};

    // methods
    virtual double operator() (const mcni::Neutron::Event &ev) const = 0;
  };

}

#endif


// version
// $Id$

// End of file 
