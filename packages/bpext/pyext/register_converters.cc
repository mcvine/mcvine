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

#include <vector>
#include "bpext/bpext.h"


namespace wrap{

  void register_converters()
  {

    using namespace bpext;

    using std::vector;

    // register extractors
    extractorRegistry["vec_double"] = extract_ptr< vector<double> >;
    extractorRegistry["double"] = extract_ptr< double >;
    extractorRegistry["WrappedPointer"] = extract_ptr< WrappedPointer >;

    // register wrappers
    wrapperRegistry["vec_double"] = wrap_ptr< vector<double> >;
    // have not found ways to wrap non-class types, the following does not work:
    //wrapperRegistry["double"] = wrap_ptr< double >;
  }

} // wrap:


// version
// $Id$

// End of file 
