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


#include "mccomponents/kernels/detector/He3.h"
#include "mccomponents/exception.h"


mccomponents::kernels::He3::He3
( double pressure )
  : m_pressure( pressure), 
    m_refAbsXS( 5333.0e-28/1.798),
    m_refWavelength( 1.798),
    m_N( pressure*2.414e20)
{
}


double
mccomponents::kernels::He3::absorption_coefficient( const mcni::Neutron::Event & ev )
{
  double energy = ev.energy();
  return m_refAbsXS * sqrt(81.81/energy) * m_N;
}

double
mccomponents::kernels::He3::scattering_coefficient( const mcni::Neutron::Event & ev )
{
  return 0;
}

void
mccomponents::kernels::He3::scatter( mcni::Neutron::Event & ev )
{
  std::cerr << "WARNING: He3 detector doesn't scatter neutrons" << std::endl;
  return;
}

    

// version
// $Id$

// End of file 
