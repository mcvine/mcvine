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


#include <iostream>
#include "mcni/geometry/Vector3.h"
#include "mcni/neutron/Event.h"


using namespace mcni;

void basicTests()
{
  Vector3<double> v(0,0,3000), r(0,0,0);
  Neutron::Spin s;
  Neutron::State state(r,v,s);
  Neutron::Event ev(state, 0, 1);
  std::cout << ev << std::endl;
}


int main()
{
  basicTests();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
