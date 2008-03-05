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

#ifndef MCCOMPONENTS_KERNELS_DETECTOR_EVENTMODEMCA_H
#define MCCOMPONENTS_KERNELS_DETECTOR_EVENTMODEMCA_H


#include <vector>
#include <fstream>
#include "AbstractMultiChannelAnalyzer.h"


namespace mccomponents {

  namespace detector {
    
    /// write every event to a data file
    /// The event is  { pixelID, tofChannelNo, n }
    /// The pixelID is the global unique ID for any pixel.
    /// For example, let us assume that there are only three channels:
    ///     detector, pixel, tof
    ///   pixelID is calculated from channels[0]*npixels + channels[1].
    ///   tofChannelNo = channels[2].
    ///   npixels is given in the dims array as dims[0].
    /// 
    class EventModeMCA: public AbstractMultiChannelAnalyzer {
    public:
      // types
      typedef unsigned int index_t;
      typedef std::vector<index_t> indexes_t;

      struct Event {
	index_t pixelID, tofChannelNo;
	double n; 
      };


      // metat methods
      /// ctor
      /// outfilename: binary output file name
      /// dims: dimensions of detector indexes. 
      /// For example, if we have 100 detector packs, each pack has 8 tubes, 
      /// each tube has 128 pixels,
      ///   dims = 100, 8, 128
      EventModeMCA( const char * outfilename, const indexes_t & dims);
      virtual ~EventModeMCA();
      
      // methods
      /// accept an event by knowing all channel numbers and the number
      /// of particles for the event.
      /// channels: channel numbers. 
      ///   For example, an event at pixel 31 of detector 3 of pack 25
      ///   at tof channel 2122, 
      ///      channels = (25, 3, 31, 2122)
      /// n: number of particles in the event
      virtual void accept( const channels_t & channels, double n );
      
    private:
      //data
      std::ofstream m_out;
      indexes_t m_dims;
      Event m_buffer;
    };
  }

}

#endif

// version
// $Id$

// End of file 
