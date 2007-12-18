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
#include "mcni/test/assert.h"

class Scatterer: public mcni::AbstractNeutronScatterer{
public:
  Scatterer() : mcni::AbstractNeutronScatterer() {}
  virtual void scatter(mcni::Neutron::Event &) 
  {
  }
};

void test1()
{
  using namespace mcni;

  Scatterer s;
  Neutron::Event ev;
  s.scatter( ev );

  s.absorb( ev );

  Neutron::Events evts;
  s.scatterM( (const Neutron::Event &)ev, evts );
}


int main()
{
  test1();
}

// version
// $Id$

// End of file 
