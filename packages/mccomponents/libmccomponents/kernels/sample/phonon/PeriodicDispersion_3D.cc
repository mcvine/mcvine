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
#include "mccomponents/kernels/sample/phonon/PeriodicDispersion_3D.h"


template <typename FloatType> 
FloatType
decimal_part( const FloatType & num )
{
  return num - std::floor(num);
}


struct
DANSE::phonon::PeriodicDispersion_3D::
Details{
  typedef PeriodicDispersion_3D w_t;
  Details( const w_t & target );
  const w_t & m_target;

  K_t reducedQ( const K_t & Q );
  const ReciprocalCell &rc;
  K_t a1, a2, a3;
};

// algorithm hint:
// b1, b2, b3
// a1 dot b2 = 0; a1 dot b3 = 0
// a1 dot b1 = 2pi
// Q = q1*b1 + q2*b2 + q3*b3
// qi = (Q dot ai)/2/pi
// Q dot ai = qi*2pi = Q dot ai

DANSE::phonon::PeriodicDispersion_3D::Details::
Details( const w_t & target ) 
  : m_target(target),
    rc( target.m_rcell )
{
  mcni::get_inversions<float_t>
    ( rc.b1, rc.b2, rc.b3,
      a1, a2, a3 );
}

DANSE::phonon::PeriodicDispersion_3D::
K_t
DANSE::phonon::PeriodicDispersion_3D::Details::
reducedQ
( const K_t & Q )
{
  float_t c1 = a1|Q, c2 = a2|Q, c3 = a3|Q;
  return decimal_part<float_t>(c1)*rc.b1 \
    + decimal_part<float_t>(c2)*rc.b2 \
    + decimal_part<float_t>(c3)*rc.b3;
}


DANSE::phonon::PeriodicDispersion_3D::
PeriodicDispersion_3D
( const AbstractDispersion_3D &core , const ReciprocalCell& rcell)
  : AbstractDispersion_3D( 0 ),
    m_core( core ),
    m_rcell( rcell ),
    m_details( new Details(*this) )
{
}


DANSE::phonon::PeriodicDispersion_3D::
~PeriodicDispersion_3D
()
{
}



DANSE::phonon::PeriodicDispersion_3D::n_t
DANSE::phonon::PeriodicDispersion_3D::
nBranches() const
{
  return m_core.nBranches();
}


DANSE::phonon::PeriodicDispersion_3D::n_t
DANSE::phonon::PeriodicDispersion_3D::
nAtoms() const
{
  return m_core.nAtoms();
}


DANSE::phonon::PeriodicDispersion_3D::
float_t 
DANSE::phonon::PeriodicDispersion_3D::
energy(n_t branch_id, const K_t &k) const
{
  K_t q = m_details->reducedQ( k );
  return m_core.energy( branch_id, q );
}


DANSE::phonon::PeriodicDispersion_3D::
epsilon_t 
DANSE::phonon::PeriodicDispersion_3D::
polarization(n_t branch_id, n_t atom_id, const K_t &k) const
{
  K_t q = m_details->reducedQ( k );
  return m_core.polarization( branch_id, atom_id, q );
}


// version
// $Id$

// End of file
