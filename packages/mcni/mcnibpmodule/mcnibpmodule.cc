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


void wrap_Vector3s();
void wrap_Matrix3s();
void wrap_geometry();
void wrap_neutron();
void wrap_abstractneutronscatterer();
void wrap_abstractneutroncomponent();
void wrap_dummycomponent();


BOOST_PYTHON_MODULE(mcnibp)
{
  using namespace boost::python;
  wrap_Vector3s();
  wrap_Matrix3s();
  wrap_geometry();
  wrap_neutron();
  wrap_abstractneutronscatterer();
  wrap_abstractneutroncomponent();
  wrap_dummycomponent();
}


// version
// $Id: mcnibpmodule.cc 658 2007-10-24 21:33:08Z linjiao $

// End of file 
