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


#ifndef MCCOMPOSITE_GEOMETRY_LINEINTERSECTOR_H
#define MCCOMPOSITE_GEOMETRY_LINEINTERSECTOR_H

#include <vector>
#include "AbstractShapeVisitor.h"
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"

namespace mccomposite {

  template <typename Float>
  struct Arrow{

    // types
    typedef mcni::Position<Float> position_t;
    typedef mcni::Vector3<Float> direction_t;
    
    // meta methods
    Arrow( const position_t & start, const direction_t & direction );
    Arrow();

    // methods
    /// Just for ostream << operator
    void print( std::ostream & os ) const;

    // data
    position_t start;
    direction_t direction;
  };

  struct AbstractShape;

  /// compute intersections between a shape and a given line
  /// It populates a list of numbers and return it, 
  /// each number corresponds to 
  /// one intersection. The number is the "distance" from the
  /// starting point of the line to an intersection point.
  /// The "distance" could be positive or negative, because
  /// the line has a direction.
  /// Please note the "distance" is measured by the unit of the
  /// the length of the "direction" vector. In other words,
  /// they are more like "time" if you consider "direction" vector
  /// as "velocity" vector.
  struct LineIntersector: public AbstractShapeVisitor {
    
    // types
    typedef Arrow<double> arrow_t;
    typedef double distance_t;
    typedef std::vector<distance_t> distances_t;
    

    //meta methods
    LineIntersector( const arrow_t & arrow );
    LineIntersector();
    virtual ~LineIntersector( );

    //methods
    void setArrow(const arrow_t::position_t & start, 
		  const arrow_t::direction_t & direction);
    void setArrow(const arrow_t & arrow);
    distances_t calculate_intersections(const AbstractShape & shape);

    //  visitor methods
    virtual void onBox( const Box & box );

  private:
    void reset();

    // data
    arrow_t m_arrow;
    distances_t m_distances;
  };

}


template <typename Float>
std::ostream & operator << (std::ostream & os, const mccomposite::Arrow<Float> & arrow)
{
  arrow.print( os );
  return os;
}


#endif

// version
// $Id$

// End of file 
