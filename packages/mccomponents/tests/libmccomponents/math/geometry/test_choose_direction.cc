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

#include "journal/debug.h"

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


int main()
{
#ifdef DEBUG
  //  journal::debug_t("mccomposite.geometry.ArrowIntersector").activate();
  //  journal::debug_t(jrnltag).activate();
#endif
  test1();
}

// version
// $Id$

// End of file 
