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

  // propagate a neutron out of a shape
  inline void propagate_out( mcni::Neutron::Event & ev, const AbstractShape & shape )
  {
    distances_t distances = intersect( ev, shape );
    if (distances.size()==0) return;
    double t = distances[ distances.size()-1 ];
    ev.state.position += ev.state.velocity * t;
    ev.time += t;
  }
}


#endif
