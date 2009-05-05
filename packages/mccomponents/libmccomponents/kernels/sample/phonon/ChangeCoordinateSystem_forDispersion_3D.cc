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


#include <cmath>
#include "mcni/geometry/matrix3_operators.h"
#include "mccomponents/kernels/sample/phonon/ChangeCoordinateSystem_forDispersion_3D.h"


struct
DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
Details{
  typedef ChangeCoordinateSystem_forDispersion_3D w_t;
  Details( const w_t & target, const m_t & transformation);
  const w_t & m_target;

  K_t transform( const K_t & Q );

  m_t transformation;
};


DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::Details::
Details( const w_t & target, const m_t & transformation_ ) 
  : m_target(target), transformation(transformation_)
{
}

DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
K_t
DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::Details::
transform
( const K_t & Q )
{
  using namespace mcni::matrix3_operators;
  return dot_mv(transformation, Q);
}


DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
ChangeCoordinateSystem_forDispersion_3D
( const AbstractDispersion_3D &core , const m_t& transformation)
  : AbstractDispersion_3D( 0 ),
    m_core( core ),
    m_details( new Details(*this, transformation) )
{
}


DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
~ChangeCoordinateSystem_forDispersion_3D
()
{
}



DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::n_t
DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
nBranches() const
{
  return m_core.nBranches();
}


DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::n_t
DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
nAtoms() const
{
  return m_core.nAtoms();
}


DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
float_t 
DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
energy(n_t branch_id, const K_t &k) const
{
  K_t q = m_details->transform( k );
  return m_core.energy( branch_id, q );
}


DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
epsilon_t 
DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D::
polarization(n_t branch_id, n_t atom_id, const K_t &k) const
{
  K_t q = m_details->transform( k );
  return m_core.polarization( branch_id, atom_id, q );
}


// version
// $Id$

// End of file
