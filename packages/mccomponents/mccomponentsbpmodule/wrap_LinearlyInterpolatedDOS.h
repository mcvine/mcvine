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
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedDOS.h"


namespace wrap_mccomponents {

  template <typename Float, typename Array_1D>
  void wrap_LinearlyInterpolatedDOS_T( const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::phonon::LinearlyInterpolatedDOS<Float, Array_1D> w_t;
    typedef DANSE::phonon::AbstractDOS<Float> base_t;
    typedef typename w_t::float_t float_t;
    typedef typename w_t::index_t index_t;
    typedef typename w_t::array_t array_t;

    class_<w_t, bases<base_t>, boost::noncopyable>
      (classname, 
       init< 
       float_t, float_t, index_t, 
       const array_t &
       > ()
       )
      ;
  }

}


// version
// $Id$

// End of file 
