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
#include "mcni/AbstractNeutronComponent.h"
#include "mcni/process_neutron_events.h"
#include "mcni/test/assert.h"

using namespace mcni;


class Component: public AbstractNeutronComponent{
public:
  Component(const char * name): AbstractNeutronComponent(name) {}
  virtual void scatter(Neutron::Event &) 
  {
  }
};


void test1()
{
  Component component("component");
  Neutron::Event ev;
  component.scatter( ev );
}

void test2()
{
  Component component("component");
  Neutron::Events evts(100);
  process( component, evts );
}


int main()
{
  test1();
  test2();
}

// version
// $Id$

// End of file 
