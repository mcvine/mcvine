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
#include "mccomponents/kernels/sample/AbstractSQE.h"
#include "mccomponents/kernels/sample/SQE/GridSQE.h"


namespace wrap_mccomponents {

  using namespace mccomponents::sample;

  double fxy_get( const fxy & fxy, const double & x, const double & y) 
  {
    return fxy(x,y);
  }

  fxy * new_fxy( double xbegin, double xend, double xstep,
		 double ybegin, double yend, double ystep,
		 std::vector<double> & v )
  {
    return new fxy( xbegin, xend, xstep,
		    ybegin, yend, ystep,
		    v.begin() );
  }

  void wrap_GridSQE()
  {
    using namespace boost::python;

    typedef GridSQE w_t;

    class_<w_t, bases<mccomponents::sample::AbstractSQE>, boost::noncopyable >
      ("GridSQE",
       init<const fxy &>()
       [with_custodian_and_ward<1,2> () ]
       )
      ;
    
    class_<fxy>
      ("fxy", no_init)
      .def( "__call__", fxy_get)
      ;
    
    def( "new_fxy", new_fxy, 
	 with_custodian_and_ward_postcall<0,7,
	 return_value_policy< manage_new_object > > () )
      ;

    
  }

}


// version
// $Id$

// End of file 
