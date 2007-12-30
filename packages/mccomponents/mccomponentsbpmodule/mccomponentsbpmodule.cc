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

namespace wrap_mccomponents{
  void wrap_HomogeneousNeutronScatterer();
}


BOOST_PYTHON_MODULE(mccomponentsbp)
{
  using namespace boost::python;
  using namespace wrap_mccomponents;

  wrap_HomogeneousNeutronScatterer();
}


// version
// $Id: mccompositebpmodule.cc 658 2007-10-24 21:33:08Z linjiao $

// End of file 
