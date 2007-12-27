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
  void wrap_geometers();
  void wrap_AbstractNeutronScatterer();
  void wrap_scatterercontainer();
  void wrap_CompositeNeutronScatterer();
}


BOOST_PYTHON_MODULE(mccompositebp)
{
  using namespace boost::python;
  using namespace wrap_mccomposite;

  wrap_geometers();
  wrap_AbstractNeutronScatterer();
  wrap_scatterercontainer();
  wrap_CompositeNeutronScatterer();
}


// version
// $Id: mccompositebpmodule.cc 658 2007-10-24 21:33:08Z linjiao $

// End of file 
