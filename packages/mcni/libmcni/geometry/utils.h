// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2010  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#ifndef MCNI_GEOMETRY_UTILS_H
#define MCNI_GEOMETRY_UTILS_H

#include "Vector3.h"

namespace mcni {

  template <typename Number>
  void rotate(Vector3<Number> &v, const Vector3<Number> &by, const Number &angle, Number epsilon=1e-7);

  template <typename Number>
  Vector3<Number> rotated(const Vector3<Number> &v, const Vector3<Number> &by, const Number &angle, Number epsilon=1e-7);

}

#include "utils.icc"

#endif

// version
// $Id$

// End of file 
