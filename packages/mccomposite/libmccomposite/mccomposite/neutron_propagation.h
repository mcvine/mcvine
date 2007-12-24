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
  // It cannot be on the output surface of the shape
  void propagate_to_next_out_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape);


  // propagate a neutron to the next in-surface of a shape
  // please notice that a neutorn could go through a shape in/out
  // several times. For example, a neutron can go through a 
  // hollow cylinder by entering/exiting it twice (one at the
  // front surface, and another at the back surface.
  // note: shape cannot be infinitely large.
  // note: point must be out of shape, or it may be at the exiting
  //  surface.
  inline void propagate_to_next_in_surface
  ( mcni::Neutron::Event & ev, const geometry::AbstractShape & shape);

}



#endif
