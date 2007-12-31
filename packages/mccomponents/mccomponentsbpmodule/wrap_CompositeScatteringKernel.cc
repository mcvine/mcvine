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
#include "mccomponents/CompositeScatteringKernel.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"


namespace wrap_mccomponents {

  void wrap_CompositeScatteringKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;

    kernel_wrapper<mccomponents::CompositeScatteringKernel>::wrap
      ("CompositeScatteringKernel", 
       init<const mccomponents::CompositeScatteringKernel::kernels_t &>()
       [with_custodian_and_ward<1,2>()]
       )
      ;
  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
