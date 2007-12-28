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

  void wrap_operations()
  {
    using namespace boost::python;
    using namespace mccomposite::geometry;


    class_<Difference, bases<AbstractShape> >
      ("Difference", 
       init< const AbstractShape &, const AbstractShape &>()
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3> >()])
      ;

    typedef std::vector< const AbstractShape * > shapes_t;
       
    class_<Union, bases<AbstractShape> >
      ("Union", 
       init< const AbstractShape &, const AbstractShape &>()
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3> >()])
      .def( init< const shapes_t & >()
	    [with_custodian_and_ward<1,2>()] )
      ;

    class_<Intersection, bases<AbstractShape> >
      ("Intersection", 
       init< const AbstractShape &, const AbstractShape &>()
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3> >()])
      .def( init< const shapes_t & >()
	    [with_custodian_and_ward<1,2>()] )
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
      ;

    class_<Translation, bases<AbstractShape> >
      ("Translation",
       init< const AbstractShape &,  const Vector &>()
       [with_custodian_and_ward<1,2>()] 
       )
      ;
  }    
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
