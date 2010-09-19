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


#include <iostream>
#include <vector>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"

#include "mcni/neutron/cEvent.h"
#include "mcni/neutron/EventBuffer.h"
#include "mcni/neutron/event_cevent_conversion.h"

namespace mcni{ namespace Neutron {

    void events_fromCevents( Events & events, const cEvent * cevents, size_t n)
    {
      size_t N = std::min( events.size(), n );

      for (size_t i=0; i<N; i++) 
	event_fromCevent( events[i], *(cevents+i) ) ;
      
    }
    
    void events_toCevents( const Events & events, cEvent * cevents, size_t n)
    {
      size_t N = std::min( events.size(), n );

      for (size_t i=0; i<N; i++) 
	event_toCevent( events[i], *(cevents+i) ) ;
      
    }
    
  }  // Neutron:
} //mcni:



// version
// $Id: neutron_buffer.h 598 2007-01-21 19:48:06Z linjiao $

// End of file
