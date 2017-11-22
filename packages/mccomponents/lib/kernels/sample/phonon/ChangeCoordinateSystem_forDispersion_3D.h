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

#ifndef CHANGECOORDINATESYSTEM_FORDISPERSION_3D_H
#define CHANGECOORDINATESYSTEM_FORDISPERSION_3D_H



#include <memory>

#include "mcni/geometry/Matrix3.h"
#include "AbstractDispersion_3D.h"


namespace DANSE{
  
  namespace phonon{

    //! change coord system
    class ChangeCoordinateSystem_forDispersion_3D : public AbstractDispersion_3D{
    
    public:
      
      // types
      typedef double float_t;
      typedef mcni::Matrix3<float_t> m_t;

      // meta methods
      ChangeCoordinateSystem_forDispersion_3D
      (const AbstractDispersion_3D &, const m_t& transformation);
      virtual ~ChangeCoordinateSystem_forDispersion_3D();

      // methods
      n_t nBranches() const;
      n_t nAtoms() const;
    
      virtual float_t energy(n_t branch_id, const K_t &k) const;
      virtual epsilon_t polarization(n_t branch_id, n_t atom_id, const K_t &k) const;

      virtual float_t max_energy(n_t branch_id) const {return m_core.max_energy(branch_id);}
      virtual float_t min_energy(n_t branch_id) const {return m_core.min_energy(branch_id);}
    
    protected:
      // data
      const AbstractDispersion_3D & m_core;
      
      struct Details;
      std::auto_ptr< Details > m_details;
    };
  
  } // phonon::
} //DANSE::


#endif // CHANGECOORDINATESYSTEM_FORDISPERSION_3D_H



// version
// $Id$

// End of file
