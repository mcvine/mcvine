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


/*
 Jiao Lin
 Caltech
 linjiao@caltech.edu
 (c) 2004
*/


#ifndef INTERPOLATE_H
#define INTERPOLATE_H

template <typename FloatType>
FloatType interp1D_01(FloatType y0, FloatType y1, FloatType x);
/* y0 = y(0), y1 = y(1), for any 0<x<1, return y(x) */

template <typename FloatType>
FloatType interp1D(FloatType xbegin, FloatType xend, 
		   FloatType ybegin, FloatType yend,
		   FloatType x);
/* y(xbegin) = ybegin, y(xend) = xend
   return y(x)
*/

template <typename FloatType>
FloatType interp2D_01(FloatType z00, FloatType z10, FloatType z01, 
		      FloatType z11, FloatType x, FloatType y);
/*
given z(0,0), z(0,1), z(1,0), z(1,1)
for ang 0<x<1, 0<y<1, return z(x,y)
*/

template <typename FloatType>
FloatType interp2D(FloatType xb, FloatType xe, FloatType yb, FloatType ye, 
		   FloatType zbb, FloatType zeb, FloatType zbe, FloatType zee,
		   FloatType x, FloatType y);
/* 
given z(xb,yb), z(xe, yb), z(xb,ye), z(xe,ye)
      xb,xe, yb,ye
      x,y
return z(x,y)
*/

template <typename FloatType>
FloatType interp3D_01(FloatType u000, FloatType u100, FloatType u010, 
		      FloatType u001, FloatType u011, FloatType u101, 
		      FloatType u110, FloatType u111,
		      FloatType x, FloatType y, FloatType z);
/*
given u(0,0,0), u(1,0,0), ..., u(1,1,1)
for any 0<x<1, 0<y<1, 0<z<1, 
return u(x,y,z)
*/

template <typename FloatType>
FloatType interp3D(FloatType x0, FloatType x1, 
		   FloatType y0, FloatType y1, 
		   FloatType z0, FloatType z1,
		   FloatType u000, FloatType u100, FloatType u010,
		   FloatType u001, FloatType u011, FloatType u101, 
		   FloatType u110, FloatType u111,
		   FloatType x, FloatType y, FloatType z);


template <typename FloatType>
FloatType interp1D_01(FloatType y0, FloatType y1, FloatType x)
/* y0 = y(0), y1 = y(1), for any 0<x<1, return y(x) */
{
  return y0+x*(y1-y0);
}

template <typename FloatType>
FloatType interp1D(FloatType xbegin, FloatType xend, FloatType ybegin, FloatType yend,
     FloatType x)
/* y(xbegin) = ybegin, y(xend) = xend
   return y(x)
*/
{
  return interp1D_01(ybegin, yend, (x-xbegin)/(xend-xbegin));
}

template <typename FloatType>
FloatType interp2D_01(FloatType z00, FloatType z10, FloatType z01, FloatType z11,
   FloatType x, FloatType y)
/*
given z(0,0), z(0,1), z(1,0), z(1,1)
for ang 0<x<1, 0<y<1, return z(x,y)

algorithm:
 z ~= a+bx+cy+dxy

 a = z00; c = z01-z00; b = z10-z00;
 d = z11-a-b-c = z11-z00-z10+z00-z01+z00 = z11+z00-z10-z01
*/
{
  FloatType d = z11+z00-z10-z01;
  return z00+(z10-z00)*x+(z01-z00)*y+d*x*y;
}

template <typename FloatType>
FloatType interp2D(FloatType xb, FloatType xe, FloatType yb, FloatType ye, 
   FloatType zbb, FloatType zeb, FloatType zbe, FloatType zee,
   FloatType x, FloatType y)
/* 
given z(xb,yb), z(xe, yb), z(xb,ye), z(xe,ye)
      xb,xe, yb,ye
      x,y
return z(x,y)
algorithm see `interp2D_01`
*/
{
  return interp2D_01(zbb, zeb, zbe, zee, 
   (x-xb)/(xe-xb), (y-yb)/(ye-yb) );
}

template <typename FloatType>
FloatType interp3D_01(FloatType u000, FloatType u100, FloatType u010, FloatType u001,
   FloatType u011, FloatType u101, FloatType u110, FloatType u111,
   FloatType x, FloatType y, FloatType z)
/*
given u(0,0,0), u(1,0,0), ..., u(1,1,1)
for any 0<x<1, 0<y<1, 0<z<1, 
return u(x,y,z)

algorithm 
 u ~= a+bx+cy+dz+eyz+fxz+gxy+hxyz

 a=u000; b=u100-u000; c=u010-u000; d=u001-u000;
 e=u011-a-c-d; f=u101-a-b-d; g=u110-a-b-c;
 h=u111-a-b-c-d-e-f-g;
*/
{
 FloatType a,b,c,d,e,f,g,h;

 a=u000; b=u100-u000; c=u010-u000; d=u001-u000;
 e=u011-a-c-d; f=u101-a-b-d; g=u110-a-b-c;
 h=u111-a-b-c-d-e-f-g;
 
 return a+b*x+c*y+d*z+e*y*z+f*x*z+g*x*y+h*x*y*z;
}

template <typename FloatType>
FloatType interp3D(FloatType x0, FloatType x1, 
		FloatType y0, FloatType y1, 
		FloatType z0, FloatType z1,
		FloatType u000, FloatType u100, FloatType u010, FloatType u001,
		FloatType u011, FloatType u101, FloatType u110, FloatType u111,
		FloatType x, FloatType y, FloatType z)
{
  return interp3D_01(u000, u100, u010, u001,
		     u011, u101, u110, u111,
		     (x-x0)/(x1-x0), (y-y0)/(y1-y0), (z-z0)/(z1-z0));
}


#endif



// version
// $Id$

// End of file 
