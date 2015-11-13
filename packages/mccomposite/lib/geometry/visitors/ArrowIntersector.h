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


#ifndef MCCOMPOSITE_GEOMETRY_ARROWINTERSECTOR_H
#define MCCOMPOSITE_GEOMETRY_ARROWINTERSECTOR_H

#include <vector>
#include "AbstractShapeVisitor.h"
#include "Arrow.h"

#include "shapes.h"


namespace mccomposite {
  
  namespace geometry {
    
    /// compute intersections between a shape and a given arrow
    /// It populates a list of numbers and return it, 
    /// each number corresponds to 
    /// one intersection. The number is the "distance" from the
    /// starting point of the arrow to an intersection point.
    /// The "distance" could be positive or negative, because
    /// the arrow has a direction.
    /// Please note the "distance" is measured by the unit of the
    /// the length of the "direction" vector. In other words,
    /// they are more like "time" if you consider "direction" vector
    /// as "velocity" vector.
    /// Note: 
    /// If the start point is inside of a shape, the implementations
    /// here must garauntee that the number of forward intersections 
    /// is even.
    /// If the start point is outside  a shape, the implementations
    /// here must garauntee that the number of forward intersections 
    /// is odd.
    struct ArrowIntersector: public AbstractShapeVisitor {
      
      // types
      typedef Arrow arrow_t;
      typedef double distance_t;
      typedef std::vector<distance_t> distances_t;
      
      
      //meta methods
      ArrowIntersector( const arrow_t & arrow );
      ArrowIntersector();
      virtual ~ArrowIntersector( );
      
      //methods
      void setArrow(const Position & start, 
		    const Direction & direction);
      void setArrow(const arrow_t & arrow);
      distances_t calculate_intersections(const AbstractShape & shape);
      
      //visiting methods
      // for primitives
      void visit( const Box * box );
      void visit( const Cylinder * cylinder );
      void visit( const Sphere * sphere );
      // for operations      // for operations
      void visit( const Difference * difference );
      void visit( const Dilation * dilation );
      void visit( const Intersection * intersection );
      void visit( const Reflection * reflection );
      void visit( const Rotation * rotation );
      void visit( const Translation * translation );
      void visit( const Union * adunion );

    private:
      void reset();
      
      // data
      arrow_t m_arrow;
      distances_t m_distances;

      // impl. details
      void visit_composition( const Composition * composition );
    };
    
  }
}


#endif

// version
// $Id$

// End of file 
