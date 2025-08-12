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


#include <cassert>
#include <iostream>
#include "mcni/test/assert.h"
#include "mccomponents/math/random/geometry.h"

using namespace std;
using namespace mccomponents::math;
char * jrnltag ="test_choose_direction";

typedef mcni::Vector3<double> V3;
using mcni::PI;


void test1()
{
  V3 dir;
  double theta, phi;

  const int Ntheta = 10, Nphi = 10;
  const int N1 = 10000;
  const int N = Ntheta*Nphi*N1;

  double I[Ntheta*Nphi];
  for (int i=0; i<Ntheta*Nphi; i++) 
    I[i] = 0;

  int itheta, iphi;
  

  for (int i=0; i<N; i++) {
    choose_direction(dir);
    mcni::assertAlmostEqual(dir.length(), 1.);
    
    theta = std::acos(dir.z);
    phi = std::atan2(dir.y, dir.x);
    
    // convert to cos(theta) because solid angle is sintheta dtheta dphi = d(costheta) dphi
    itheta = (std::cos(theta)+1)/2*Ntheta;
    iphi = (phi+PI)/2/PI * Nphi;

    /*
    std::cout << "theta=" << theta << ", "
	      << "phi = " << phi 
	      << std::endl;
    */
    I[itheta*Nphi + iphi] += 1;
  }

  double sigma = sqrt(N1);
  for (int i=0; i<Ntheta*Nphi; i++) {
    /*
    std::cout << "i=" << i << ", "
	      << "I=" << I[i] 
	      << std::endl;
    */
    if (isnan(I[i]))
      std::cout 
	<< "**Warning: "
	<< "i=" << i << ", "
	<< "I=" << I[i] 
	<< std::endl;
    mcni::assertAlmostEqual(I[i], N1, 3./sigma, 3*sigma);
  }
}


void test2()
{
  V3 dir, target(0, 0, 10);
  double radius = 3;
  double theta, phi;

  const int Ntheta = 10, Nphi = 10;
  const int N1 = 10000;
  const int N = Ntheta*Nphi*N1;
  
  double I[Ntheta*Nphi];
  for (int i=0; i<Ntheta*Nphi; i++) 
    I[i] = 0;

  int itheta, iphi, index;
  double sa, l;
  for (int i=0; i<N; i++) {
    sa = choose_direction(dir, target, radius);
    l = dir.length();
    mcni::assertAlmostEqual(l, 10.);
    mcni::assertAlmostEqual(sa, 0.264985, 1e-4, 1e-5);
    
    theta = std::acos(dir.z/l);
    phi = std::atan2(dir.y, dir.x);
    
    // convert to cos(theta) because solid angle is sintheta dtheta dphi = d(costheta) dphi
    itheta = (std::cos(theta)+1)/2*Ntheta;
    iphi = (phi+PI)/2/PI * Nphi;
    if (iphi==Nphi) iphi = Nphi-1;
    if (iphi>Nphi) throw mcni::Exception("phi index out of bound");

    /*
    std::cout << "theta=" << theta << ", "
	      << "phi = " << phi 
	      << std::endl;
    */
    index = itheta*Nphi + iphi;
    I[index] += 1;
  }

  double sigma = sqrt(N1*Ntheta);
  for (int i=0; i<Ntheta*Nphi; i++) {
    /*
    std::cout << "i=" << i << ", "
	      << "I=" << I[i] 
	      << std::endl;
    */
    if (isnan(I[i]))
      std::cout 
	<< "**Warning: "
	<< "i=" << i << ", "
	<< "I=" << I[i] 
	<< std::endl;
    if (i>=(Ntheta-1)*Nphi) 
      mcni::assertAlmostEqual(I[i], N1*Ntheta, 3./sigma, 3*sigma);
    else
      mcni::assertAlmostEqual(I[i], 0);
  }
}


void test3()
{
  V3 dir, target(10, 0, 0);
  double radius = 3;
  double theta, phi;

  const int Ntheta = 10, Nphi = 10;
  const int N1 = 10000;
  const int N = Ntheta*Nphi*N1;
  
  double I[Ntheta*Nphi];
  for (int i=0; i<Ntheta*Nphi; i++) 
    I[i] = 0;

  int itheta, iphi;
  double sa, l;
  for (int i=0; i<N; i++) {
    sa = choose_direction(dir, target, radius);
    l = dir.length();
    mcni::assertAlmostEqual(l, 10.);
    mcni::assertAlmostEqual(sa, 0.264985, 1e-4, 1e-5);
    
    theta = std::acos(dir.x/l);
    phi = std::atan2(dir.z, dir.y);
    
    // convert to cos(theta) because solid angle is sintheta dtheta dphi = d(costheta) dphi
    itheta = (std::cos(theta)+1)/2*Ntheta;
    iphi = (phi+PI)/2/PI * Nphi;

    /*
    std::cout << "theta=" << theta << ", "
	      << "phi = " << phi 
	      << std::endl;
    */
    I[itheta*Nphi + iphi] += 1;
  }

  double sigma = sqrt(N1*Ntheta);
  for (int i=0; i<Ntheta*Nphi; i++) {
    /*
    std::cout << "i=" << i << ", "
	      << "I=" << I[i] 
	      << std::endl;
    */
    if (isnan(I[i]))
      std::cout 
	<< "**Warning: "
	<< "i=" << i << ", "
	<< "I=" << I[i] 
	<< std::endl;
    if (i>=(Ntheta-1)*Nphi) 
      mcni::assertAlmostEqual(I[i], N1*Ntheta, 3./sigma, 3*sigma);
    else
      mcni::assertAlmostEqual(I[i], 0);
  }
}


int main()
{
  test1();
  test2();
  test3();
}

// version
// $Id$

// End of file 
