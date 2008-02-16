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
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedDispersionOnGrid_3D.h"
#include "histogram/NdArray.h"


void test()
{
  using namespace DANSE::Histogram;
  using namespace DANSE::phonon;

  typedef NdArray<double *, double, unsigned int, size_t, 7> array_7d_t;
  typedef NdArray<double *, double, unsigned int, size_t, 4> array_4d_t;
  
  typedef LinearlyInterpolatedDispersionOnGrid_3D< array_7d_t, array_4d_t > w_t;
  
  double eps_data[ 11*11*11*15*5*3*2 ];
  w_t::n_t eps_shape[7] = {11,11,11,15,5,3,2};
  array_7d_t eps_array( eps_data, eps_shape );

  double E_data[ 11*11*11*15 ];
  w_t::n_t E_shape[4] = {11,11,11,15};
  array_4d_t E_array( E_data, E_shape );

  const w_t::axis_t QX(0, 0.1, 10), QY(0, 0.1, 10), QZ(0, 0.1, 10);
  
  w_t::n_t indexes[7];
  w_t::n_t & ix = indexes[0];
  w_t::n_t & iy = indexes[1];
  w_t::n_t & iz = indexes[2];
  w_t::n_t & ibranch = indexes[3];
  w_t::n_t & iatom = indexes[4];
  w_t::n_t & idir = indexes[5];
  w_t::n_t & iri = indexes[6];

  for (ix = 0; ix <= QX.n; ix ++ )
    for (iy = 0; iy <= QY.n; iy ++ )
      for (iz = 0; iz <= QZ.n; iz ++ ) {
	double x = QX.start + QX.step * ix;
	double y = QY.start + QY.step * iy;
	double z = QZ.start + QZ.step * iz;

	for (ibranch = 0; ibranch<15; ibranch++) {
	  for (iatom = 0; iatom < 5; iatom ++ )
	    for (idir =0; idir<3; idir ++) 
	      for (iri = 0; iri<2; iri++) {
		eps_array[ indexes ] = (x+y+z) + ibranch*10000 + iatom*100 + idir*10 + iri;
	      }
	  E_array[indexes] = (x+y+z) + ibranch*10000;
	}
      }

  w_t disp( (w_t::n_t)5, QX,QY,QZ, eps_array, E_array );
  
  double x = 0.34, y=0.29, z = 0.87;
  w_t::n_t branch = 7, atom = 2;

  w_t::epsilon_t eps = disp.polarization( branch, atom, w_t::K_t(x, y, z) );
  std::cout << eps << std::endl;

  double t = x+y+z + branch* 10000 + atom*100;
  assert ( std::abs( eps.x.real() - t ) < 0.001 ) ;
  assert ( std::abs( eps.x.imag() - (t+1) ) < 0.001 ) ;
  assert ( std::abs( eps.y.real() - (10+t) ) < 0.001 ) ;
  assert ( std::abs( eps.y.imag() - (11+t) ) < 0.001 ) ;
  assert ( std::abs( eps.z.real() - (20+t) ) < 0.001 ) ;
  assert ( std::abs( eps.z.imag() - (21+t) ) < 0.001 ) ;

  w_t::float_t E = disp.energy( branch, w_t::K_t(x,y,z) );
  assert ( std::abs( E - (x+y+z+branch*10000) ) < 0.001 );
}

int main()
{
  test();
}


// version
// $Id$

// End of file 
