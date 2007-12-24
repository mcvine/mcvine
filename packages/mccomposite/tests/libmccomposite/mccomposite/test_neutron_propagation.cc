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


#include <cassert>
#include <iostream>
#include "mcni/neutron.h"
#include "mccomposite/neutron_propagation.h"
#include "mccomposite/exception.h"

void test1()
{
  using namespace mcni;
  using namespace mccomposite;

  Neutron::Event ev, save;
  ev.state.position = mccomposite::geometry::Position(0,0,-5);
  ev.state.velocity = mccomposite::geometry::Direction(0,0,1);
  save = ev;

  geometry::Box box(2,2,2);

  propagate_to_next_out_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 6);


  ev = save;
  ev.state.position.z = 0.;
  propagate_to_next_out_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 1);

  ev = save;
  ev.state.position.z = -1;
  propagate_to_next_out_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2);

  ev = save;
  ev.state.position.z = -1-1e-10;
  propagate_to_next_out_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2+1e-10);

  ev = save;
  ev.state.position.z = -1+1e-10;
  propagate_to_next_out_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2-1e-10);
}

void test2()
{
  using namespace mcni;
  using namespace mccomposite;

  geometry::Box box(2,2,2);
  geometry::Union shape(box, box);

  Neutron::Event ev, save;
  ev.state.position = mccomposite::geometry::Position(0,0,-5);
  ev.state.velocity = mccomposite::geometry::Direction(0,0,1);
  save = ev;

  propagate_to_next_out_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 6);


  ev = save;
  ev.state.position.z = 0.;
  propagate_to_next_out_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 1);

  ev = save;
  ev.state.position.z = -1;
  propagate_to_next_out_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2);

  ev = save;
  ev.state.position.z = -1-1e-10;
  propagate_to_next_out_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2+1e-10);

  ev = save;
  ev.state.position.z = -1+1e-10;
  propagate_to_next_out_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2-1e-10);
}


void test3()
{
  using namespace mcni;
  using namespace mccomposite;

  geometry::Box box(2,2,2);
  geometry::Translation translated(box, geometry::Position(0,0,3));
  geometry::Union shape(box, translated);

  Neutron::Event ev, save;
  ev.state.position = mccomposite::geometry::Position(0,0,-5);
  ev.state.velocity = mccomposite::geometry::Direction(0,0,1);
  save = ev;

  propagate_to_next_out_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 6);

  ev = save;
  ev.state.position.z = 1.;
  try {
    propagate_to_next_out_surface(ev, shape);
    throw "If we reach here, it is bad";
  }
  catch (mccomposite::Exception e) {
    std::cout << "good, exception caught: " << e.what() << std::endl;
  }
  
}


int main()
{
  test1();
  test2();
  test3();
}

// version
// $Id$

// End of file 
