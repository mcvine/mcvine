// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2010  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include <iostream>
#include <cassert>
#include <string>
#include <cmath>
#include "fparser/fparser.hh"


int test1()
{
  std::string function = "sin(2*pi*x)";
  FunctionParser fparser;
  
  double pi = 3.1415926535897932;
  fparser.AddConstant("pi", pi);

  int res = fparser.Parse(function, "x");
  if (res>=0) {
    return 1;
  }
  
  double vals[] = {0};
  for (double x=0; x<1; x+=0.25) {
    vals[0] = x;
    double y = fparser.Eval(vals);
    // std::cout << "f(" << x << ") = " << y << std::endl;
    assert (y==std::sin(2*pi*x));
  }
  return 0;
}


int test2()
{
  std::string function = "Q+E", vars="Q,E";
  FunctionParser fparser;
  
  fparser.AddConstant("pi", 3.1415926535897932);

  int res = fparser.Parse(function, vars);
  if (res>=0) {
    std::cout << "failed to parse function " << function << " with vars " << vars << std::endl;
    return 1;
  }
  
  double vals[] = {0,0};
  for (double Q=0; Q<10; Q+=0.1) {
    for (double E=0; E<40; E+=0.5) {
      vals[0] = Q; vals[1] = E;
      double y = fparser.Eval(vals);
      // std::cout << "f(" << Q << "," << E << ") = " << y << std::endl;
      assert (std::abs(y-(Q+E)) < 1e-6);
    }
  }
  return 0;
}


int main()
{
  if (test1()) return 1;
  if (test2()) return 1;
  return 0;
}

// version
// $Id$

// End of file 
