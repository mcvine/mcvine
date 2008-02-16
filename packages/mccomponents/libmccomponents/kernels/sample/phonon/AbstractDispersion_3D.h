// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#ifndef PHONON_ABSTRACTDISPERSION_3D_H
#define PHONON_ABSTRACTDISPERSION_3D_H



#include "mcni/geometry/Vector3.h"

namespace DANSE{
  
  namespace phonon{

    //! phonon dispersion
    /*! base class for phonon dispersion
      ! nBranches() return number of branches
      ! energy() and polarization() return phonon energy and polarization 
    */
    class AbstractDispersion_3D{
    
    public:
      
      // types:
      typedef double float_t;
      typedef mcni::Vector3<float_t> K_t;
      typedef mcni::Vector3< std::complex<float_t> > epsilon_t;
      typedef unsigned int n_t;

      // meta methods
      AbstractDispersion_3D( n_t nAtoms );
      virtual ~AbstractDispersion_3D();

      // methods
      n_t nBranches() const;
      n_t nAtoms() const;
    
      virtual float_t energy(n_t branch_id, const K_t &k) const =0;
      virtual epsilon_t polarization(n_t branch_id, n_t atom_id, const K_t &k) const = 0;
    
    protected:
      // data
      n_t m_nAtoms, m_nBranches;
    
    };
  
  } // phonon::
} //DANSE::

#endif // PHONON_ABSTRACTDISPERSION_3D_H



// version
// $Id: AbstractDispersion_3D.h 178 2005-07-19 13:01:58Z linjiao $

// End of file
