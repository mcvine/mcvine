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


#ifndef MCNI_NEUTRON_EVENT_H
#define MCNI_NEUTRON_EVENT_H

#include "Spin.h"
#include "State.h"


// forward declaration
namespace mcni { namespace Neutron {
    struct Event;
  } // Neutron:
} // mcni:


// declare outside any namespace to avoid a gcc bug that will prevent
// journal codes from compiling
std::ostream & operator <<
( std::ostream &os, const mcni::Neutron::Event & s ) ;


namespace mcni{ namespace Neutron {
    
    /// Neutron event
    /*! This class is supposed to have all the information of a neutron.
      Objects of NeutronEvent will be passed to any neutron component that
      will do scatterings. Neutron component will update the event after a
      scattering process is done.
      
      Currently a neutron event has following information:
      - neutron state: velocity, position, spin
      - time: how long has it been away from moderator?
      - probability: this is for the ease of doing Monte-Carlo simulation.
      We follow the practice taken in the McStas package; we update 
      the probability of an event anytime it is scattered, by
      multiplying the original probability
      by the probability of the current scattering process.
    */
    struct Event{

      // types
      typedef State state_t;
      
      // meta-methods
      inline Event( const State &state, double time, double probability );
      inline Event();
      
      // methods
      /// print to an output stream.
      /// useful for operator <<
      inline void print( std::ostream &os) const ;
      /// neutron energy
      inline double energy( ) const { return state.energy(); }
      /// operator ==
      inline bool operator==(const Event & other) const {
        return state==other.state && time==other.time && probability==other.probability;
      }
      // data
      State state;
      double time, probability; 
    };
    
    
  }  // Neutron:
} //mcni:


#include "Event.icc"

#endif // MCNI_NEUTRON_EVENT_H

// version
// $Id$

// End of file
