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

#include <cassert>
#include "mccomposite/mccomposite.h"
#include "mccomponents/math/random.h"
#include "mccomponents/homogeneous_scatterer/CompositeScatteringKernel.h"


struct mccomponents::CompositeScatteringKernel::Details{
  // types
  typedef CompositeScatteringKernel w_t;
  
  // meta methods
  Details( w_t & kernel );

  // methods
  int select_kernel() const;

  // data
  w_t & kernel;
};


mccomponents::CompositeScatteringKernel::
Details::Details( w_t & i_kernel )
  : kernel(i_kernel)
{
}

int mccomponents::CompositeScatteringKernel::
Details::select_kernel() const
{
  int N = kernel.m_kernels.size();
  if (N==1) return 0;
  
  double x = math::random01(), t=0;
  // std::cout << "x=" << x << std::endl;
  for (int i=0; i<N; i++) {
    t+=kernel.m_weights[i];
    // std::cout << "t=" << t << std::endl;
    if (x<t) return i;
  }
  // std::cout << std::endl;
  return N-1;
}



// meta-methods
mccomponents::CompositeScatteringKernel::CompositeScatteringKernel
( const kernels_t & kernels, const weights_t &weights, bool average)
  : m_kernels(kernels),
    m_average(average),
    m_weights(weights),
    m_details(new Details(*this))
{
  assert(m_kernels.size() == m_weights.size());
  // normalize weights
  double tw = 0;
  for (int i=0; i<m_weights.size(); i++)
    tw += m_weights[i];
  for (int i=0; i<m_weights.size(); i++)
    m_weights[i]/=tw;
}

mccomponents::CompositeScatteringKernel::~CompositeScatteringKernel
()
{
}

// methods
double 
mccomponents::CompositeScatteringKernel::absorption_coefficient
( const mcni::Neutron::Event & ev )
{
  double ret = 0.;
  for (size_t i=0; i<m_kernels.size(); i++) 
    ret += m_kernels[i]->absorption_coefficient( ev );
  
  // always average the absorption coefficient??????????????
  ret/=m_kernels.size();
  
  return ret;
}

double
mccomponents::CompositeScatteringKernel::scattering_coefficient
( const mcni::Neutron::Event & ev ) 
{
  double ret = 0.;
  for (size_t i=0; i<m_kernels.size(); i++) 
    ret += m_kernels[i]->scattering_coefficient( ev );
  if (m_average) ret/=m_kernels.size();
  return ret;
}

void mccomponents::CompositeScatteringKernel::scatter
( mcni::Neutron::Event & ev )
{
  size_t index = m_details->select_kernel();
  ev.probability /= m_weights[index];
  m_kernels[index]->scatter( ev );
}

void mccomponents::CompositeScatteringKernel::absorb
( mcni::Neutron::Event & ev )
{
  size_t index = m_details->select_kernel();
  ev.probability /= m_weights[index];
  m_kernels[index]->absorb( ev );
}


// version
// $Id$

// End of file 
