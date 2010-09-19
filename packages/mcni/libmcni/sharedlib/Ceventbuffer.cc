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

/*! C library of neutron_buffer to be used by mcstas components
 */

#include <iostream>
#include <utility>
#include <string>
#include <vector>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/EventBuffer.h"
#include "mcni/neutron/Ceventbuffer.h"
#include "mcni/test/exception.h"


using namespace mcni::Neutron;


//helper
void checkBuffer(void *bufferPtr)
{
  if (bufferPtr==NULL) {
    std::cerr<<"Buffer has not been initialized!";
    throw mcni::Exception("buffer not initd");
  }
}



// methods

#ifdef __cplusplus
extern "C"
#endif
void * neutron_buffer_initialize(size_t size)
{
  EventBuffer *bufferPtr;
  bufferPtr = new EventBuffer(size);
  
  return static_cast<void *>(bufferPtr);
}


#ifdef __cplusplus
extern "C"
#endif
void neutron_buffer_set_ntrn
(void *bufferPtr, size_t idx,
 double x, double y, double z,
 double vx, double vy, double vz, 
 double t, double s1, double s2, double p)
{
  checkBuffer(bufferPtr);
  EventBuffer &buffer = *( static_cast<EventBuffer *>(bufferPtr) );
  
  State ns(State::position_t(x,y,z),
	   State::velocity_t(vx,vy,vz),
	   Spin(s1,s2));
  
  buffer[idx] = Event(ns, t, p);
}


#ifdef __cplusplus
extern "C"
#endif
void neutron_buffer_set_ntrn_prob
(void *bufferPtr, size_t idx, double p)
{
  checkBuffer(bufferPtr);
  EventBuffer &buffer = *( static_cast<EventBuffer *>(bufferPtr) );
  buffer[idx].probability = p;
}

#ifdef __cplusplus
extern "C"
#endif
void neutron_buffer_get_ntrn
( void *bufferPtr, size_t idx,
  double *x, double *y, double *z, double *vx, double *vy, double *vz, 
  double *t, double *s1, double *s2, double *p)
{
  checkBuffer(bufferPtr);
  
  EventBuffer &buffer = *( static_cast<EventBuffer *>(bufferPtr) );
  
  const Event &evt = buffer[idx];
  const State &state = evt.state;
  
  *x = state.position.x;
  *y = state.position.y;
  *z = state.position.z;
  
  *vx = state.velocity.x;
  *vy = state.velocity.y;
  *vz = state.velocity.z;
  
  *s1 = state.spin.s1;
  *s2 = state.spin.s2;
  
  *t=evt.time;
  *p=evt.probability;
}


#ifdef __cplusplus
extern "C"
#endif
double neutron_buffer_get_ntrn_prob
(void *bufferPtr, size_t idx)
{
  checkBuffer(bufferPtr);
  
  EventBuffer &buffer = *( static_cast<EventBuffer *>(bufferPtr) );
  
  const Event &evt = buffer[idx];
  
  return evt.probability;
}


#ifdef __cplusplus
extern "C"
#endif
void neutron_buffer_finalize(void *bufferPtr)
{
  checkBuffer(bufferPtr);
  EventBuffer *buffer_ptr = static_cast<EventBuffer *>(bufferPtr);
  delete buffer_ptr;
}

