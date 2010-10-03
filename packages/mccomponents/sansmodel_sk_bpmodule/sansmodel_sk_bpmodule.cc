// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2008 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>

namespace wrap_models{
  void wrap_cylinder();
  void wrap_ellipsoid();
  void wrap_elliptical_cylinder();
  void wrap_sphere();
  void wrap_core_shell();
  void wrap_core_shell_cylinder();
}


BOOST_PYTHON_MODULE(sansmodel_sk_bp)
{
  using namespace boost::python;
  using namespace wrap_models;

  wrap_cylinder();
  wrap_ellipsoid();
  wrap_elliptical_cylinder();
  wrap_sphere();
  wrap_core_shell();
  wrap_core_shell_cylinder();
}


// version
// $Id$

// End of file 
