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
#include "mcni/neutron.h"
#include "mccomposite/Geometer.h"

struct Element {};
typedef mccomposite::Geometer<Element> Geometer;

void test1()
{
  Geometer g;
  Element e;
  g.remember( e, Geometer::position_t(0,0,0), Geometer::orientation_t(1,0,0,0,1,0,0,0,1) );
  std::cout << g.getPosition( e ) << std::endl;
  std::cout << g.getOrientation( e ) << std::endl;
}


int main()
{
  test1();
}

// version
// $Id$

// End of file 
