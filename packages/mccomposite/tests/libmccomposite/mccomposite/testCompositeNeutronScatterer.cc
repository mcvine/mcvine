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
#include "mccomposite/CompositeNeutronScatterer.h"
#include "mccomposite/neutron_propagation.h"
#include "mccomposite/geometry/shapes.h"
#include "mcni/test/assert.h"
#include "mccomposite/geometry/shape2ostream.h"
#include "mccomposite/vector2ostream.h"


class Nothing: public mccomposite::AbstractNeutronScatterer{
public:
  Nothing(const mccomposite::geometry::AbstractShape & shape) 
    : AbstractNeutronScatterer( shape ) 
  {}
  InteractionType interact_path1(mcni::Neutron::Event &ev) 
  {
    mccomposite::propagate_to_next_out_surface( ev, shape() );
    return none;
  }
};

class Forwarding: public mccomposite::AbstractNeutronScatterer{
public:
  Forwarding(const mccomposite::geometry::AbstractShape & shape) 
    : AbstractNeutronScatterer( shape ) 
  {}
  InteractionType interact_path1(mcni::Neutron::Event & ev) 
  {
    mccomposite::propagate_to_next_out_surface( ev, shape() );
    return scattering;
  }
};

// half time forwarding, half time nothing
class HalfForwarding: public mccomposite::AbstractNeutronScatterer{
public:
  HalfForwarding(const mccomposite::geometry::AbstractShape & shape,
	     bool i_1sttime_is_forwarding) 
    : AbstractNeutronScatterer( shape ),
      forwarding(i_1sttime_is_forwarding)
  {}
  InteractionType interact_path1(mcni::Neutron::Event & ev) 
  {
    mccomposite::propagate_to_next_out_surface( ev, shape() );
    InteractionType itype;
    if (forwarding) itype = scattering;
    else itype = none;
    forwarding ^= 1;
    return itype;
  }
  bool forwarding;
};

// scatter and forwarding. good to test multiple-scattering
// "scattered" neutrons are always (1,0,0)
class Scattering_and_Forwarding: public mccomposite::AbstractNeutronScatterer{
public:
  Scattering_and_Forwarding
  (const mccomposite::geometry::AbstractShape & shape)
    : AbstractNeutronScatterer( shape )
  {}
  InteractionType interact_path1(mcni::Neutron::Event & ev) 
  {
    mccomposite::propagate_to_next_out_surface( ev, shape() );
    return scattering;
  }
  
  InteractionType interactM_path1(const mcni::Neutron::Event & ev, mcni::Neutron::Events & evts) 
  {
    mcni::Neutron::Event ev1=ev;
    interact_path1( ev1 );
    evts.push_back(ev1);
    
    mcni::Neutron::Event ev2;
    ev2.state.velocity = mccomposite::geometry::Direction(1,0,0);
    ev2.state.position = mccomposite::geometry::Position(0,0,0);
    interact_path1( ev2 );
    evts.push_back( ev2 );
    return scattering;
  }
  
  bool forwarding;
};

// simple. a box that does nothing to neutron
void test1()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Nothing s(box);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s );
  
  Geometer<AbstractNeutronScatterer> g;
  CompositeNeutronScatterer cs( box, scatterers, g );

  mcni::Neutron::Event ev;
  assert (cs.interact_path1( ev )==AbstractNeutronScatterer::none);
}

// simple. a box just just forwards any input neutron.
// It actually does nothing to neutrons. But we call it scattering
// here just for fun.
void test2()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Forwarding s(box);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s );

  std::cout << scatterers << std::endl;

  Geometer<AbstractNeutronScatterer> g;
  CompositeNeutronScatterer cs( box, scatterers, g );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Event save = ev;

  assert (cs.interact_path1( ev )==AbstractNeutronScatterer::scattering);
//   assert (ev.state.position.z == 0.5);
//   assert (ev.time == 5.5);
}


// two boxes. both just forward neutrons. 
// box1 at (0,0,0), box2 at (0,0,2).
void test3()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Forwarding s1(box), s2(box);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s1 );
  scatterers.push_back( &s2 );

  typedef CompositeNeutronScatterer::geometer_t geometer_t;
  geometer_t g;
  g.remember( s2, geometer_t::position_t(0,0,2), geometer_t::orientation_t() );

  geometry::Translation translated(box, g.getPosition( s2 ) );
  geometry::Union frameshape(box, translated);
  CompositeNeutronScatterer cs( frameshape, scatterers, g );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Event save = ev;

  assert (cs.interact_path1( ev ) == AbstractNeutronScatterer::scattering);
  assert (abs(ev.state.position.z-0.5) < 1.e-5 );
  assert (ev.time == 5.5);

  ev = save;
  cs.scatter(ev);
  assert (abs(ev.state.position.z-2.5) < 1.e-5 );
  assert (ev.time == 7.5);
}


