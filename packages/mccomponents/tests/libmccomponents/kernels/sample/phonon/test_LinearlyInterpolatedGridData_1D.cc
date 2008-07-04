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


#include <cassert>
#include <iostream>
#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedGridData_1D.h"


void test()
{
  using namespace DANSE::phonon;

  typedef std::vector<double> array_t;
  typedef LinearlyInterpolatedGridData_1D< array_t, double > w_t;
  
  array_t array( 11 );
  w_t::axis_t X(0, 0.1, 10);
  
  for (w_t::index_t i=0; i<=X.n; i++) array[i] = 7*(0.1*i);

  w_t f( X, array );
  
  double x = 0.34;
  std::cout << f(x) << std::endl;
  assert ( std::abs( f(x) - 7*x ) < 0.01 ) ;
  assert ( f( 0 ) == 0 );
}

int main()
{
  test();
}


// version
// $Id$

// End of file 
