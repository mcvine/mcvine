#ifndef MCCOMPOSITE_NEUTRON_PROPAGATION_H
#define MCCOMPOSITE_NEUTRON_PROPAGATION_H

#include "mcni/neutron.h"
#include "mccomposite/geometry/intersect.h"


namespace mccomposite{
  
  typedef geometry::ArrowIntersector::distances_t distances_t;
  
  inline distances_t intersect( const mcni::Neutron::Event & ev, const AbstractShape & shape )
  {
    geometry::Arrow arrow( ev.state.position, ev.state.velocity );
    return geometry::intersect( arrow, shape );
  }
  
  inline distances_t forward_intersect
  ( const mcni::Neutron::Event & ev, const AbstractShape & shape )
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
  inline void propagate_out( mcni::Neutron::Event & ev, const AbstractShape & shape )
  {
    distances_t distances = intersect( ev, shape );
    if (distances.size()==0) return;
    double t = distances[ distances.size()-1 ];
    propagate( ev, t );
  }
  
  // propagate a neutron to the next out-surface of a shape
  // please notice that a neutorn could go through a shape in/out
  // several times. For example, a neutron can go through a 
  // hollow cylinder by entering/exiting it twice (one at the
  // front surface, and another at the back surface.
  inline void propagate_to_next_out_surface
  ( mcni::Neutron::Event & ev, const AbstractShape & shape)
  {
    distances_t distances = forward_intersect( ev, shape );
    if (distances.size()==0) return;
    // this needs a bit of thinking.
    // The number of forward intersections(t>0) would be
    // even if the starting point is outside of the shape.
    // It would be odd if the starting point is inside the shape.
    // If the starting point is outside of the shape, 
    // the next out surface should be the 2nd intersections, i.e., index=1.
    // If the starting point is inside the shape,
    // the next out surface would be the 1st intersection, i.e., index=0.
    double t = distances[ (distances.size()+1)%2 ];

    propagate( ev, t );
  }
}


#endif
