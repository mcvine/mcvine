// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                          (C) 2008  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#ifndef PHONON_PERIODICDISPERSION_3D_H
#define PHONON_PERIODICDISPERSION_3D_H



#include <memory>

#include "AbstractDispersion_3D.h"


namespace DANSE{
  
  namespace phonon{

    //! convert an arbitrary dispersion to a periodic dispersion
    class PeriodicDispersion_3D : public AbstractDispersion_3D{
    
    public:
      
      // types:
//       typedef double float_t;
//       typedef mcni::Vector3<float_t> K_t;
//       typedef std::complex<float_t> complex_t;
//       typedef mcni::Vector3< complex_t > epsilon_t;
//       typedef unsigned int n_t;
      struct ReciprocalCell {
	K_t b1, b2, b3;
      };

      // meta methods
      PeriodicDispersion_3D( const AbstractDispersion_3D &, const ReciprocalCell& );
      virtual ~PeriodicDispersion_3D();

      // methods
      n_t nBranches() const;
      n_t nAtoms() const;
    
      virtual float_t energy(n_t branch_id, const K_t &k) const;
      virtual epsilon_t polarization(n_t branch_id, n_t atom_id, const K_t &k) const;
    
    protected:
      // data
      const AbstractDispersion_3D & m_core;
      ReciprocalCell m_rcell;
      struct Details;
      std::auto_ptr< Details > m_details;
    };
  
  } // phonon::
} //DANSE::


#endif // PHONON_PERIODICDISPERSION_3D_H



// version
// $Id: PeriodicDispersion_3D.h 178 2005-07-19 13:01:58Z linjiao $

// End of file
