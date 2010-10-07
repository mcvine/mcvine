// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2010 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/TargetCone.h"


namespace wrap_mccomponents {

  void wrap_targetregion()
  {
    using namespace boost::python;
    using namespace mccomponents::kernels;

    class_<TargetCone>
      ("TargetCone",
       init<const TargetCone::R_t &, TargetCone::float_t>() )
      ;
    
  }

}

// version
// $Id$

// End of file 
