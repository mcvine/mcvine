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
#include "fparser/fparser.hh"


int test1()
{
  std::string function = "sin(2*pi*x)";
  FunctionParser fparser;
  
  fparser.AddConstant("pi", 3.1415926535897932);

  int res = fparser.Parse(function, "x");
  if (res>=0) {
    return 1;
  }
  
  double vals[] = {0};
  for (double x=0; x<1; x+=0.25) {
    vals[0] = x;
    double y = fparser.Eval(vals);
    std::cout << "f(" << x << ") = " << y << std::endl;
  }
}


int main()
{
  test1();
  return 0;
}

// version
// $Id$

// End of file 
