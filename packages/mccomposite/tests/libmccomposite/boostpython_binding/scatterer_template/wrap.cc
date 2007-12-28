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

#include "mccomposite/mccomposite.h"


namespace mccomposite{

  class xxxCLASSxxx: public AbstractNeutronScatterer {
  public:

    // meta-methods
    xxxCLASSxxx( const geometry::AbstractShape &shape) : AbstractNeutronScatterer(shape) {}
    virtual ~xxxCLASSxxx() {}

    // methods
    virtual InteractionType interact_path1(mcni::Neutron::Event & ev) 
    {
      propagate_to_next_exiting_surface( ev, shape() );
      //... your code here ...
      return none/scattering/absorption;
    }
  };

} // mccomposite



#include "mccomposite/boostpython_binding/wrap_scatterer.h"

void wrap() 
{
  using namespace mccomposite::boostpython_binding;

  boostpython_binding::scatterer_wrapper<mccomposite::xxxCLASSxxx>::wrap
    ("xxxCLASSxxx", init<const mccomposite::geometry::AbstractShape &>() );
}



// version
// $Id$

// End of file 
