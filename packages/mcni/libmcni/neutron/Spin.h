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


#ifndef MCNI_NEUTRON_SPIN_H
#define MCNI_NEUTRON_SPIN_H


// forward declaration for operator << s
namespace mcni { namespace Neutron {

    struct Spin;

}} // mcni::Neutron



// declare them outside any namespace to avoid a gcc bug that will prevent
// journal codes from compiling
std::ostream & operator <<
( std::ostream &os, const mcni::Neutron::Spin & s ) ;



namespace mcni { namespace Neutron {

    /// neutron spin.
    /// TODO: might want to change to use three numbers, sx,sy,sz (normalized to one)
    struct Spin{

      // meta-methods
      inline Spin(double i_s1, double i_s2);
      inline Spin();

      
      // methods
      /// print to an output stream.
      /// This is useful to support << operator 
      inline void print( std::ostream &os ) const;

 
      // data
      double s1, s2;

    };
  
  } // Neutron:
} //mcni:


#include "Spin.icc"

#endif // MCNI_NEUTRON_SPIN_H


// version
// $Id: neutron_buffer.h 598 2007-01-21 19:48:06Z linjiao $

// End of file
