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


#include "mccomposite/mccomposite.h"
#include "wrap_Geometer.h"


namespace wrap_mccomposite {

  void wrap_geometers()
  {
    using namespace boost::python;

    wrap_Geometer<AbstractNeutronScatterer>( "NeutronScatterer" );
    
    typedef Geometer<AbstractNeutronScatterer>::position_t position_t;
    class_<position_t, bases<mccomposite::geometry::Vector> >("Position", init<double, double, double>());

    typedef Geometer<AbstractNeutronScatterer>::orientation_t orientation_t;
    class_<orientation_t>
      ("Orientation",
       init<double, double, double, double, double, double, double, double, double>()
       )
      .def(init<> () )
      ;
  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
