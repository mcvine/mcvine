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


#include <boost/python.hpp>
#include "mccomposite/AbstractNeutronScatterer.h"
#include "mccomposite/geometry/intersect.h"

namespace wrap_mccomposite {

  void wrap_AbstractNeutronScatterer()
  {
    using namespace boost::python;

    class_<mccomposite::AbstractNeutronScatterer, bases<mcni::AbstractNeutronScatterer>,
      boost::noncopyable>
      ("AbstractNeutronScatterer", no_init)
      .def("shape", &mccomposite::AbstractNeutronScatterer::shape, return_internal_reference<>())
      ;

  }

  size_t countIntersections(const mcni::Neutron::Event &n, const mccomposite::AbstractShape & shape)
  {
    using namespace mccomposite::geometry;
    Arrow arrow(n.state.position, n.state.velocity);
    ArrowIntersector::distances_t dists = intersect(arrow, shape);
    return dists.size();
  }

  void wrap_countIntersections()
  {
    using namespace boost::python;

    def("countIntersections", countIntersections);
  }
}


// version
// $Id$

// End of file 
