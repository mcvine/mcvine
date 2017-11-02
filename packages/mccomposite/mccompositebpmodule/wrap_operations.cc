// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include "mccomposite/geometry/operations.h"

#include <boost/python.hpp>


namespace wrap_mccomposite {

  template <typename T>
  const mccomposite::geometry::AbstractShape & get_body(const T &t)
  {
    return t.body;
  }


  void wrap_operations()
  {
    using namespace boost::python;
    using namespace mccomposite::geometry;
    typedef std::vector< const AbstractShape * > shapes_t;
       
    class_<Difference, bases<AbstractShape> >
      ("Difference", 
       init< const AbstractShape &, const AbstractShape &>()
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3> >()])
      .def_readonly("shapes", &Difference::shapes)
      ;

    class_<Union, bases<AbstractShape> >
      ("Union", 
       init< const AbstractShape &, const AbstractShape &>()
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3> >()])
      .def( init< const shapes_t & >()
	    [with_custodian_and_ward<1,2>()] )
      .def_readonly("shapes", &Union::shapes)
      ;

    class_<Intersection, bases<AbstractShape> >
      ("Intersection", 
       init< const AbstractShape &, const AbstractShape &>()
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3> >()])
      .def( init< const shapes_t & >()
	    [with_custodian_and_ward<1,2>()] )
      .def_readonly("shapes", &Intersection::shapes)
      ;

    class_<Dilation, bases<AbstractShape> >
      ("Dilation", 
       init< const AbstractShape &, double>()
       [with_custodian_and_ward<1,2>()]
       )
      ;

    class_<Rotation, bases<AbstractShape> >
      ("Rotation",
       init< const AbstractShape &,  const RotationMatrix &>()
       [with_custodian_and_ward<1,2>()] 
       )
      .def("get_body", &get_body<Rotation>, return_internal_reference<>())
      .def_readonly("rotmat", &Rotation::rotmat)
      ;

    class_<Translation, bases<AbstractShape> >
      ("Translation",
       init< const AbstractShape &,  const Vector &>()
       [with_custodian_and_ward<1,2>()] 
       )
      .def("get_body", &get_body<Translation>, return_internal_reference<>())
      .def_readonly("vector", &Translation::vector)
      ;
  }    
}


// version
// $Id$

// End of file 
