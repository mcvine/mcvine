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
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedPolarizationOnGrid_3D.h"
#include "histogram/NdArray.h"


void test()
{
  typedef DANSE::Histogram::NdArray<double *, double, unsigned int, size_t, 5>
    array_5d_t;
  
  typedef DANSE::phonon::LinearlyInterpolatedPolarizationOnGrid_3D< array_5d_t > w_t;
  
  double data[ 11*11*11*3*2 ];
  w_t::index_t shape[5] = {11,11,11,3,2};
  array_5d_t array( data, shape );

  w_t::axis_t QX(0, 0.1, 10), QY(0, 0.1, 10), QZ(0, 0.1, 10);
  
  w_t::index_t indexes[5];
  w_t::index_t & ix = indexes[0];
  w_t::index_t & iy = indexes[1];
  w_t::index_t & iz = indexes[2];
  w_t::index_t & idir = indexes[3];
  w_t::index_t & iri = indexes[4];
  for (ix = 0; ix <= QX.n; ix ++ )
    for (iy = 0; iy <= QY.n; iy ++ )
      for (iz = 0; iz <= QZ.n; iz ++ ) 
	for (idir =0; idir<3; idir ++) 
	  for (iri = 0; iri<2; iri++) {
	    double x = QX.start + QX.step * ix;
	    double y = QY.start + QY.step * iy;
	    double z = QZ.start + QZ.step * iz;
	    array[ indexes ] = (x+y+z) * (idir*10+iri);
	  }

  w_t epsilon_f( QX,QY,QZ, array );
  
  double x = 0.34, y=0.29, z = 0.87;

  w_t::epsilon_t eps = epsilon_f( w_t::K_t(x, y, z) );
  std::cout << eps << std::endl;

  double t = x+y+z;
  assert ( std::abs( eps.x.real() - 0*t ) < 0.001 ) ;
  assert ( std::abs( eps.x.imag() - 1*t ) < 0.001 ) ;
  assert ( std::abs( eps.y.real() - 10*t ) < 0.001 ) ;
  assert ( std::abs( eps.y.imag() - 11*t ) < 0.001 ) ;
  assert ( std::abs( eps.z.real() - 20*t ) < 0.001 ) ;
  assert ( std::abs( eps.z.imag() - 21*t ) < 0.001 ) ;
}

int main()
{
  test();
}


// version
// $Id$

// End of file 
