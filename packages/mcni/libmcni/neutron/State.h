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
      typedef Position<double> position_t;
      typedef Velocity<double> velocity_t;
      typedef Spin spin_t;

      // meta-methods
      inline State(const position_t &i_position, 
		   const velocity_t &i_velocity,
		   const spin_t & i_s) ;
      inline State();
      
      // methdos
      /// energy of neutron
      inline double energy( ) const;
      /// print to an output stream.
      /// Useful for defining operator << 
      inline void print( std::ostream &os ) const;

      // data
      position_t position;
      velocity_t velocity;
      spin_t spin;
    };
    
  }  // Neutron:
} //mcni:


#include "State.icc"

#endif // NEUTRON_NEUTRON_STATE_H

// version
// $Id$

// End of file
