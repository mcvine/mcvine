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
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/Event.h"
#include "mcni/test/assert.h"

using namespace mcni;

void test_basics()
{
  Position<double> r(0,0,0);
  Velocity<double> v(0,0,3000);

  Neutron::Spin s;
  Neutron::State state(r,v,s);
  Neutron::Event ev(state, 0, 1);
  std::cout << ev << std::endl;
  assertAlmostEqual( ev.energy(), 47.043, 2 );
}

void test2()
{
  typedef Position<double> r_t;
  typedef Velocity<double> v_t;

  v_t v(0,0,3000); r_t r(0,0,0);
  Neutron::Spin s;
  Neutron::State state(r,v,s);
  Neutron::Event ev(state, 0, 1);
  assertVectorAlmostEqual( v, ev.state.velocity );
  assertVectorAlmostEqual( r, ev.state.position );
  assertAlmostEqual( ev.time, 0 );
  assertAlmostEqual( ev.probability, 1 );
  assertAlmostEqual( ev.state.spin.s1, s.s1 );
  assertAlmostEqual( ev.state.spin.s2, s.s2 );  
}

int main()
{
  test_basics();
  test2();
}

// version
// $Id$

// End of file 
