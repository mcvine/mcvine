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


#ifndef MCCOMPONENTS_KERNELS_Z2CHANNEL_H
#define MCCOMPONENTS_KERNELS_Z2CHANNEL_H


#include "mccomposite/geometry/Vector.h"


namespace mccomponents {

  namespace detector {

    /// convert z of neutron coordinates in a detector tube to a channel number
    class Z2Channel {

    public:

      // types
      /// 3-D vector type
      typedef mccomposite::geometry::Vector vector_t;


      // meta methods
      /// ctor
      /// parameters:
      /// detlength: tube length. unit: meter
      /// npixels: number of pixels
      /// axisDirection: direction vector of z (axis)
      /// channel0Coords: coordinates of the start point of the detector (negative end of channel 0)
      ///
      /// Eg: a tube of 1 meter long centered a (0,0,0). Its axis is along z direction.
      ///     then 
      ///       channel0Coords = (0,0,-0.5)
      ///       axisDirection = (0,0,1)
      inline Z2Channel( double detlength, size_t npixels, 
		 const vector_t & axisDirection,
		 const vector_t & channel0Coords);

      // methods
      inline int operator ()( const vector_t & neutron_coords ) const;

    
    private:
      // data
      double m_pixelheight, m_npixels;
      vector_t m_axisDirection, m_channel0Coords;
    };

  } // detector::

} // mccomponents::


#include "Z2Channel.icc"

#endif


// version
// $Id$

// End of file 
