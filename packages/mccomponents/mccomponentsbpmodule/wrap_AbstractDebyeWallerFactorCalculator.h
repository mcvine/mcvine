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


#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/AbstractDebyeWallerFactor.h"


namespace wrap_mccomponents {

  template <typename Float>
  Float
  DWCalculator_DW_Q
  ( const DANSE::phonon::AbstractDebyeWallerFactorCalculator<Float> & dwcalcor,
    const typename DANSE::phonon::AbstractDebyeWallerFactorCalculator<Float>::K_t & Q )
  {
    return dwcalcor.DW( Q );
  }

  template <typename Float>
  Float
  DWCalculator_DW_q
  ( const DANSE::phonon::AbstractDebyeWallerFactorCalculator<Float> & dwcalcor,
    const Float & q )
  {
    return dwcalcor.DW( q );
  }


  template <typename Float>
  void wrap_AbstractDebyeWallerFactorCalculator_T( const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::phonon::AbstractDebyeWallerFactorCalculator<Float> w_t;

    class_<w_t, boost::noncopyable>
      (classname, no_init)
      .def("__call__", &DWCalculator_DW_Q<Float> )
      .def("__call__", &DWCalculator_DW_q<Float> )
      ;
  }

}


// version
// $Id$

// End of file 
