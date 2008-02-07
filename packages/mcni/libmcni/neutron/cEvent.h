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


#ifndef MCNI_NEUTRON_CEVENT_H
#define MCNI_NEUTRON_CEVENT_H

namespace mcni{ namespace Neutron {
    
    /// Neutron event c struct
    struct cEvent{
      double x,y,z;
      double vx,vy,vz;
      double s1, s2;
      double time, probability;
    };
    
    
  }  // Neutron:
} //mcni:


#endif // MCNI_NEUTRON_CEVENT_H

// version
// $Id: neutron_buffer.h 598 2007-01-21 19:48:06Z linjiao $

// End of file
