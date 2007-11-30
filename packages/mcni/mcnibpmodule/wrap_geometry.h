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


//#include <boost/python.hpp>
//#include "mcni/geometry/Vector3.h"
//#include "mcni/geometry/Position.h"
#include "mcni/geometry.h"
#include "wrap_Vector3.h"


namespace wrap {

  using namespace mcni;
  using namespace boost::python;
  
  template <typename Type>
  void wrap_Position( const char * elementTypeName )
  {
    using namespace boost::python;
    std::string name("Position_");

    name += elementTypeName;
    
    typedef Position<Type> w_t;
    typedef Vector3<Type> base_t;

    class_< w_t, bases< base_t > > 
      (name.c_str(),
       init<const Type &, const Type &, const Type &>()
       )
      ;
    
  }

  template <typename Type>
  void wrap_Velocity( const char * elementTypeName )
  {
    using namespace boost::python;
    std::string name("Velocity_");

    name += elementTypeName;

    typedef Velocity<Type> w_t;
    typedef Vector3<Type> base_t;
    
    class_<w_t, bases< base_t > >
      (name.c_str(), 
       init<const Type &, const Type &, const Type &> ()
       )
      ;
  }
  
  template <typename Type>
  void wrap_RotationMatrix( const char * elementTypeName )
  {
    using namespace boost::python;
    std::string name("RotationMatrix_");

    name += elementTypeName;
    
    typedef RotationMatrix<Type> w_t;
    typedef  Matrix3<Type> base_t;
    
    class_<w_t, bases<base_t> >
      (name.c_str(), 
       init<
       const Type &, const Type &, const Type &,
       const Type &, const Type &, const Type &,
       const Type &, const Type &, const Type &
       > () 
       )
      ;
  }

}

// version
// $Id: wrap_vector3.h 658 2007-10-24 21:33:08Z linjiao $

// End of file 
