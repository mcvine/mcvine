// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2008 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>

#include "mccomponents/kernels/sample/AbstractSQ.h"
#include "mccomponents/kernels/sample/SQAdaptor.h"

extern "C" {
#include "sans/sphere.h"
}


namespace wrap_models{

  struct Sphere {

    Sphere( double scale, double radius, double contrast, double background) 
    {
      p.scale = scale;
      p.radius = radius;
      p.contrast = contrast;
      p.background = background;
    }

    double operator() (double q) const
    {
      return sphere_analytical_1D( const_cast<SphereParameters *>(&p), q );
    }

    SphereParameters p;
    
  };

  
  void wrap_sphere()
  {
    using namespace boost::python;
    typedef Sphere w_t;
    class_<w_t>
      ( 
       "SANSModel_Sphere",
       init< double, double, double, double >()
	)
      ;
    
    using namespace mccomponents::sample;
    typedef SQAdaptor<w_t> SQ;
    class_<SQ, bases<AbstractSQ> >
      (
       "SANSModel_Sphere_SQAdaptor",
       init< const w_t & >()
       )
      ;
  }
}


// version
// $Id: mccompositebpmodule.cc 658 2007-10-24 21:33:08Z linjiao $

// End of file 

