// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>


#ifndef MCCOMPONENTS_INTERPOLATEABSORPTIONFROMCURVE_H
#define MCCOMPONENTS_INTERPOLATEABSORPTIONFROMCURVE_H


#include "AbstractAbsorptionCoefficientCalculator.h"

namespace mccomponents {

  class InterpolateAbsorptionFromCurve: public AbstractAbsorptionCoefficientCalculator {

  public:
    typedef std::vector<double> vec_t;
    InterpolateAbsorptionFromCurve(const vec_t &energies, const vec_t &mus);
    virtual double operator() (const mcni::Neutron::Event &ev) const;
  private:
    vec_t m_energies, m_mus;
  };

}

#endif


// version
// $Id$

// End of file 
