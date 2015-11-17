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


#include "mcni/AbstractNeutronScatterer.h"

void
mcni::AbstractNeutronScatterer::absorb
(Neutron::Event &ev) 
{
  mcni::absorb( ev );
}

void
mcni::AbstractNeutronScatterer::scatterM
(const Neutron::Event &ev, Neutron::Events & evts) 
{
  // default implementation is single-scattering
  evts.resize(1);
  evts[0] = ev;
  scatter( evts[0] );
}



// version
// $Id$

// Generated automatically by CxxMill on Thu Apr  7 14:44:15 2005

// End of file 
