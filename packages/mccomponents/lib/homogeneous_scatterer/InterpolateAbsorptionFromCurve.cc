// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>


#include <cassert>
#include "mccomponents/math/search.h"
#include "mccomponents/homogeneous_scatterer/InterpolateAbsorptionFromCurve.h"

mccomponents::InterpolateAbsorptionFromCurve::InterpolateAbsorptionFromCurve
(const vec_t &energies, const vec_t &mus)
  : m_energies(energies),
    m_mus(mus)
{
  assert(energies.size() == mus.size());
  for (int i=0; i<energies.size()-1; i++) {
    assert(energies[i] < energies[i+1]);
  }
}
  
double mccomponents::InterpolateAbsorptionFromCurve::operator ()
  (const mcni::Neutron::Event &ev) const
{
  double E = ev.energy();
  typedef std::vector<double>::const_iterator it_t;
  typedef unsigned int uint;
  uint index = math::find_1st_bin_larger_than<double, it_t>(E, m_energies.begin(), m_energies.end());
  // boundaries
  if (index<=0) return m_mus[0];
  if (index>=m_energies.size()) return m_mus[m_energies.size()-1];
  // linear interpolation
  double E1 = m_energies[index-1], E2 = m_energies[index];
  double ratio = (E-E1)/(E2-E1);
  return ratio*m_mus[index] + (1-ratio)*m_mus[index-1];
}


// version
// $Id$

// End of file 
