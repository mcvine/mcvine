// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>


#include "mccomponents/homogeneous_scatterer/InverseVelocityAbsorption.h"

mccomponents::InverseVelocityAbsorption::InverseVelocityAbsorption
(double mu_at_2200)
  : m_mu_at_2200(mu_at_2200)
{
}
  
double mccomponents::InverseVelocityAbsorption::operator ()
  (const mcni::Neutron::Event &ev) const
{
  double v = ev.state.velocity.length();
  return m_mu_at_2200 * (2200/v);
}


// version
// $Id$

// End of file 
