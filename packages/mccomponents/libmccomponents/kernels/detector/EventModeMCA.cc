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


#include "mccomponents/kernels/detector/EventModeMCA.h"


mccomponents::detector::EventModeMCA::EventModeMCA
(const char *outfilename, const index_t &npixels)
  : m_out( outfilename, std::ofstream::binary ),
    m_npixels( npixels )
{
}

mccomponents::detector::EventModeMCA::~EventModeMCA()
{
  
}

void mccomponents::detector::EventModeMCA::accept
( const channels_t & channels, double n )
{
  assert (channels.size()==3);
  if (channels[0] < 0 || channels[1]<0 || channels[2]<0) return;
  index_t pixelID = channels[0] * m_npixels + channels[1];
  m_out.write( (const char *)&pixelID, sizeof(index_t) );
  m_out.write( (const char *)(&channels[2]), sizeof(index_t) );
  m_out.write( (const char *)&n, sizeof(double) );
}



// version
// $Id$

// End of file 
