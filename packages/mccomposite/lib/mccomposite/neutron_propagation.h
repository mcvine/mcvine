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


#ifndef MCCOMPOSITE_NEUTRON_PROPAGATION_H
#define MCCOMPOSITE_NEUTRON_PROPAGATION_H

#include "mcni/neutron.h"
#include "mccomposite/geometry/AbstractShape.h"
#include "mccomposite/geometry/intersect.h"
#include "mccomposite/geometry/locate.h"


namespace mccomposite{
  
  typedef geometry::Locator::Location Location;

  inline Location locate
  ( const mcni::Neutron::Event  & ev, 
    const geometry::AbstractShape & shape )
  {
    //return geometry::locate(ev.state.position, shape );
    return geometry::locate(ev.state.position, shape );
  }



  typedef geometry::ArrowIntersector::distances_t tofs_t;
  
  inline tofs_t intersect
  ( const mcni::Neutron::Event & ev, const geometry::AbstractShape & shape )
  {
    geometry::Arrow arrow( ev.state.position, ev.state.velocity );
    return geometry::intersect( arrow, shape );
  }
  
  inline tofs_t forward_intersect
  ( const mcni::Neutron::Event & ev, const geometry::AbstractShape & shape )
  {
    geometry::Arrow arrow( ev.state.position, ev.state.velocity );
    return geometry::forward_intersect( arrow, shape );
  }

  // propagate a neutron for a given time
  inline void propagate( mcni::Neutron::Event & ev, double t)
  {
    ev.state.position += ev.state.velocity * t;
    ev.time += t;
  }
  
  // propagate a neutron out of a shape
  inline void propagate_out
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape )
  {
    tofs_t tofs = intersect( ev, shape );
    if (tofs.size()==0) return;
    double t = tofs[ tofs.size()-1 ];
    propagate( ev, t );
  }
  
  // propagate a neutron to the next out-surface of a shape
  // please notice that a neutorn could go through a shape in/out
  // several times. For example, a neutron can go through a 
  // hollow cylinder by entering/exiting it twice (one at the
  // front surface, and another at the back surface.
  // note: shape cannot be infinitely large.
  // note: the starting point must be either
  //   1. inside the shape
  //   2. outside the shape
  //   3. on the input surface of the shape
  // If the starting point is already on the exiting surface of the shape,
  // nothing will be done.
  void propagate_to_next_exiting_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape);


  // propagate a neutron to the next incident-surface of a shape
  // please notice that a neutorn could go through a shape in/out
  // several times. For example, a neutron can go through a 
  // hollow cylinder by entering/exiting it twice (one at the
  // front surface, and another at the back surface.
  // note: shape cannot be infinitely large.
  // note: point must be out of shape, or it may be at an exiting
  //  surface.
  // note: if the starting point is already on a
  //  incident surface, nothing will be done.
  void propagate_to_next_incident_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape);

  // calcualte the total tof of neutron for it to exit
  // the given shape for the first time.
  // please notice that a neutorn could go through a shape in/out
  // several times. For example, a neutron can go through a 
  // hollow cylinder by entering/exiting it twice (one at the
  // front surface, and another at the back surface.
  // note: shape cannot be infinitely large.
  // note: point must be inside the shape, or it may be at an incident
  // surface.
  double tof_before_exit
  ( const mcni::Neutron::Event & ev, const geometry::AbstractShape & shape);


  /// test if a neutron is exiting a shape and never hits it again.
  /// note: sometimes a neutron could be exiting from a shape, but
  /// will hit the shape again, for example, when a neutron inside 
  /// a hllow box.
  bool is_exiting
  ( const mcni::Neutron::Event & ev, const geometry::AbstractShape & shape);

  /// test if a neutron is moving (has velocity)
  bool is_moving (const mcni::Neutron::Event &ev);
}



#endif


// version
// $Id$

// End of file 
