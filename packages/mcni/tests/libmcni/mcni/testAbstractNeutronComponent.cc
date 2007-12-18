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
  virtual void scatterM(const Neutron::Event & ev, Neutron::Events & evts)
  {
    evts.push_back(ev);
    evts.push_back(ev);
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

void test3()
{
  Component component("component");
  Neutron::Events evts(100);
  processM( component, evts );
  assert (evts.size() == 200);
}

void test4()
{
  Component component("component");
  Neutron::Events evts(100);
  for (size_t i = 0; i<10; i++) evts[i].probability = -1;
  processM( component, evts );
  assert (evts.size() == 180);
}


int main()
{
  test1();
  test2();
  test3();
  test4();
}

// version
// $Id$

// End of file 
