// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2007-2011  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef H_MCCOMPONENTS_EVENT2QE
#define H_MCCOMPONENTS_EVENT2QE

#include "histogram/Event2Quantity.h"

namespace mccomponents{ namespace reduction {

    USING_HISTOGRAM_NAMESPACE;

    // Event -> pixelID, energy transfer
    template <typename event_t, typename float_t>
    class Event2QE: public Event2Quantity2<event_t, float_t>
    {
    public:
      // meta methods
      /// ctor.
      /// Constructor. 
      /// Ei: neutron incident energy. meV
      /// pixelPositions: mapping of pixelID --> position 
      ///     pixelPositions[pixelID*3, pixelID*3+1, pixelID*3+2] is the position vector
      /// tofUnit: unit of tof in the event struct. 
      ///          for example, for 100ns, tofUnit = 1e-7
      /// mod2sample: distance from moderator to sample. unit: meter
      /// tofset: shutter tof offset. unit: microsecond
      /// tofmax: maximum tof. unit: microsecond
      ///         the default value corresponds to the case where
      ///         The moderator frequency is 60 Hz
      ///         so any data with tof > 1/60. should be not real
      Event2QE
      ( float_t Ei,
	const float_t * pixelPositions, 
	unsigned int ntotpixels = (1+115)*8*128,
	float_t tofUnit=1e-7, float_t mod2sample=13.5,
	float_t toffset = 0.0,
	float_t tofmax = 15000.
	);
      
      // methods
      float_t operator() ( const event_t & e, float_t &Q, float_t & E ) const ;
      
    private:

      //data
      float_t m_Ei, m_vi, m_ki;
      const float_t * m_pixelPositions;
      float_t m_tofUnit;
      float_t m_mod2sample;
      float_t m_ntotpixels;
      float_t m_toffset;
      float_t m_tofmax;
    };
  
  }}


#include "Event2QE.icc"

#endif // H_MCCOMPONENTS_EVENT2QE


// version
// $Id$

// End of file 
  
