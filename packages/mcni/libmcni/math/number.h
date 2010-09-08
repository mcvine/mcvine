#ifndef MCNI_MATH_NUMBER_H 
#define MCNI_MATH_NUMBER_H 


#include <complex>

namespace mcni {

  typedef std::complex<double> Complex;
  const Complex cI(0,1);

  const double PI=3.1415926535897932384626;

  const double DEG2RAD = PI/180.;
}

#endif// MCNI_MATH_NUMBER_H 
