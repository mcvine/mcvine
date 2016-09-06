// -*- C++ -*-
//
//

#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/DGSSXResPixel.h"

#include "mccomposite/boostpython_binding/wrap_scatterer.h"


namespace wrap_mccomponents {

  void wrap_DGSSXResPixel()
  {

    using namespace mccomposite::boostpython_binding;
    typedef mccomponents::DGSSXResPixel w_t;
    scatterer_wrapper<w_t>::wrap
      ("DGSSXResPixel", 

       init< 
       double, double,
       const mccomponents::AbstractShape &
       >
       () 
       [with_custodian_and_ward<1,4>()]
       )
      ;
  }
}


// End of file 
