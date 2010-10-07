// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2010 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>
#include "mccomponents/math/rootfinding.h"


namespace wrap_mccomponents {

  void wrap_rootsfinders()
  {
    using namespace boost::python;
    using namespace mccomponents::math;

    
    class_<RootFinder, boost::noncopyable>
      ("RootFinder", no_init)
      ;
    
    class_<Algorithms::Bracketing::Ridder::ZRidd, bases<RootFinder> >
      ("ZRidd",
       init<double>() )
      ;
    
    class_<RootsFinder, boost::noncopyable>
      ("RootsFinder", no_init)
      ;
    
    class_<FindRootsEvenly, bases<RootsFinder> >
      ("FindRootsEvenly",
       init<const RootFinder &, size_t> ()
       [with_custodian_and_ward<1,2>()]
       )
      ;
  }

}

// version
// $Id$

// End of file 
