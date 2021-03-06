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


#include "mcni/geometry/Vector3.h"
#include "mcni/neutron/Spin.h"

std::ostream & operator <<
( std::ostream &os, const mcni::Neutron::Spin & s ) 
{
  s.print(os); return os;
}



// version
// $Id$

// Generated automatically by CxxMill on Tue Nov 27 20:21:35 2007

// End of file 
