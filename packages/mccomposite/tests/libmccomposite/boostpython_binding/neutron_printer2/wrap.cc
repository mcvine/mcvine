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

  class NeutronPrinter: public AbstractNeutronScatterer {
  public:

    // meta-methods
    NeutronPrinter( const geometry::AbstractShape &shape) : AbstractNeutronScatterer(shape) {}
    virtual ~NeutronPrinter() {}

    // methods
    virtual InteractionType interact_path1(mcni::Neutron::Event & ev) 
    {
      propagate_to_next_exiting_surface( ev, shape() );
      std::cout << ev << std::endl;
      return none;
    }
  };

} // mccomposite



#include "mccomposite/boostpython_binding/wrap_scatterer.h"

void wrap() 
{
  using namespace mccomposite::boostpython_binding;

  boostpython_binding::scatterer_wrapper<mccomposite::NeutronPrinter>::wrap
    ("NeutronPrinter", 
     init<const mccomposite::geometry::AbstractShape &>() 
     [with_custodian_and_ward<1,2>()]
     );
}



// version
// $Id$

// End of file 
