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


#ifndef MCNI_NEUTRON_COORDS_TRANSFORM_H
#define MCNI_NEUTRON_COORDS_TRANSFORM_H

namespace mcni{

  // the rotation matrix here is the rotation matrix that converts absolute
  // coordinates to new coordinates relative to the relative coord system.
  //  position_relative = rotmat * (position_absolute - position_coordsystem )

  // absolute --> relative
  // transform neutron coordinates from absolute coord system to 
  // relative coord system (Imagine it is on a neutron component).
  // The position and orientation of the relative coordinate system
  // in the absolute coordinate system is given.
  inline void abs2rel
  ( Neutron::Event &ev,
    const Position<double> & cs_pos, const RotationMatrix<double> & cs_rot);

  inline void abs2rel
  ( Neutron::Event &ev,
    const Position<double> & cs_pos);

  // relative --> absolute
  // transform coordinates from relative coord system to absolute coord system.
  // The position and orientation of the relative coordinate system
  // in the absolute coordinate system is given.
  inline void rel2abs
  ( Neutron::Event &ev,
    const Position<double> & cs_pos, const RotationMatrix<double> & cs_rot);

  inline void rel2abs
  ( Neutron::Event &ev,
    const Position<double> & cs_pos);


  // conversion of a bunch of neutrons
  void abs2rel_batch
  ( Neutron::Events &,
    const Position<double> & cs_pos, const RotationMatrix<double> & cs_rot);

  void rel2abs_batch
  ( Neutron::Events &,
    const Position<double> & cs_pos, const RotationMatrix<double> & cs_rot);

  // helpers
  template <typename NumberType>
  bool is_almost_I(const RotationMatrix<NumberType> & m);
  template <typename NumberType>
  bool is_almost_0(const Position<NumberType> & r);
}


#include "coords_transform.icc"

#endif// MCNI_NEUTRON_COORDS_TRANSFORM_H


// version
// $Id$

// End of file
