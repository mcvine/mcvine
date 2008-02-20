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
#include "mccomponents/kernels/sample/phonon/DWFromDOS.h"


namespace wrap_mccomponents {

  template <typename Float>
  void wrap_DWFromDOS_T( const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::phonon::DWFromDOS<Float> w_t;
    typedef DANSE::phonon::AbstractDebyeWallerFactorCalculator<Float> base_t;
    typedef typename w_t::dos_t dos_t;

    class_<w_t, bases<base_t>, boost::noncopyable>
      (classname,
       init <
       const dos_t &, size_t 
       > ()
       [ with_custodian_and_ward<1,2> () 
	 ]
       )
      .def( "calc_DW_core", &w_t::calc_DW_core )
      ;
  }

}


// version
// $Id$

// End of file 
