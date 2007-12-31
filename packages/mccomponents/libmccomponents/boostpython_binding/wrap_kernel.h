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
#include "mccomponents/AbstractScatteringKernel.h"


namespace mccomponents {
  namespace boostpython_binding {
    
    using namespace boost::python;
    
    /// wrap a neutron scattering kernel class 
    /// that is derived from mccomponents::AbstractScatteringKernel
    /// Usage:
    ///  kernel_wrapper<kernel_t>::wrap( kernel_name, init< ... >() );
    /// Examples:
    ///  kernel_wrapper<phonon::coherent_inelastic_polycrystal>::wrap
    ///    ( "coherent_inelastic_polycrystal", init< double, double, ... >() );
    template <typename Kernel>
    struct kernel_wrapper
    {
      typedef boost::python::class_< Kernel, bases< AbstractScatteringKernel >,
				     boost::noncopyable> wrap;
    };
  }
}

// version
// $Id$

// End of file 
