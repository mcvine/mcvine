// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2007-2013  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef MCCOMPONENTS_REGRESSION_LINEAR1_H
#define MCCOMPONENTS_REGRESSION_LINEAR1_H


#include <memory>

namespace mccomponents {

  namespace math {

    // fit y = cx. return c and R**2
    template <typename Float>
    void linear_regression1
    (const Float * x, const Float *y, int N, Float &c, Float &R2);

  }
}


#include <functional>
#include <numeric>

template <typename Float>
void mccomponents::math::linear_regression1
(const Float * x, const Float *y, int N, Float &c, Float &R2)
{
  Float xys=0, xxs=0, ys=0;
  
  for (int i=0; i<N; i++) {
    xys += x[i]*y[i];
    xxs += x[i]*x[i];
    ys += y[i];
  }
  c = xys/xxs;
  
  // compute R2
  Float yave = ys/N;
  Float sstot=0, sserr=0;
  for (int i=0; i<N; i++){
    sstot += (y[i]-yave)*(y[i]-yave);
    sserr += (y[i]-c*x[i])*(y[i]-c*x[i]);
  }
  R2 = 1 - sserr/sstot;
}

#endif // MCCOMPONENTS_REGRESSION_LINEAR1_H

// version
// $Id$

// End of file 
