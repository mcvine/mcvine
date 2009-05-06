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


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/ChangeCoordinateSystem_forDispersion_3D.h"


namespace wrap_mccomponents {

  void wrap_ChangeCoordinateSystem_forDispersion_3D()
  {
    using namespace boost::python;
    typedef DANSE::phonon::AbstractDispersion_3D base_t;
    typedef DANSE::phonon::ChangeCoordinateSystem_forDispersion_3D w_t;

    class_<w_t, bases<base_t>, boost::noncopyable>
      ("ChangeCoordinateSystem_forDispersion_3D",
       init<const base_t &, const w_t::m_t &>()
       [with_custodian_and_ward<1,2>() ]
       )
      ;
  }

}


// version
// $Id$

// End of file 
