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


#ifndef MCNI_NEUTRON_EVENTBUFFER_H
#define MCNI_NEUTRON_EVENTBUFFER_H


#include "Event.h"


namespace mcni{ namespace Neutron {
    
    typedef std::vector<Event> Events;
    
    
    /// buffer of neutron events
    /*! to reduce the function calls to each neutron component, we pass a bunch
      of neutrons to a neutron component, instead of passing one neutron a time.
      This class represents a bucket of neutrons.
    */
    class EventBuffer : public Events{
      
    public:

      // types
      typedef Events base_t;
      
      // meta-methods
      EventBuffer( size_t n );
      EventBuffer();

      // methods
      /// snapshot of first n valid neutron events 
      /*! valid means the probability of the neutron event is positive.
	In simulation we use negative possibility to tag absorbed neutrons.
      */
      EventBuffer snapshot( size_t n );
    };
    
  }} //mcni::Neutron


#endif // MCNI_NEUTRON_EVENTBUFFER_H

// version
// $Id: neutron_buffer.h 598 2007-01-21 19:48:06Z linjiao $

// End of file
