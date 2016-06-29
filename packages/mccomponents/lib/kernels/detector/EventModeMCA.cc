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


#include <cassert>

#include "mccomponents/kernels/detector/EventModeMCA.h"
#include "mccomposite/vector2ostream.h"
#include "mccomponents/exception.h"
#include "journal/debug.h"


namespace mccomponents {
  namespace detector {

    namespace EventModeMCA_impl {
      
      const char * jrnltag = "EventModeMCA";

    }
    
  }
}


mccomponents::detector::EventModeMCA::EventModeMCA
(const char *outfilename, const indexes_t &dims)
  : m_out( outfilename, std::ofstream::binary ),
    m_dims( dims )
{
  // #ifdef DEBUG
  journal::debug_t debug( EventModeMCA_impl::jrnltag );
  debug << journal::at(__HERE__)
	<< "Opening event mode mca" << journal::newline
	<< "output file name: " << outfilename 
	<< journal::endl;

  // #endif
}

mccomponents::detector::EventModeMCA::~EventModeMCA()
{
  journal::debug_t debug( EventModeMCA_impl::jrnltag );
  debug << journal::at(__HERE__)
	<< "Closing event mode mca" 
	<< journal::endl;
  m_out.flush();
  m_out.close();
}

void mccomponents::detector::EventModeMCA::accept
( const channels_t & channels, double n )
{
  
#ifdef DEBUG
  journal::debug_t debug( EventModeMCA_impl::jrnltag );
  debug << journal::at(__HERE__)
	<< "channels: ";
  for (size_t i=0; i<channels.size(); i++) debug << channels[i] << ", ";
  debug << journal::newline;
  debug << "n = " << n 
	<< journal::endl;
#endif

  if  (channels.size()!=m_dims.size()+1) {
    std::ostringstream oss;
    oss << "Value error. Test of channels.size()==m_dims.size()+1 failed. ";
    oss << "channels = " << channels << ", "
	<< "dims = " << m_dims
	<< ".";
#ifdef DEBUG
    debug << journal::at(__HERE__) << oss.str() << journal::endl;
#endif
    throw Exception( oss.str().c_str() );
  }
  
  assert (m_dims.size() > 0);

  for (int i=0; i<channels.size(); i++) {
    if (channels[i] < 0 ) return;
    if (i < m_dims.size() && channels[i] >= m_dims[i]) {
      std::ostringstream oss;
      oss << "Value error. Channel " << i << " is out of bound: "
	  << "channel number = " << channels[i] << ", "
	  << "dimension = " << m_dims[i]
	  << ".";
#ifdef DEBUG
      debug << journal::at(__HERE__) << oss.str() << journal::endl;
#endif
      throw Exception( oss.str().c_str() );
    }
  }


  index_t &pixelID = m_buffer.pixelID;
  pixelID = 0;
  for (int i=0; i<m_dims.size(); i++) {
    pixelID = pixelID * m_dims[i] + channels[i];
  }


  m_buffer.tofChannelNo = channels[channels.size()-1];
  m_buffer.n = n;

#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "about to write  "
	<< "pixelID=" << m_buffer.pixelID << ", "
	<< "tofChannelNo=" << m_buffer.tofChannelNo << ", "
	<< "n=" << m_buffer.n << ", "
	<< journal::endl
    ;
#endif

  m_out.write( (const char *)&m_buffer, sizeof(m_buffer) );
}




// version
// $Id$

// End of file 
