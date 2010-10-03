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
#include <vector>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/geometry/Matrix3.h"
#include "mcni/geometry/RotationMatrix.h"
#include "mcni/neutron/Event.h"
#include "mcni/neutron/EventBuffer.h"
#include "mcni/geometry/coords_transform.h"
#include "mcni/neutron/coords_transform.h"
#include "mcni/test/assert.h"

using namespace mcni;

typedef Position<double> r_t;
typedef Velocity<double> v_t;
typedef RotationMatrix<double> rot_t;


// absolute --> relative 
void test1()
{
  r_t r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;

  Neutron::Event event( Neutron::State(r,v,s), 0, 1);

  r_t cs_pos(0,0,1);
  
  abs2rel( event, cs_pos );

  assertVectorAlmostEqual( event.state.position, r_t(1,2,2) );
  assertVectorAlmostEqual( event.state.velocity, v_t(1,2,3) );
}



void test2()
{
  r_t cs_pos(0,0,1), r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;
  Neutron::Event event( Neutron::State(r,v,s), 0, 1);

  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  abs2rel( event, cs_pos, rot );

  assertVectorAlmostEqual( event.state.position, r_t(2,-1,2) );
  assertVectorAlmostEqual( event.state.velocity, v_t(2,-1,3) );
}


// relative --> absolute
void test3()
{
  r_t r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;

  Neutron::Event event( Neutron::State(r,v,s), 0, 1);

  r_t cs_pos(0,0,1);
  
  rel2abs( event, cs_pos );

  assertVectorAlmostEqual( event.state.position, r_t(1,2,4) );
  assertVectorAlmostEqual( event.state.velocity, v_t(1,2,3) );
}

void test4()
{
  r_t cs_pos(0,0,1), r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;
  Neutron::Event event( Neutron::State(r,v,s), 0, 1);

  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  rel2abs( event, cs_pos, rot );

  assertVectorAlmostEqual( event.state.position, r_t(-2,1,4) );
  assertVectorAlmostEqual( event.state.velocity, v_t(-2,1,3) );
}


// batch
void test5()
{
  r_t r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;
  Neutron::Event event( Neutron::State(r,v,s), 0, 1);
  Neutron::Events events(1);
  events[0] = event;

  r_t cs_pos(0,0,1);
  
  rot_t rot( 1, 0, 0,
	     0, 1, 0,
	     0, 0, 1);
  
  abs2rel_batch( events, cs_pos, rot );

  assertVectorAlmostEqual( events[0].state.position, r_t(1,2,2) );
  assertVectorAlmostEqual( events[0].state.velocity, v_t(1,2,3) );
}

void test6()
{
  r_t r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;
  Neutron::Event event( Neutron::State(r,v,s), 0, 1);
  Neutron::Events events(1);
  events[0] = event;

  r_t cs_pos(0,0,1);
  
  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  abs2rel_batch( events, cs_pos, rot );

  assertVectorAlmostEqual( events[0].state.position, r_t(2,-1,2) );
  assertVectorAlmostEqual( events[0].state.velocity, v_t(2,-1,3) );
}

void test7()
{
  r_t r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;
  Neutron::Event event( Neutron::State(r,v,s), 0, 1);
  Neutron::Events events(1);
  events[0] = event;

  r_t cs_pos(0,0,1);
  
  rot_t rot( 1, 0, 0,
	     0, 1, 0,
	     0, 0, 1);
  
  rel2abs_batch( events, cs_pos, rot );

  assertVectorAlmostEqual( events[0].state.position, r_t(1,2,4) );
  assertVectorAlmostEqual( events[0].state.velocity, v_t(1,2,3) );
}

void test8()
{
  r_t r(1,2,3);
  v_t v(1,2,3);
  Neutron::Spin s;
  Neutron::Event event( Neutron::State(r,v,s), 0, 1);
  Neutron::Events events(1);
  events[0] = event;

  r_t cs_pos(0,0,1);
  
  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  rel2abs_batch( events, cs_pos, rot );

  assertVectorAlmostEqual( events[0].state.position, r_t(-2,1,4) );
  assertVectorAlmostEqual( events[0].state.velocity, v_t(-2,1,3) );
}

int main()
{
  test1();
  test2();
  test3();
  test4();
  test5();
  test6();
  test7();
  test8();
}

// version
// $Id$

// End of file 
