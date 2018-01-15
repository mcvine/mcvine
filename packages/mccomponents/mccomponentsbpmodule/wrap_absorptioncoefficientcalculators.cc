// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <boost/python.hpp>
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomponents/homogeneous_scatterer/AbstractAbsorptionCoefficientCalculator.h"
#include "mccomponents/homogeneous_scatterer/HomogeneousNeutronScatterer.h"
#include "mccomponents/homogeneous_scatterer/InverseVelocityAbsorption.h"
#include "mccomponents/homogeneous_scatterer/InterpolateAbsorptionFromCurve.h"

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

    typedef std::vector<double> vec_t;
    class_<mccomponents::InterpolateAbsorptionFromCurve,
	   bases<AbstractAbsorptionCoefficientCalculator> >
      ("InterpolateAbsorptionFromCurve",
       init<const vec_t&, const vec_t&> ()
       );
  }
}


// version
// $Id$

// End of file 
