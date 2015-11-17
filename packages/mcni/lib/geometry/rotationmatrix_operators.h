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

#ifndef MCNI_GEOMETRY_ROTATIONMATRIX_OPERATORS_H
#define MCNI_GEOMETRY_ROTATIONMATRIX_OPERATORS_H


#include "matrix3_operators.h"

template <typename NumberType>
mcni::Position<NumberType> operator *
(const mcni::Matrix3<NumberType> &m, const mcni::Position<NumberType> & r)
{
  using namespace mcni::matrix3_operators;
  return dot_mv( m * r );
}



template <typename NumberType>
mcni::Velocity<NumberType> operator *
(const mcni::Matrix3<NumberType> &m, const mcni::Velocity<NumberType> & v)
{
  using namespace mcni::matrix3_operators;
  return dot_mv( m * v );
}


#endif


// version
// $Id$

// End of file

