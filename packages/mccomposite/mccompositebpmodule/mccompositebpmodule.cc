// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2007 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>

namespace wrap_mccomposite{
  void wrap_basics();

  void wrap_AbstractShape();
  void wrap_shapeoperators();

  void wrap_shapecontainer();
  void wrap_primitives();
  void wrap_operations();

  void wrap_geometers();
  void wrap_AbstractNeutronScatterer();
  void wrap_scatterercontainer();
  void wrap_CompositeNeutronScatterer();
}


BOOST_PYTHON_MODULE(mccompositebp)
{
  using namespace boost::python;
  using namespace wrap_mccomposite;

  wrap_basics();

  wrap_AbstractShape();
  wrap_shapeoperators();

  wrap_shapecontainer();
  wrap_primitives();
  wrap_operations();

  wrap_geometers();
  wrap_AbstractNeutronScatterer();
  wrap_scatterercontainer();
  wrap_CompositeNeutronScatterer();
}


// version
// $Id: mccompositebpmodule.cc 658 2007-10-24 21:33:08Z linjiao $

// End of file 
