// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCCOMPONENTS_KERNELS_TOF2CHANNEL_H
#define MCCOMPONENTS_KERNELS_TOF2CHANNEL_H


namespace mccomponents {

  namespace detector {

    /// convert tof to a channel number
    class Tof2Channel {

    public:

      // meta methods
      /// ctor
      inline Tof2Channel( double tofmin, double tofmax, double tofstep );

      // methods
      inline int operator ()( double tof ) const;

    
    private:
      // data
      double m_tofmin, m_tofmax, m_tofstep;
    };

  } // detector::

} // mccomponents::


#include "Tof2Channel.icc"

#endif


// version
// $Id$

// End of file 
