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


#include "journal/debug.h"

#include "mccomponents/kernels/detector/He3Tube.h"


namespace He3Tube_impl {
  char * jrnltag = "He3Tube_kernel";
}

mccomponents::kernels::He3Tube::He3Tube
( double pressure, 
  const channels_t & tube_channels,
  const detector::Z2Channel & z2channel,
  const detector::Tof2Channel & tof2channel,
  detector::AbstractMultiChannelAnalyzer & mca
  )
  :
  He3(pressure),
  m_tube_channels( tube_channels ),
  m_z2channel( z2channel ),
  m_tof2channel( tof2channel ),
  m_mca( mca )
{
}

void
mccomponents::kernels::He3Tube::absorb
( mcni::Neutron::Event & ev )
{
#ifdef DEBUG
  journal::debug_t debug( He3Tube_impl::jrnltag );
  debug << journal::at(__HERE__)
	<< "event: " << ev
	<< journal::endl;
#endif
  
  channels_t channels = m_tube_channels;
  channels.push_back( m_z2channel( ev.state.position ) );
  channels.push_back( m_tof2channel( ev.time ) );
  m_mca.accept( channels, ev.probability );
}


// version
// $Id$

// End of file 
