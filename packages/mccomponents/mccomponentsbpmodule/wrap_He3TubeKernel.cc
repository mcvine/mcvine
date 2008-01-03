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


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/detector/He3Tube.h"
#include "mccomponents/boostpython_binding/wrap_kernel.h"
#include "wrap_vector.h"


namespace wrap_mccomponents {

  void wrap_He3TubeKernel()
  {
    using namespace boost::python;
    using namespace mccomponents::boostpython_binding;
    using namespace mccomponents::detector;

    typedef mccomponents::kernels::He3Tube w_t;
    typedef w_t::channels_t channels_t;

    kernel_wrapper<w_t>::wrap
      ("He3TubeKernel",
       init<double, const channels_t &, const Z2Channel &,
       const Tof2Channel &, AbstractMultiChannelAnalyzer &>()
       [with_custodian_and_ward<1,4,
	with_custodian_and_ward<1,5,
	with_custodian_and_ward<1,6 > > > ()]
       )
      ;

    class_<AbstractMultiChannelAnalyzer, boost::noncopyable> 
      ("AbstractMultiChannelAnalyzer", no_init)
      .def("accept", &AbstractMultiChannelAnalyzer::accept)
      ;

    class_<Tof2Channel>
      ("Tof2Channel", init<double, double, double>())
      .def("__call__", &Tof2Channel::operator () )
      ;
      
    class_<Z2Channel>
      ("Z2Channel", 
       init<double, size_t, const Z2Channel::vector_t, const Z2Channel::vector_t>())
      .def("__call__", &Z2Channel::operator () )
      ;
      
    wrap_vector<int>( "int" ); // channel_t

  }
}


// version
// $Id$

// End of file 
