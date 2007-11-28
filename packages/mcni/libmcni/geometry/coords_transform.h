// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 2005  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#ifndef MCNI_GEOMETRY_COORDS_TRANSFORM_H
#define MCNI_GEOMETRY_COORDS_TRANSFORM_H

namespace mcni{

  // the rotation matrix here is the rotation matrix that converts absolute
  // coordinates to new coordinates relative to the relative coord system.
  //  position_relative = rotmat * (position_absolute - position_coordsystem )

  // absolute --> relative
  // transform coordinates from absolute coord system to relative coord system.
  // The position and orientation of the relative coordinate system
  // in the absolute coordinate system is given.

  //   1. position
  template <typename NumberType>
  inline void abs2rel
  ( Position<NumberType> &r, 
    const Position<NumberType> & cs_pos, const RotationMatrix<NumberType> & cs_rot);
  template <typename NumberType>
  inline void abs2rel
  ( Position<NumberType> &r, 
    const Position<NumberType> & cs_pos);


  //   2. velocity
  template <typename NumberType>
  inline void abs2rel
  ( Velocity<NumberType> &v, 
    const RotationMatrix<NumberType> & cs_rot);


  // relative --> absolute
  // transform coordinates from relative coord system to absolute coord system.
  // The position and orientation of the relative coordinate system
  // in the absolute coordinate system is given.

  //    1. position
  template <typename NumberType>
  inline void rel2abs
  ( Position<NumberType> &r,
    const Position<NumberType> & cs_pos, const RotationMatrix<NumberType> & cs_rot);
  template <typename NumberType>
  inline void rel2abs
  ( Position<NumberType> &r,
    const Position<NumberType> & cs_pos);

  //    2. velocity
  template <typename NumberType>
  inline void rel2abs
  ( Velocity<NumberType> &v,
    const RotationMatrix<NumberType> & cs_rot);
}


#include "coords_transform.icc"

#endif// MCNI_GEOMETRY_COORDS_TRANSFORM_H


// version
// $Id: coords_transform.h 7 2005-06-09 21:36:49Z linjiao $

// End of file
