// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                               Jiao Lin
//                        California Institute of Technology
//                         (C) 2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

#include <iostream>
#include "mcni/neutron/Ceventbuffer.h"

int main()
{
  using namespace std;
  //using namespace DANSE::Simulation;

  void * buf = neutron_buffer_initialize(2);
  double x=0, y=1, z=2, vx=3, vy=4, vz=5, t=6, s1=7, s2=8, p=9;

  neutron_buffer_set_ntrn(buf, 0, x,y,z,vx,vy,vz,t,s1,s2,p);

  neutron_buffer_get_ntrn(buf, 0, &x,&y,&z,&vx,&vy,&vz,&t,&s1,&s2,&p);
  cout << x <<","
       << y <<","
       << z <<","
       << vx <<","
       << vy <<","
       << vz <<","
       << t <<","
       << s1 <<","
       << s2 <<","
       << p <<endl;

  neutron_buffer_set_ntrn(buf, 0, 9,8,7,6,5,4,3,2,1,0);
  neutron_buffer_get_ntrn(buf, 0, &x,&y,&z,&vx,&vy,&vz,&t,&s1,&s2,&p);
  cout << x <<","
       << y <<","
       << z <<","
       << vx <<","
       << vy <<","
       << vz <<","
       << t <<","
       << s1 <<","
       << s2 <<","
       << p <<endl;


  neutron_buffer_set_ntrn_prob(buf, 1, -1);
  neutron_buffer_get_ntrn(buf, 1, &x,&y,&z,&vx,&vy,&vz,&t,&s1,&s2,&p);
  cout << x <<","
       << y <<","
       << z <<","
       << vx <<","
       << vy <<","
       << vz <<","
       << t <<","
       << s1 <<","
       << s2 <<","
       << p <<endl;
  cout << neutron_buffer_get_ntrn_prob(buf, 1) << endl;

  neutron_buffer_finalize(buf);

  return 0;
}
