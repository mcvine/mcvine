#ifndef MCCOMPOSITE_NEUTRON_PROPAGATION_H
#define MCCOMPOSITE_NEUTRON_PROPAGATION_H

#include "mcni/neutron.h"
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
  
  inline tofs_t intersect( const mcni::Neutron::Event & ev, const AbstractShape & shape )
  {
    geometry::Arrow arrow( ev.state.position, ev.state.velocity );
    return geometry::intersect( arrow, shape );
  }
  
  inline tofs_t forward_intersect
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
  inline void propagate_to_next_out_surface
  ( mcni::Neutron::Event & ev, const AbstractShape & shape)
  {
    tofs_t tofs = forward_intersect( ev, shape );
    if (tofs.size()==0) return;
    // this needs a bit of thinking.
    // The number of forward intersections(t>0) would be
    // even if the starting point is outside of the shape.
    // It would be an odd number if the starting point is inside the shape.
    // If the starting point is outside of the shape, 
    // the next out surface should be the 2nd intersections, i.e., index=1.
    // If the starting point is inside the shape,
    // the next out surface would be the 1st intersection, i.e., index=0.
    double t = tofs[ (tofs.size()+1)%2 ];
    
    // if the neutron is inside the shape or outside the shape,
    // the above algorithm works. but if the neutron is on the front border,
    // we need to move that neutron beyond the border
//     bool found = 0;
//     if (locate(ev, shape) == geometry::Locator::onborder) {
//       // we need to find the first intersection that is not really 
//       // the same point as the start point
//       double previous = 0;
//       for (size_t i=0; i<tofs.size(); i++) {
// 	geometry::Position middlepoint = ev.state.position + tofs[i] * 0.5 * ev.state.velocity;
// 	if (locate(middlepoint, shape) == geometry::Locator::inside)
// 	  { t = tofs[i]; found = 1; break; }
//       }
//       if (! found ) throw "cannot find out surface?";
//     }

    propagate( ev, t );
  }


  // propagate a neutron to the next in-surface of a shape
  // please notice that a neutorn could go through a shape in/out
  // several times. For example, a neutron can go through a 
  // hollow cylinder by entering/exiting it twice (one at the
  // front surface, and another at the back surface.
  // note: shape cannot be infinitely large.
  inline void propagate_to_next_in_surface
  ( mcni::Neutron::Event & ev, const AbstractShape & shape)
  {
    tofs_t tofs = forward_intersect( ev, shape );
    if (tofs.size()==0) return;
    // this needs a bit of thinking.
    // The number of forward intersections(t>0) would be
    // even if the starting point is outside of the shape.
    // It would be an odd number if the starting point is inside the shape.
    // If the starting point is outside of the shape, 
    // the next in surface should be the 1st intersection, i.e., index=0.
    // If the starting point is inside the shape,
    // the next in surface would be the 2nd intersection, i.e., index=1.
    double t = tofs[ tofs.size()%2 ];

    propagate( ev, t );
  }


}


#endif
