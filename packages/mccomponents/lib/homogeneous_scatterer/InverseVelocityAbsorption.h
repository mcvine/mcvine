// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>


#ifndef MCCOMPONENTS_INVERSEVELOCITYABSORPTION_H
#define MCCOMPONENTS_INVERSEVELOCITYABSORPTION_H


#include "AbstractAbsorptionCoefficientCalculator.h"

namespace mccomponents {

  class InverseVelocityAbsorption: public AbstractAbsorptionCoefficientCalculator {
    // "normal" behavior
  public:
    InverseVelocityAbsorption(double mu_at_2200);
    virtual double operator() (const mcni::Neutron::Event &ev) const;
  private:
    double m_mu_at_2200;
  };

}

#endif


// version
// $Id$

// End of file 
