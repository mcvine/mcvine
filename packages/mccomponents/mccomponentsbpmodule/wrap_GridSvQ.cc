// -*- C++ -*-
//
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/AbstractSvQ.h"
#include "mccomponents/kernels/sample/SQ/GridSvQ.h"


namespace wrap_mccomponents {

  using namespace mccomponents::sample;

  double fxyz_get( const fxyz & fxyz, double x, double y, double z)
  {
    return fxyz(x, y, z);
  }

  fxyz * new_fxyz(double xbegin, double xend, double xstep,
                  double ybegin, double yend, double ystep,
                  double zbegin, double zend, double zstep,
                  std::vector<double> & v )
  {
    return new fxyz( xbegin, xend, xstep, ybegin, yend, ystep, zbegin, zend, zstep, v.begin() );
  }

  void wrap_GridSvQ()
  {
    using namespace boost::python;

    typedef GridSvQ w_t;

    class_<w_t, bases<mccomponents::sample::AbstractSvQ>, boost::noncopyable >
      ("GridSvQ",
       init<const fxyz &>()
       [with_custodian_and_ward<1,2> () ]
       )
      ;

    class_<fxyz>
      ("fxyz", no_init)
      .def( "__call__", fxyz_get)
      ;

    def( "new_fxyz", new_fxyz,
         with_custodian_and_ward_postcall<0, 10,
         return_value_policy< manage_new_object > > () )
      ;
  }
}

// End of file
