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

    class_<Pyramid, bases<AbstractShape> >
      ("Pyramid", 
       init< double, double, double >() )
      ;

    class_<Cone, bases<AbstractShape> >
      ("Cone", 
       init< double, double >() )
      ;

  }
}


// version
// $Id$

// End of file 
