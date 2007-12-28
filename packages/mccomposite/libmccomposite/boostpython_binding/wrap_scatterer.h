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
#include "mccomposite/AbstractNeutronScatterer.h"


namespace mccomposite {
  namespace boostpython_binding {
    
    using namespace mccomposite;
    using namespace boost::python;
    
    /// wrap a neutron scatterer class that is derived from mccomposite::AbstractNeutronScatterer
    /// Usage:
    ///  scatterer_wrapper<scatterer_t>::wrap( scatterer_name, init< ... >() );
    /// Examples:
    ///  scatterer_wrapper<Aluminum>::wrap( "Aluminum", init< double, double, ... >() );
    template <typename Scatterer>
    struct scatterer_wrapper
    {
      typedef boost::python::class_< Scatterer, bases< AbstractNeutronScatterer >,
				     boost::noncopyable> wrap;
    };
  }
}

// version
// $Id$

// End of file 