// a box and a spherical shell. the box just forwards the neutron.
// the spherical shell does nothing.
void test4()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Forwarding s1(box);

  geometry::Sphere sphere1( 2), sphere2( 2.1 );
  geometry::Difference shell(sphere2, sphere1);
  Nothing s2(shell);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s1 );
  scatterers.push_back( &s2 );

  typedef CompositeNeutronScatterer::geometer_t geometer_t;
  geometer_t g;

  geometry::Union frameshape(box, shell);
  CompositeNeutronScatterer cs( frameshape, scatterers, g );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Event save = ev;
  assert (cs.interact_path1( ev ) == AbstractNeutronScatterer::scattering);
  assert (ev.state.position.z == 0.5 );
  assert (ev.time == 5.5 );

  ev = save;
  cs.scatter( ev ) ;
  assert (abs(ev.state.position.z-2.1) < 1.e-5 );
  assert (ev.time == 7.1);
}


// a box and a spherical shell. the box just forwards the neutron.
// the spherical shell does nothing. This is different from test4
// in frameshape.
void test4a()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Forwarding s1(box);

  geometry::Sphere sphere1( 2), sphere2( 2.1 );
  geometry::Difference shell(sphere2, sphere1);
  Nothing s2(shell);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s1 );
  scatterers.push_back( &s2 );

  typedef CompositeNeutronScatterer::geometer_t geometer_t;
  geometer_t g;

  CompositeNeutronScatterer cs( sphere2, scatterers, g );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Event save = ev;
  assert (cs.interact_path1( ev ) == AbstractNeutronScatterer::scattering);
  assert (abs(ev.state.position.z-2.1) < 1.e-5 );
  assert (ev.time == 7.1);
}


// a box and a spherical shell. the box forwards the neutron.
// the spherical shell does nothing or forwards the neutron half/half.
void test5()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Forwarding s1(box);

  geometry::Sphere sphere1( 2), sphere2( 2.1 );
  geometry::Difference shell(sphere2, sphere1);
  HalfForwarding s2(shell,1);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s1 );
  scatterers.push_back( &s2 );

  typedef CompositeNeutronScatterer::geometer_t geometer_t;
  geometer_t g;

  geometry::Union frameshape(box, shell);
  CompositeNeutronScatterer cs( frameshape, scatterers, g );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Event save = ev;

  assert (cs.interact_path1( ev ) == AbstractNeutronScatterer::scattering);
  assert (ev.state.position.z == -2 );
  assert (ev.time == 3 );

  ev = save;
  assert (cs.interact_path1( ev ) == AbstractNeutronScatterer::scattering);
  assert (ev.state.position.z == 0.5 );
  assert (ev.time == 5.5 );

  ev = save;
  cs.scatter( ev ) ;
  assert (abs(ev.state.position.z-2.1) < 1.e-5 );
  assert (ev.time == 7.1);
}


// a box and a spherical shell. the box forwards and satters the neutron.
// the spherical shell does nothing.
void test6()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Scattering_and_Forwarding s1(box);

  geometry::Sphere sphere1( 2), sphere2( 2.1 );
  geometry::Difference shell(sphere2, sphere1);
  Nothing s2(shell);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s1 );
  scatterers.push_back( &s2 );

  typedef CompositeNeutronScatterer::geometer_t geometer_t;
  geometer_t g;

  geometry::Union frameshape(box, shell);
  CompositeNeutronScatterer cs( frameshape, scatterers, g );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Events evts;
  cs.interactM_path1( ev, evts ) ;
  for (size_t i=0; i<evts.size(); i++)
    std::cout <<  evts[i] << std::endl;

  assert (evts.size() == 1);
  assert (std::abs(evts[0].state.position.z+2) < 1.e-5 );
  assert (evts[0].time == 3);

  evts.clear();
  cs.scatterM( ev, evts ) ;
//   assert (evts.size() == 2);
//   assert (evts[0].state.position.z == 2.1 );
//   assert (evts[0].time == 7.1);
//   assert (evts[0].state.velocity.z == 1);
//   assert (evts[1].state.position.x == 2.1 );
//   assert (evts[1].state.velocity.x == 1);
}


// a box and a spherical shell. both forward and satter the neutron.
void test7()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Scattering_and_Forwarding s1(box);

  geometry::Sphere sphere1( 2), sphere2( 2.1 );
  geometry::Difference shell(sphere2, sphere1);
  Scattering_and_Forwarding s2(shell);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s1 );
  scatterers.push_back( &s2 );

  typedef CompositeNeutronScatterer::geometer_t geometer_t;
  geometer_t g;

  geometry::Union frameshape(box, shell);
  CompositeNeutronScatterer cs( frameshape, scatterers, g );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Events evts;
  cs.interactM_path1( ev, evts ) ;
  for (size_t i=0; i<evts.size(); i++)
    std::cout <<  evts[i] << std::endl;

  assert (evts.size() == 2);
  assert (std::abs(evts[0].state.position.z+2) < 1.e-5 );
  assert (evts[0].time == 3);

  evts.clear();

  cs.scatterM( ev, evts ) ;
  // there must be five neutrons
  // four of them going to x direction, one of them going to z direction
  // this is fun!
  std::cout << evts << std::endl;
  assert (evts.size() == 5);
}


int main()
{
#ifdef DEBUG
  journal::debug_t("mccomposite.geometry.ArrowIntersector").activate();
  journal::debug_t("mccomposite.geometry.Locator").activate();
  journal::debug_t("CompositeNeutronScatterer_Impl").activate();
#endif
     test1();
      test2();
       test3();
       test4();
     test5();
    test6();
    test7();
}

// version
// $Id$

// End of file 
