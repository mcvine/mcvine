// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "mccomposite/mccomposite.h"


namespace wrap_mccomposite {

  typedef mccomposite::geometry::Vector Vector;
  typedef mccomposite::geometry::RotationMatrix RotationMatrix;
  
  inline double V3_getitem( const Vector & v3, size_t i)
  {
    return v3[i];
  }
  
  inline size_t V3_size( const Vector & v3)
  {
    return Vector::size();
  }
  
  void wrap_basics()
  {
    using namespace boost::python;
    // check if prior registration exists
    if (converter::registry::query(type_id<Vector>())==NULL) {
      // register
      class_<Vector>
	("Vector",
	 init<double, double, double>()
	 )
	.def(init<> () )
	.def("__len__", &V3_size )
	.def("__getitem__", &V3_getitem)
	.def("__iter__", iterator<Vector>() )
	;
    }

    // check if prior registration exists
    if (converter::registry::query(type_id<RotationMatrix>())==NULL) {
      class_<RotationMatrix>
	("RotationMatrix",
	 init<double, double, double, double, double, double, double, double, double>()
	 )
	.def(init<> () )
	;
    }
  } // wrap_basics
}


// version
// $Id$

// End of file 
