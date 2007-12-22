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
#include "mccomposite/AbstractNeutronScatterer.h"
#include "mccomposite/geometry/AbstractShape.h"
#include "mccomposite/geometry/shapes.h"
#include "mcni/test/assert.h"



class Scatterer: public mccomposite::AbstractNeutronScatterer{
public:
  Scatterer(const mccomposite::geometry::AbstractShape & shape) 
    : AbstractNeutronScatterer( shape ) 
  {}
  InteractionType interact_path1(mcni::Neutron::Event &) 
  {
    return none;
  }
};

void test1()
{
  using namespace mccomposite;

  geometry::Box box(1,1,1);
  Scatterer s(box);
  mcni::Neutron::Event ev;
  s.scatter( ev );
}


int main()
{
  test1();
}

// version
// $Id$

// End of file 
