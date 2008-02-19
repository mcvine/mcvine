// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedDispersionOnGrid_3D.h"


namespace wrap_mccomponents {

  template <typename Array_7D, typename Array_4D>
  void wrap_LinearlyInterpolatedDispersionOnGrid_3D_T(const char * classname)
  {
    using namespace boost::python;
    typedef DANSE::phonon::AbstractDispersion_3D base_t;
    typedef DANSE::phonon::LinearlyInterpolatedDispersionOnGrid_3D<Array_7D, Array_4D> w_t;
    typedef typename w_t::axis_t axis_t;
    typedef typename w_t::n_t n_t;
    typedef typename w_t::epsilonarray_t epsilonarray_t;
    typedef typename w_t::Earray_t Earray_t;

    class_<w_t, bases< base_t >, boost::noncopyable >
      (classname, 
       init< 
       n_t,
       const axis_t & , const axis_t &, const axis_t &, 
       epsilonarray_t & , Earray_t &
       > () 
       [ with_custodian_and_ward<1,3, 
	 with_custodian_and_ward<1,4,
	 with_custodian_and_ward<1,5,
	 with_custodian_and_ward<1,6,
	 with_custodian_and_ward<1,7> > > > > () ]
       )
      ;

  }

}

// version
// $Id$

// End of file 
