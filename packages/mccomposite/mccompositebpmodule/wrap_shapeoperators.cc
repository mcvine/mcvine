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


#include <sstream>
#include <boost/python.hpp>
#include "mccomposite/geometry/AbstractShape.h"
#include "mccomposite/geometry/locate.h"


namespace wrap_mccomposite {

  void wrap_shapeoperators()
  {
    using namespace boost::python;

    typedef mccomposite::geometry::Locator t_L;
    enum_<t_L::Location>( "location" )
      .value( "inside", t_L::inside)
      .value( "outside", t_L::outside)
      .value( "onborder", t_L::onborder)
      .export_values()
      ;

    def("locate", mccomposite::geometry::locate);

  }
}


// version
// $Id$

// End of file 
