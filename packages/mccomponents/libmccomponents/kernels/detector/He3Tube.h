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


#ifndef MCCOMPONENTS_KERNELS_HE3TUBE_H
#define MCCOMPONENTS_KERNELS_HE3TUBE_H

#include <vector>
#include "He3.h"
#include "AbstractMultiChannelAnalyzer.h"
#include "Tof2Channel.h"
#include "Z2Channel.h"


namespace mccomponents {

  namespace kernels {

    /// scattering kernel for He3 tube
    class He3Tube: public He3 {

    public:

      // types
      /// type of channels of the tube in the detector system
      typedef detector::AbstractMultiChannelAnalyzer::channels_t channels_t;

      // meta methods
      /// ctor
      /// pressure: pressure of tube. unit: pascal
      /// tube_channels: channels of the tube in the detector system (channel number(s))
      ///   for example, this tube is 3rd tube in the 20th 8-pack of the detector
      ///   system, channels = (19, 2).
      /// z2channel: neutron coordinates -> channel number
      /// tof2channel: tof->channel number
      He3Tube( double pressure, 
	       const channels_t & tube_channels,
	       const detector::Z2Channel & z2channel,
	       const detector::Tof2Channel & tof2channel,
	       detector::AbstractMultiChannelAnalyzer & mca
	       );

      // methods
      virtual void absorb( mcni::Neutron::Event & ev );
      
    private:
      // data
      /// channels
      channels_t m_tube_channels;
      /// coordinates->channel number 
      const detector::Z2Channel & m_z2channel;
      /// tof->channel converter
      const detector::Tof2Channel &m_tof2channel;
      /// multichannel analyzer
      detector::AbstractMultiChannelAnalyzer & m_mca;
    };

  } // kernels::

} // mccomponents::


#endif


// version
// $Id$

// End of file 
