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
#include <vector>
#include <algorithm>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/EventBuffer.h"


mcni::Neutron::EventBuffer::EventBuffer( size_t n )
  : base_t(n)
{}


mcni::Neutron::EventBuffer::EventBuffer()
  : base_t() 
{}


bool 
isInValid(const mcni::Neutron::Event &evt)
{
  return evt.probability == -1;
}

mcni::Neutron::EventBuffer::EventBuffer
mcni::Neutron::EventBuffer::snapshot( size_t n )
{
  EventBuffer valid_evts;
  
  std::remove_copy_if( this->begin(), this->begin()+n,
		  back_inserter(valid_evts),
		  isInValid);
  return valid_evts;
}



// version
// $Id: neutron_buffer.h 598 2007-01-21 19:48:06Z linjiao $

// End of file
