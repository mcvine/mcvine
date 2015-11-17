// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"


DANSE::phonon::AbstractDispersion_3D::AbstractDispersion_3D
( n_t nAtoms )
  : m_nAtoms( nAtoms ), m_nBranches( 3 * nAtoms )
{
}

DANSE::phonon::AbstractDispersion_3D::~AbstractDispersion_3D
()
{
}

DANSE::phonon::AbstractDispersion_3D::n_t 
DANSE::phonon::AbstractDispersion_3D::nBranches() const 
{return m_nBranches;}

DANSE::phonon::AbstractDispersion_3D::n_t 
DANSE::phonon::AbstractDispersion_3D::nAtoms() const
{return m_nAtoms;}


// version
// $Id$

// End of file 
