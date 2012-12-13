#ifndef MCNI_MATH_FUNC_H 
#define MCNI_MATH_FUNC_H 


#include <complex>

namespace mcni {

  template <typename T> int sgn(T val) {
    return (T(0) < val) - (val < T(0));
  }

}

#endif// MCNI_MATH_FUNC_H 
