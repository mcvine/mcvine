// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <iostream>
#include <cassert>
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedGridData_3D.h"
#include "histogram/NdArray.h"


void test()
{
  using namespace DANSE::phonon;

  typedef DANSE::Histogram::NdArray<double *, double, unsigned int, size_t, 3>
    array_3d;
  
  typedef LinearlyInterpolatedGridData_3D< array_3d, double > w_t;
  
  double data[ 11*11*11 ];
  w_t::index_t shape[3] = {11,11,11};
  w_t::dataarray_t array( data, shape );
  w_t::axis_t X(0, 0.1, 10), Y(1, 0.1, 10), Z(5, 0.1, 10);
  
  w_t::index_t indexes[3];
  w_t::index_t & ix = indexes[0];
  w_t::index_t & iy = indexes[1];
  w_t::index_t & iz = indexes[2];
  for (ix = 0; ix <= X.n; ix ++ )
    for (iy = 0; iy <= Y.n; iy ++ )
      for (iz = 0; iz <= Z.n; iz ++ ) {
	double x = X.start + X.step * ix;
	double y = Y.start + Y.step * iy;
	double z = Z.start + Z.step * iz;
	array[ indexes ] = x+y+z;
      }

  w_t f( X,Y,Z, array );
  
  double x = 0.34, y=1.29, z = 5.87;
  assert ( std::abs( f(x,y,z) - (x+y+z) ) < 0.01 ) ;
}

int main()
{
  test();
}


// version
// $Id$

// End of file 
