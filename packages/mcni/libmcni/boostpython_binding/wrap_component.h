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
#include "mcni/AbstractNeutronComponent.h"


namespace mcni {
  namespace boostpython_binding {
    
    using namespace mcni;
    using namespace boost::python;
    
    /// wrap a neutron component class
    /// Usage:
    ///  component_wrapper<component_t>::wrap( component_name, init< ... >() );
    /// Examples:
    ///  component_wrapper<Guide>::wrap( "guide", init< double, double, double >() );
    template <typename Component>
    struct component_wrapper
    {
      typedef boost::python::class_< Component, bases< AbstractNeutronComponent > > wrap;
    };
  }
}

// version
// $Id$

// End of file 
