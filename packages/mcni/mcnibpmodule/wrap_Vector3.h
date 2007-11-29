// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include <boost/python/iterator.hpp>
#include "mcni/geometry/Vector3.h"


using namespace mcni;

template <typename Type>
inline Type V3_getitem( const Vector3<Type> & v3, size_t i)
{
  return v3[i];
}

template <typename Type>
inline Type V3_size( const Vector3<Type> & v3)
{
  return Vector3<Type>::size();
}

template <typename Type>
void wrapVector3( const char * name )
{
  using namespace boost::python;
  //xusing namespace DANSE::Simulation;

  typedef Vector3<Type> w_t;

  class_<w_t>
    (name,
     init<const Type &, const Type &, const Type & > () )
    .def("__len__", &V3_size<Type> )
    .def("__getitem__", &V3_getitem<Type>)
    .def("__iter__", iterator<w_t>() );
}


// version
// $Id: wrap_vector3.h 658 2007-10-24 21:33:08Z linjiao $

// End of file 
