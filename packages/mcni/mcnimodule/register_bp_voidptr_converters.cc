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

#include "mcni/neutron.h"
#include "bpext/bpext.h"


namespace mcnimodule{

  void register_bp_voidptr_converters()
  {

    using namespace bpext;
    using namespace mcni;

    // register extractors
    extractorRegistry["NeutronSpin"] = extract_ptr< Neutron::Spin >;
    extractorRegistry["cNeutronEvent"] = extract_ptr< Neutron::cEvent >;

    // register wrappers
    wrapperRegistry["NeutronSpin"] = wrap_ptr< Neutron::Spin >;
    wrapperRegistry["cNeutronEvent"] = wrap_ptr< Neutron::cEvent >;
  }

} // wrap:


// version
// $Id$

// End of file 
