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


#ifndef MCCOMPONENTS_ABSTRACTMULTICHANNELANALYZER_H
#define MCCOMPONENTS_ABSTRACTMULTICHANNELANALYZER_H


#include <vector>


namespace mccomponents {

  namespace detector {

    class AbstractMultiChannelAnalyzer {
    public:

      //types
      typedef std::vector< int > channels_t;

      //meta methods
      virtual ~AbstractMultiChannelAnalyzer() {};

      //methods
      /// accept an event.
      /// channels: channels[i] is the number of the ith channel at which the event happened.
      ///   For example, if third channel is for time-of-flight, channel[2] = 777 means
      ///   that the event happened at tof channel #777. 
      ///   #777 could mean, for example, 3777 microsecond of time of flight.
      /// n: number of particles in this event. In MC simulation, this is the probability
      ///   of the event.
      virtual void accept( const channels_t & channels, double n ) = 0;
    };

  } //detector::

} // mccomponents::


#endif


// version
// $Id$

// End of file 
