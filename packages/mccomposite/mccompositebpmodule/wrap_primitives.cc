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

#include "mccomposite/geometry/primitives.h"

#include <boost/python.hpp>


namespace wrap_mccomposite {

  void wrap_primitives()
  {
    using namespace boost::python;
    using namespace mccomposite::geometry;


    class_<Box, bases<AbstractShape> >
      ("Block", 
       init< double, double, double>() )
      ;
    
    class_<Sphere, bases<AbstractShape> >
      ("Sphere", 
       init< double >() )
      ;

    class_<Cylinder, bases<AbstractShape> >
      ("Cylinder", 
       init< double, double >() )
      ;

  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
