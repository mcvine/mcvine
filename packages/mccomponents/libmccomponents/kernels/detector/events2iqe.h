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


// XXX: this file should be inside a reduction library
// XXX: and in here we only need to specialize this method.
// XXX: to use the event struct (EventModeMCA::Event)
// XXX: and the event2qe functor (Event2QE)


#ifndef H_MCCOMPONENTS_EVENTS2IQE
#define H_MCCOMPONENTS_EVENTS2IQE

#include "Event2QE.h"
#include "histogram/EvenlySpacedGridData_2D.h"
#include "histogram/events2EvenlySpacedIxy.h"

namespace mccomponents{ namespace reduction {

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
    template <typename event_t, 
	      typename float_t, 
	      typename event_it_t,
	      typename float_it_t
	      >
    void 
    events2iqe
    ( 
     // input events
     const event_it_t & evts_begin, const event_it_t & evts_end,
     // output
     const float_it_t & output_intensities_begin,
     // output histogram bin parameters
     float_t Qbegin, float_t Qend, float_t dQ,
     float_t Ebegin, float_t Eend, float_t dE,
     // event -> qe conversion parameters
     float_t Ei,
     const float_t * pixelPositions, 
     unsigned int ntotpixels = (1+115)*8*128,
     float_t tofUnit=1e-7, float_t mod2sample=13.5,
     float_t toffset = 0.0, float_t tofmax = 15000.
      )
    {
      // event->q,e functor
      typedef Event2QE<event_t, float_t> e2qe_t;
      e2qe_t e2qe
	(Ei, pixelPositions, ntotpixels, tofUnit, mod2sample, toffset);
      
      // reduce
      typedef float_t Q_t;
      typedef float_t E_t;
      typedef float_t I_t;
      events2EvenlySpacedIxy
	<event_t, e2qe_t, 
	Q_t, E_t, I_t
	>
	(evts_begin, evts_end, 
	 e2qe,
	 Qbegin, Qend, dQ,
	 Ebegin, Eend, dE,
	 output_intensities_begin
	 );
    }
    
  }}


#endif // H_MCCOMPONENTS_EVENTS2IQE


// version
// $Id$

// End of file 
  
