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
//libmccomposite/mccomposite/test_neutron_propagation.cc (Subprocess aborted)


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

  propagate_to_next_exiting_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 6);


  ev = save;
  ev.state.position.z = 0.;
  propagate_to_next_exiting_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 1);

  ev = save;
  ev.state.position.z = -1;
  propagate_to_next_exiting_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2);

  ev = save;
  ev.state.position.z = -1-1e-10;
  propagate_to_next_exiting_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2+1e-10);

  ev = save;
  ev.state.position.z = -1+1e-10;
  propagate_to_next_exiting_surface(ev, box);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2-1e-10);

  ev = save;
  ev.state.position.z = -5;
  propagate_to_next_incident_surface(ev, box);
  assert (ev.state.position.z == -1);
  assert (ev.time == 4);

  ev = save;
  ev.state.position.z = -1;
  propagate_to_next_incident_surface(ev, box);
  assert (ev.state.position.z == -1);
  assert (ev.time == 0);

  ev = save;
  ev.state.position.z = -1+1.e-10;


  // starting point is already at the
  // incident surface,  so we cannot propagate it to next incident surface
  //ev = save;
  //ev.state.position.z = -1+1.e-10;
  //propagate_to_next_incident_surface(ev, box);
  //assert (ev.state.position.z == +1.e-10);
  //assert (ev.time == 1);

  // starting point is already at the
  // incident surface,  so we cannot propagate it to next incident surface
  ev = save;
  ev.state.position.z = -1-1.e-10;
  propagate_to_next_incident_surface(ev, box);
  //assert (ev.state.position.z == -1-1.e-10);
  //assert (ev.time == 0);

  ev.state.position.z = -1;
  assert (tof_before_exit(ev, box) == 2);
  ev.state.position.z = 0;
  assert (tof_before_exit(ev, box) == 1);
  ev.state.position.z = 1;
  assert (tof_before_exit(ev, box) == 0);
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

  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 6);


  ev = save;
  ev.state.position.z = 0.;
  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 1);

  ev = save;
  ev.state.position.z = -1;
  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2);

  ev = save;
  ev.state.position.z = -1-1e-10;
  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2+1e-10);


  ev = save;
  ev.state.position.z = -1+1e-10;
  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 2-1e-10);

  ev = save;
  ev.state.position.z = -5;
  propagate_to_next_incident_surface(ev, box);
  assert (ev.state.position.z == -1);
  assert (ev.time == 4);

  ev = save;
  ev.state.position.z = -1;
  propagate_to_next_incident_surface(ev, box);
  assert (ev.state.position.z == -1);
  assert (ev.time == 0);

  // starting point is already at the
  // incident surface,  so we cannot propagate it to next incident surface
  //ev = save;
  //ev.state.position.z = -1+1.e-10;
  //propagate_to_next_incident_surface(ev, box);
  //assert (ev.state.position.z == -1+1.e-10);
  //assert (ev.time == 0);

  // starting point is already at the
  // incident surface,  so we cannot propagate it to next incident surface
  //ev = save;
  //ev.state.position.z = -1-1.e-10;
  //propagate_to_next_incident_surface(ev, box);
  //assert (ev.state.position.z == -1-1.e-10);
  //assert (ev.time == 0);

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

  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 6);

  ev = save;
  ev.state.position.z = 1.;
  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 1);
  assert (ev.time == 0);

  // starting point is already at the
  // incident surface,  so we cannot propagate it to next incident surface
  //ev = save;
  //ev.state.position.z = 1.+1.e-10;
  //propagate_to_next_exiting_surface(ev, shape);
  //assert (ev.state.position.z == 1.+1.e-10);
  //assert (ev.time == 0);

  // starting point is already at the
  // incident surface,  so we cannot propagate it to next incident surface
  //ev = save;
  //ev.state.position.z = 1.-1.e-10;
  //propagate_to_next_exiting_surface(ev, shape);
  //assert (ev.state.position.z == 1.-1.e-10);
  //assert (ev.time == 0);

  ev = save;
  ev.state.position.z = 1.+1.e-3;
  propagate_to_next_exiting_surface(ev, shape);
  assert (ev.state.position.z == 4);
  assert (ev.time == 3-1.e-3);

  ev = save;
  ev.state.position.z = 1;
  propagate_to_next_incident_surface(ev, shape);
  assert (ev.state.position.z ==2);
  assert (ev.time == 1);

  ev = save;
  ev.state.position.z = 1+1.e-10;
  propagate_to_next_incident_surface(ev, shape);
  assert (ev.state.position.z ==2);
  assert (ev.time == 1-1.e-10);

  //ev = save; not supported as stating it is not able to propagate
  //ev.state.position.z = 1-1.e-10;
  //propagate_to_next_incident_surface(ev, shape);
  //assert (ev.state.position.z ==2);
  //assert (ev.time == 1+1.e-10);

}


void test4()
{
  using namespace mcni;
  using namespace mccomposite;

  geometry::Box box(2,2,2);

  Neutron::Event ev;
  ev.state.velocity = mccomposite::geometry::Direction(0,0,1);

  ev.state.position = mccomposite::geometry::Position(0,0,-5);
  assert (is_exiting( ev, box ) == 0);

  ev.state.position = mccomposite::geometry::Position(0,0,1);
  assert (is_exiting( ev, box ) == 1);

  ev.state.position = mccomposite::geometry::Position(0,0,2);
  assert (is_exiting( ev, box ) == 1);

}


void test5()
{
  using namespace mcni;
  using namespace mccomposite;

  Neutron::Event ev;
  ev.state.position = mccomposite::geometry::Position(0,0,-5);
  ev.state.velocity = mccomposite::geometry::Direction(0,0,1);
  assert (is_moving( ev ) == 1);

  ev.state.velocity = mccomposite::geometry::Direction(0,0,0);
  assert (is_moving( ev ) == 0);

}



int main()
{
  test1();
  test2();
  test3();
  test4();
  test5();
}

// version
// $Id$

// End of file

// version
// $Id$

// End of file 
