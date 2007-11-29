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


#include <iostream>
#include "mcni/geometry/Vector3.h"
#include "mcni/geometry/Position.h"
#include "mcni/geometry/Velocity.h"
#include "mcni/neutron/Event.h"

std::ostream & operator <<
( std::ostream &os, const mcni::Neutron::Event & e ) 
{
  e.print(os); return os;
}



// version
// $Id$

// Generated automatically by CxxMill on Tue Nov 27 20:21:35 2007

// End of file 
