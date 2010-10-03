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


#include "wrap_Vector3.h"
#include "mcni/geometry/Matrix3.h"


namespace wrap {
  
  using namespace mcni;
  
  template <typename Type>
  void wrap_Matrix3( const char * elementTypeName )
  {
    using namespace boost::python;

    std::string name;

    name = std::string("Vector3_") + elementTypeName;

    // wrap the base class first
    wrap_Vector3< Vector3<Type> >(name.c_str());

    
    // now wrap the Matrix3 class
    typedef Matrix3<Type> w_t;
    typedef Vector3< Vector3<Type> > base_t;

    name = std::string("Matrix3_") + elementTypeName;
    
    class_<w_t, bases<base_t> >
      (name.c_str(),
       init
       <
       const Type &, const Type &, const Type &,
       const Type &, const Type &, const Type &,
       const Type &, const Type &, const Type &
       > () )
      ;
  }
  
}

// version
// $Id$

// End of file 
