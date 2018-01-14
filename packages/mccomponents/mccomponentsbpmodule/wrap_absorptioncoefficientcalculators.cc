// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <boost/python.hpp>
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/AbstractAbsorptionCoefficientCalculator.h"
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"
#include "mccomponents/homogeneous_scatterer/InverseVelocityAbsorption.h"

namespace wrap_mccomponents {

  using namespace boost::python;
  using namespace mccomponents;

  void wrap_absorptioncoefficientcalculators()
  {
    class_<AbstractAbsorptionCoefficientCalculator, boost::noncopyable>
      ("AbstractAbsorptionCoefficientCalculator", no_init)
      ;

    class_<mccomponents::InverseVelocityAbsorption,
	   bases<AbstractAbsorptionCoefficientCalculator> >
      ("InverseVelocityAbsorption",
       init<double> ()
       );
  }
}


// version
// $Id$

// End of file 
