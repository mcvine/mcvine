// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

#include <vector>

namespace bpext { 

  using namespace boost::python;
  typedef std::vector<double> vec_d;

  vec_d * new_vec_d( size_t n ) 
  {
    return new vec_d(n);
  }

  void wrap()
  {
    class_<vec_d>
      ("vec_d", init<unsigned int>())
      .def( vector_indexing_suite<vec_d> () )
      ;

    def( "new_vec_d", new_vec_d, return_value_policy< manage_new_object >() );

  }

} // bpext

// version
// $Id$

// End of file
