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

#ifndef MCCOMPONENTS_MATH_FUNCTOR_H
#define MCCOMPONENTS_MATH_FUNCTOR_H


#include <cmath>


namespace mccomponents { namespace math {
    
  /// base class for a 1D functor
  class Functor{
  public:
    Functor() {}
    virtual ~Functor() {}
    virtual double evaluate (double x) const = 0;
  };

  // sin functor
  class Sin : public Functor {
  public:
    Sin( double amplitude, double circ_freq, double phase )
      : m_amp( amplitude ), m_circ_freq( circ_freq ), m_phase( phase) 
    {}
    double evaluate( double x) const { return m_amp*std::sin( m_circ_freq*x + m_phase ); }

  private:
    double m_amp, m_circ_freq, m_phase;
  };

}} // mccomponents::math



#endif //MCCOMPONENTS_MATH_FUNCTOR_H

// version
// $Id$

// End of file 
