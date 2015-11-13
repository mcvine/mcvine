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


#ifndef MCCOMPOSITE_GEOMETER_H
#define MCCOMPOSITE_GEOMETER_H


#include <map>
#include <utility>
#include "geometry/Position.h"
#include "geometry/RotationMatrix.h"


namespace mccomposite{

  /// Geometer.
  /// Geometer is responsible to keep geometric information of subeleements
  /// of a container relative to the containter.
  template <typename element_t>
  class Geometer {

  public:

    //types:
    typedef geometry::Position position_t;
    typedef geometry::RotationMatrix orientation_t;
    
    //meta-methods 
    Geometer();
    
    //methods
    /// remember element's position and orientation
    void remember
    ( const element_t & , const position_t & , const orientation_t &);
    
    const position_t & getPosition( const element_t & )  ;
    const orientation_t & getOrientation( const element_t & ) ;

  private:
    typedef std::pair< position_t, orientation_t > info_t;
    typedef std::map< const element_t *, info_t > e2info_t;
    //data
    e2info_t m_e2info;
  };
}


#include "Geometer.icc"


#endif

// version
// $Id$

// End of file 
