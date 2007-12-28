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

  void wrap_basics()
  {
    using namespace boost::python;

    class_<mccomposite::geometry::Vector>
      ("Vector",
       init<double, double, double>()
       )
      .def(init<> () )
      ;

    class_<mccomposite::geometry::RotationMatrix>
      ("RotationMatrix",
       init<double, double, double, double, double, double, double, double, double>()
       )
      .def(init<> () )
      ;
  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
