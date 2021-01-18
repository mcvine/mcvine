// -*- C++ -*-
//
// Jiao Lin
//


#ifndef MCCOMPONENTS_KERNELS_SINGLECRYSTALDIFFRACTIONPEAKDATA_H
#define MCCOMPONENTS_KERNELS_SINGLECRYSTALDIFFRACTIONPEAKDATA_H

#include <vector>
#include "mcni/neutron.h"
#include "mccomponents/kernels/sample/crystal.h"

namespace mccomponents {
  namespace kernels {

    namespace SingleCrystalDiffractionData {

      // data independent of neutron
      struct HKLData{
        mccomponents::kernels::HKL hkl;
        K_t tau;
        float_t tau_length;
        K_t u1, u2, u3; // unit vectors of local coordinate system for a particular tau
        K_t uT1, uT2, uT3; // transposed u
        K_t sig; // gaussian broadening along three local axes. unit: 1/AA
        float_t sig123; // product of sig 1,2,3. unit: 1/AA^3
        float_t m1, m2, m3; // ??? Diagonal matrix representation of Gauss ??? unit: AA^2
        float_t cutoff;
      };

      // depends on neutron ki
      struct TauData{
        int index;                   /* Index into hkl table */ // change to ptr ????
        float_t refl;                /* unit: 1 */
        float_t xs;                  /* unit: barn */
        float_t sigma_1, sigma_2;
        /* The following vectors are in local koordinates. */
        K_t ki;
        K_t rho;                     /* The vector ki - tau */
        float_t rho_length;          /* Length of rho vector */
        K_t o;                       /* Origin of Ewald sphere tangent plane */
        K_t n;                       /* Normal vector of Ewald sphere tangent */
        K_t b1, b2;                  /* Spanning vectors of Ewald sphere tangent. unit: 1 */
        float_t l11, l12, l22;       /* Cholesky decomposition L of 2D Gauss */
        float_t det_L;               /* Determinant of L */
        float_t y0x, y0y;            /* 2D Gauss center in tangent plane */
      };

    };
  } // kernels::
} // mccomponents::

#endif // MCCOMPONENTS_KERNELS_SINGLECRYSTALDIFFRACTIONPEAKDATA_H

// End of file
