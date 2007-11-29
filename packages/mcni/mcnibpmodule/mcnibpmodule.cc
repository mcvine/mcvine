// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2005 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>


void wrapVector3s();


BOOST_PYTHON_MODULE(mcnibp)
{
  using namespace boost::python;
  wrapVector3s();
}


// version
// $Id: simulation_common_boostmodule.cc 658 2007-10-24 21:33:08Z linjiao $

// Generated automatically by CxxMill on Mon Apr 11 16:43:04 2005

// End of file 
