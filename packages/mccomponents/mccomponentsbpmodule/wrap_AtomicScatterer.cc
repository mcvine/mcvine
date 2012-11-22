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


#include "mccomponents/kernels/sample/phonon/AtomicScatterer.h"

#include <boost/python.hpp>
#include "wrap_vector.h"


namespace wrap_mccomponents {

  void wrap_AtomicScatterer()
  {
    using namespace boost::python;

    typedef mccomponents::kernels::AtomicScatterer w_t;
    typedef w_t::float_t float_t;
    typedef w_t::R_t R_t; 

    class_<w_t>
      ("AtomicScatterer", 
       init<
       const R_t &, float_t
       > ()
       )
      .def_readwrite("coherent_scattering_length", &w_t::coherent_scattering_length)
      .def_readwrite("coherent_cross_section", &w_t::coherent_cross_section)
      .def_readwrite("incoherent_cross_section", &w_t::incoherent_cross_section)
      ;

    wrap_vector2<w_t>( "AtomicScatterer" );
  }

}


// version
// $Id$

// End of file 
