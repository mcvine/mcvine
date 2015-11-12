// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 2004-2007  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#ifndef MCNI_NEUTRON_EVENT_CEVENT_CONVERSION_H
#define MCNI_NEUTRON_EVENT_CEVENT_CONVERSION_H

#include "cEvent.h"
#include "EventBuffer.h"

namespace mcni{ namespace Neutron {

    inline void event_fromCevent( Event & event, const cEvent & cevent )
    {
      event.state.position.x = cevent.x;
      event.state.position.y = cevent.y;
      event.state.position.z = cevent.z;

      event.state.velocity.x = cevent.vx;
      event.state.velocity.y = cevent.vy;
      event.state.velocity.z = cevent.vz;

      event.state.spin.s1 = cevent.s1;
      event.state.spin.s2 = cevent.s2;

      event.time = cevent.time;
      event.probability = cevent.probability;
    }
    
    inline void event_toCevent( const Event & event, cEvent & cevent )
    {
      cevent.x = event.state.position.x;
      cevent.y = event.state.position.y;
      cevent.z = event.state.position.z;

      cevent.vx = event.state.velocity.x;
      cevent.vy = event.state.velocity.y;
      cevent.vz = event.state.velocity.z;

      cevent.s1 = event.state.spin.s1;
      cevent.s2 = event.state.spin.s2;

      cevent.time = event.time;
      cevent.probability = event.probability;
    }
    
    void events_fromCevents( Events & events, const cEvent * cevents, size_t n);
    void events_toCevents( const Events & events, cEvent * cevents, size_t n);
    
  }  // Neutron:
} //mcni:


#endif // MCNI_NEUTRON_EVENT_CEVENT_CONVERSION_H

// version
// $Id$

// End of file
