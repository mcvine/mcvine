// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                         (C) 2005 All Rights Reserved  
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <iostream>
#include "mcni/neutron.h"
#include "mccomposite/CompositeNeutronScatterer.h"
#include "mccomposite/neutron_propagation.h"
#include "mccomposite/geometry/shapes.h"
#include "mcni/test/assert.h"



class Nothing: public mccomposite::AbstractNeutronScatterer{
public:
  Nothing(const mccomposite::geometry::AbstractShape & shape) 
    : AbstractNeutronScatterer( shape ) 
  {}
  InteractionType interact(mcni::Neutron::Event &) 
  {
    return none;
  }
};

void test1()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Nothing s(box);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s );

  CompositeNeutronScatterer cs( box, scatterers );

  mcni::Neutron::Event ev;
  assert (cs.interact( ev )==AbstractNeutronScatterer::none);
}

class Forwarding: public mccomposite::AbstractNeutronScatterer{
public:
  Forwarding(const mccomposite::geometry::AbstractShape & shape) 
    : AbstractNeutronScatterer( shape ) 
  {}
  InteractionType interact(mcni::Neutron::Event & ev) 
  {
    mccomposite::propagate_out( ev, shape() );
    return scattering;
  }
};

void test2()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Forwarding s(box);

  CompositeNeutronScatterer::scatterercontainer_t scatterers;

  scatterers.push_back( &s );

  CompositeNeutronScatterer cs( box, scatterers );

  mcni::Neutron::Event ev;
  ev.state.position = geometry::Position(0,0,-5);
  ev.state.velocity = geometry::Direction(0,0,1);
  ev.time = 0;
  ev.probability = 1.;

  mcni::Neutron::Event save = ev;

  assert (cs.interact( ev )==AbstractNeutronScatterer::scattering);
  assert (ev.state.position.z == 0.5);
  assert (ev.time == 5.5);
}


int main()
{
  test1();
}

// version
// $Id$

// End of file 
