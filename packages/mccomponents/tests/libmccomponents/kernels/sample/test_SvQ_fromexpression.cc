// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2007-2014  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include <cmath>
#include <iostream>
#include <cassert>
#include "mccomponents/kernels/sample/SQE/SvQ_fromexpression.h"


void test1()
{
  using namespace mccomponents::sample;
  SvQ_fromExpr svq("s");
  
  std::cout << svq(1,0,0) << std::endl;
  assert (svq(1,0,0) == 1./4./mcni::PI);
  
  SvQ_fromExpr svq2("0.3106*exp(-16.816*s*s)+0.7198*exp(-7.0487*s*s)-0.0521*exp(-0.3020*s*s)+0.0221");
  std::cout << svq2(0,0,0) << std::endl;
  std::cout << svq2(2*mcni::PI/8.87*2, 2*mcni::PI/8.87, 0) << std::endl;
  
  SvQ_fromExpr svq3("(1-(cos(4.435*Qx)*cos(4.435*Qz)))/2/sqrt(1-(cos(4.435*Qx)*cos(4.435*Qz))^2)");
  
  SvQ_fromExpr svq4("(1-(cos(4.435*Qx)*cos(4.435*Qz)))/2/sqrt(1-(cos(4.435*Qx)*cos(4.435*Qz))^2)*(0.3106*exp(-16.816*s*s)+0.7198*exp(-7.0487*s*s)-0.0521*exp(-0.3020*s*s)+0.0221)");
  
  double Qx = 0.1, Qz = 2*mcni::PI/8.87, Qy=0;
  std::cout << svq3(Qx,Qy,Qz) << std::endl;
  std::cout << svq4(Qx,Qy,Qz) << std::endl;
  std::cout << svq4(Qx,Qy,Qz)/svq3(Qx,Qy,Qz) << std::endl;
  Qx = 2*mcni::PI/8.87*2+0.1;
  std::cout << svq4(Qx,Qy,Qz)/svq3(Qx,Qy,Qz) << std::endl;
}


int main()
{
  test1();
  return 0;
}

// version
// $Id: test_SQE_fromexpression.cc 601 2010-10-03 19:55:29Z linjiao $

// End of file 
