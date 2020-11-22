// -*- C++ -*-
//
// Jiao Lin
//


#ifndef MCCOMPONENTS_KERNELS_CRYSTAL_H
#define MCCOMPONENTS_KERNELS_CRYSTAL_H

#include <cmath>
#include "mcni/math/number.h"
#include "mcni/geometry/Vector3.h"

namespace mccomponents {
  namespace kernels {

    // types
    typedef double float_t;
    typedef mcni::Vector3<float_t> K_t;
    typedef mcni::Vector3<float_t> R_t;

    struct Lattice{
      R_t a, b, c;                   /* unit cell unit vectors (direct space, AA) */
      K_t ra, rb, rc;                /* reciprocal lattice unit vectors (1/AA) with 2PI */
      float_t al, bl, cl;            /* lattice parameter lengths */
      float_t V0;                    /* Unit cell volume (AA**3) abs(a.bXc) */
      Lattice(const R_t &i_a, const R_t &i_b, const R_t &i_c)
        : a(i_a),
          b(i_b),
          c(i_c)
      {
        using mcni::PI;
        V0 = (a | (b*c));
        float_t _ = 2*PI/V0;
        ra = (b*c)*_;
        rb = (c*a)*_;
        rc = (a*b)*_;
        V0 = std::abs(V0);
        al = a.length(); bl = b.length(); cl = c.length();
      }
    };

    struct HKL{
      int h,k,l;
      float_t F2;                    /* unit: barn */
      HKL(int _h, int _k, int _l, float_t _F2)
        :h(_h),
         k(_k),
         l(_l),
         F2(_F2)
      {}
      HKL() {}
      bool operator<(const HKL rhs) const {
        if (this->h < rhs.h) return true;
        if (this->h > rhs.h) return false;
        if (this->k < rhs.k) return true;
        if (this->k > rhs.k) return false;
        if (this->l < rhs.l) return true;
        return false;
      }
    };

  } // kernels::
} // mccomponents::

#endif // MCCOMPONENTS_KERNELS_CRYSTAL_H

// End of file
