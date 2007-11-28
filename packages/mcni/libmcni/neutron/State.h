// -*- C++ -*-
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                 Jiao Lin
//                      California Institute of Technology
//                      (C) 2004-2007  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 


#ifndef MCNI_NEUTRON_STATE_H
#define MCNI_NEUTRON_STATE_H

// forward declaration for operator << s
namespace mcni { namespace Neutron {
    
    struct Spin;
    struct State;
    
  }
} // mcni::Neutron


// declare outside any namespace to avoid a gcc bug that will prevent
// journal codes from compiling
std::ostream & operator <<
( std::ostream &os, const mcni::Neutron::State & s ) ;


namespace mcni { namespace Neutron {
    
    /// neutron state
    /// This class holds information about the state of a neutron.
    /// It knows about:
    ///   - position
    ///   - velocity
    ///   - spin
    ///
    struct State{

      // types
      typedef Vector3<double> vector3_t;

      // meta-methods
      inline State(const vector3_t &i_position, 
		   const vector3_t &i_velocity,
		   const Spin & i_s) ;
      inline State();
      
      // methdos
      /// print to an output stream.
      /// Useful for defining operator << 
      inline void print( std::ostream &os ) const;

      // data
      vector3_t position, velocity;
      Spin spin;
    };
    
  }  // Neutron:
} //mcni:


#include "State.icc"

#endif // NEUTRON_NEUTRON_STATE_H

// version
// $Id: neutron_buffer.h 598 2007-01-21 19:48:06Z linjiao $

// End of file
