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
#include "mcni/geometry/Matrix3.h"
#include "mcni/geometry/RotationMatrix.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/geometry/coords_transform.h"
#include "mcni/test/assert.h"


using namespace mcni;


typedef Position<double> r_t;
typedef Velocity<double> v_t;
typedef RotationMatrix<double> rot_t;

// absolute --> relative
void test1()
{
  r_t cs_pos(0,0,1), r(1,2,3);
  
  abs2rel( r, cs_pos );

  assertVectorAlmostEqual( r, r_t(1,2,2) );
}

void test2()
{
  r_t cs_pos(0,0,1), r(1,2,3);
  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  abs2rel( r, cs_pos, rot );

  assertVectorAlmostEqual( r, r_t(2,-1,2) );
}

void test3()
{
  v_t v(1,2,3);
  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  abs2rel( v, rot );
  
  assertVectorAlmostEqual( v, v_t(2,-1,3) );
}


// relative --> absolute
void test4()
{
  r_t cs_pos(0,0,1), r(1,2,3);
  
  rel2abs( r, cs_pos );

  assertVectorAlmostEqual( r, r_t(1,2,4) );
}

void test5()
{
  r_t cs_pos(0,0,1), r(1,2,3);
  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  rel2abs( r, cs_pos, rot );

  assertVectorAlmostEqual( r, r_t(-2,1,4) );
}

void test6()
{
  v_t v(1,2,3);
  rot_t rot( 0, 1, 0,
	     -1, 0, 0,
	     0, 0, 1);
  
  rel2abs( v, rot );
  
  assertVectorAlmostEqual( v, v_t(2,-1,3) );
}



int main()
{
  test1();
  test2();
  test3();
}

// version
// $Id: testvector3.cc 310 2005-11-27 04:11:41Z linjiao $

// End of file 
