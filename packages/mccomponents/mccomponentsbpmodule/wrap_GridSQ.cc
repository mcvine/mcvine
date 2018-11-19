// -*- C++ -*-
//
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/AbstractSQ.h"
#include "mccomponents/kernels/sample/SQ/GridSQ.h"


namespace wrap_mccomponents {

  using namespace mccomponents::sample;

  double fx_get( const fx & fx, const double & x) 
  {
    return fx(x);
  }

  fx * new_fx( double xbegin, double xend, double xstep,
	       std::vector<double> & v )
  {
    return new fx( xbegin, xend, xstep, v.begin() );
  }

  void wrap_GridSQ()
  {
    using namespace boost::python;

    typedef GridSQ w_t;

    class_<w_t, bases<mccomponents::sample::AbstractSQ>, boost::noncopyable >
      ("GridSQ",
       init<const fx &>()
       [with_custodian_and_ward<1,2> () ]
       )
      ;
    
    class_<fx>
      ("fx", no_init)
      .def( "__call__", fx_get)
      ;
    
    def( "new_fx", new_fx, 
	 with_custodian_and_ward_postcall<0,7,
	 return_value_policy< manage_new_object > > () )
      ;

    
  }

}


// End of file 
