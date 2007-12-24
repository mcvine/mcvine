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

#include "mccomposite/exception.h"
#include "mccomposite/neutron_propagation.h"


namespace mccomposite {

  void propagate_to_next_out_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape)
  {
    double t; // the result
    tofs_t tofs;

    // where is the point of start relative to the shape?
    geometry::Locator::Location location = locate(ev, shape);

    // if inside, the next intersection must be what we want
    if (location == geometry::Locator::inside) {

      tofs = forward_intersect( ev, shape );
      if (tofs.size() == 0) throw Exception("not intersections");
      t = tofs[0];

    } else {

      // if outside, let us propagate the event to the front
      // surface of the shape
      if (location == geometry::Locator::outside) {
	propagate_to_next_in_surface( ev, shape );
      }
      tofs = forward_intersect( ev, shape );

      // here, the event must be at the front surface of the shape.
      if (locate(ev, shape) != geometry::Locator::onborder) 
	throw Exception("event not at the front surface");

      // we need to find the first intersection that is not really 
      // the same point as the start point
      bool found = 0;
      for (size_t intersection_index=0; intersection_index<tofs.size(); 
	   intersection_index++) {
	geometry::Position middlepoint =\
	  ev.state.position + tofs[intersection_index] * 0.5 * ev.state.velocity;

	location = geometry::locate(middlepoint, shape);

	if (location == geometry::Locator::outside) 
	  throw Exception( "propagate_to_next_in_surface only works for points "
			   "outside the shape or points at the incident "
			   "surface of the shape" );
	if (location== geometry::Locator::inside)
	  { t = tofs[intersection_index]; found = 1; break; }
      }
      if (! found ) throw Exception("cannot find out surface?");
    }
    propagate( ev, t );
  }


  void propagate_to_next_in_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape)
  {
    double t;

    // if neutron is already inside the shape
    // throw exception
    geometry::Locator::Location location = locate(ev, shape);
    if (location==geometry::Locator::inside)
      throw Exception("neutron is already inside the shape");
    
    // get intersections
    tofs_t tofs = forward_intersect( ev, shape );
    if (tofs.size()==0) return;

    // if neutron is outside the shape, it is easy
    if (location == geometry::Locator::outside)
      t = tofs[0];
    else {
      // at border of existing surface. 
      // we need to find the first intersection that is not really 
      // the same point as the start point
      bool found = 0;
      for (size_t intersection_index=0; intersection_index<tofs.size(); intersection_index++) {
	geometry::Position middlepoint =\
	  ev.state.position + tofs[intersection_index] * 0.5 * ev.state.velocity;
	if (locate(middlepoint, shape) == geometry::Locator::outside)
	  { t = tofs[intersection_index]; found = 1; break; }
      }
      if (! found ) throw Exception( "cannot find in surface?" );
    }
    propagate( ev, t );
  }

}


// version
// $Id$

// End of file 
