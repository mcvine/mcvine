// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                       California Institute of Technology
//                       (C) 2004-2007  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 

/*! C library of neutron buffer.
  To be used by mcstas components.
 */

#ifndef MCNI_NEUTRON_CEVENTBUFFER_H
#define MCNI_NEUTRON_CEVENTBUFFER_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

  //!Initialization
  void * neutron_buffer_initialize(size_t size);
  
  //!set  neutron state
  void neutron_buffer_set_ntrn
  ( void *buf, size_t ind,
    double x, double y, double z,
    double vx, double vy, double vz,
    double t, double s1, double s2, double p);

  //!get  neutron state
  void neutron_buffer_get_ntrn
  ( void *buf, size_t ind,
    double *x, double *y, double *z,
    double *vx, double *vy, double *vz, 
    double *t, double *s1, double *s2, double *p);
  
  //!set probability of  neutron
  void neutron_buffer_set_ntrn_prob(void *buf, size_t ind, double p);

  //!get probability of  neutron
  double neutron_buffer_get_ntrn_prob(void *buf, size_t ind);

  //!Finishing
  void neutron_buffer_finalize(void *buf);

#ifdef __cplusplus
}
#endif


#endif //MCNI_NEUTRON_CEVENTBUFFER_H

