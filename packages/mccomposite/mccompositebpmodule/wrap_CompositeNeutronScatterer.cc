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

#include "mccomposite/CompositeNeutronScatterer.h"

#include <boost/python.hpp>
#include "wrap_vector.h"


namespace wrap_mccomposite {

  void wrap_CompositeNeutronScatterer()
  {
    using namespace boost::python;
    using namespace mccomposite;


    wrap_vector2<AbstractNeutronScatterer *>( "NeutronScatterer_p" );

    class_<CompositeNeutronScatterer, bases<AbstractNeutronScatterer>, 
      boost::noncopyable>
      ("CompositeNeutronScatterer", 
       init< const AbstractShape &, 
       const CompositeNeutronScatterer::scatterercontainer_t &, 
       const CompositeNeutronScatterer::geometer_t &> () 
       [with_custodian_and_ward<1,2,
	with_custodian_and_ward<1,3,
	with_custodian_and_ward<1,4> > > () ]
       )
      ;

  }
}


// version
// $Id: wrap_vector.h 680 2007-11-21 16:22:12Z linjiao $

// End of file 
