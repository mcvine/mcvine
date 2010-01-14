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
#include "mccomponents/kernels/sample/phonon/interpolate.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif


struct functor {
  double a, b, c, d, e, f, g, h;
  functor(double ia, double ib,double ic,double id,double ie,double iff, double ig, double ih):
    a(ia), b(ib), c(ic), d(id),
    e(ie), f(iff), g(ig), h(ih)
  {}
  
  double operator()(double x, double y, double z) {
    return this->a+this->b*x + this->c*y + this->d*z\
      + this->e*y*z + this->f*x*z + this->g*x*y + this->h*x*y*z;
  }

};


void test1()
{
  
  functor f(1, 2, 3, 4, 5, 6, 7, 8);
  double u000 = f(0,0,0), u100 = f(1,0,0), u010 = f(0,1,0), u001 = f(0,0,1);
  double u110 = f(1,1,0), u101 = f(1,0,1), u011 = f(0,1,1), u111 = f(1,1,1);
  
  for (double x = 0; x<1; x+=0.1)
    for (double y = 0; y<1; y+=0.1)
      for (double z = 0; z<1; z+=0.1) {
	double t = interp3D_01(u000, u100, u010, u001,
			       u011, u101, u110, u111,
			       x,y,z);
	assert( t == f(x,y,z) );
      }
  
}


int main()
{
#ifdef DEBUG
  //journal::debug_t("HomogeneousNeutronScatterer").activate();
#endif
  test1();
  return 0;
}

// version
// $Id$

// End of file 
