// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2007 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "wrap_vector.h"
#include "mccomposite/geometry/RotationMatrix.h"


namespace wrap_mccomponents {

  void wrap_basic_containers()
  {
    using namespace boost::python;

    wrap_vector<int>( "int" ); 
    wrap_vector<unsigned int>( "uint" ); 
    wrap_vector<double>( "double" ); 

    wrap_vector2<mccomposite::geometry::RotationMatrix>("rotmat");
  }
}


// version
// $Id$

// End of file 
