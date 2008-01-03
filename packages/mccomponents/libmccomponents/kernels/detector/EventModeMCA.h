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
    /// the event is  { pixelID, tofChannelNo, n }
    /// It is assumed that there are only three channels: detector, pixel, tof
    /// pixelID is calculated from channels[0]*npixels + channels[1].
    /// tofChannelNo = channels[2].
    /// So this means that the pixelID is the global unique ID for any pixel.
    class EventModeMCA: public AbstractMultiChannelAnalyzer {
    public:
      // types
      typedef unsigned int index_t;

      struct Event {
	index_t pixelID, tofChannelNo;
	double n; 
      };


      // metat methods
      /// ctor
      EventModeMCA( const char * outfilename, 
		    const index_t & npixels);
      virtual ~EventModeMCA();
      
      // methods
      virtual void accept( const channels_t & channels, double n );
      
    private:
      //data
      std::ofstream m_out;
      index_t m_npixels;
    };
  }

}

#endif

// version
// $Id$

// End of file 
