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
#include "mcni/AbstractNeutronScatterer.h"
#include "mcni/process_neutron_events.h"
#include "mcni/test/assert.h"

using namespace mcni;


class Scatterer: public AbstractNeutronScatterer{
public:
  Scatterer() {}
  virtual void scatter(Neutron::Event &) const 
  {
  }
};

void test1()
{
  Scatterer s;
  Neutron::Event ev;
  s.scatter( ev );
}

void test2()
{
  Scatterer s;
  Neutron::Events evts(100);
  process( (const Scatterer *)&s, evts );
}


int main()
{
  test1();
  test2();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
