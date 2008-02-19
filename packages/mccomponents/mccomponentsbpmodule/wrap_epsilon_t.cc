// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include <string>
#include "wrap_Vector3.h"

namespace wrap_mccomponents {

  template <typename Float>
  void _wrap_epsilon_t(const char *floattypename)
  {
    typedef std::complex<Float> complex_t;
    typedef mcni::Vector3<complex_t> w_t;
    
    std::string name = "epsilon_";
    name += floattypename;
    wrap::wrap_Vector3<w_t>( name.c_str() );
  }

  void wrap_epsilon_t( )
  {
    _wrap_epsilon_t<double>( "double" );
  }

}


// version
// $Id$

// End of file 
