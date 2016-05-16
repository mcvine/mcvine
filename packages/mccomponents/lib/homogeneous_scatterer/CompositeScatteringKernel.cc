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
#include <typeinfo>
#include "mccomposite/mccomposite.h"
#include "mccomponents/exception.h"
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
  int total_scattering_ind;
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



// helper functions
/// transform velocity from coordinate system of the host to the constituent
void tosubkernel 
(mccomposite::geometry::Direction & direction, 
 const mccomposite::geometry::RotationMatrix & rotmat)
{
  mccomposite::geometry::RotationMatrix rotmatT = rotmat;
  rotmatT.transpose();
  direction = rotmatT * direction;
}
void tohostkernel
(mccomposite::geometry::Direction & direction, 
 const mccomposite::geometry::RotationMatrix & rotmat)
{
  direction = rotmat * direction;
}



// meta-methods
mccomponents::CompositeScatteringKernel::CompositeScatteringKernel
( const kernels_t & kernels, const weights_t &weights, const rotmats_t &rotmats,
  bool average)
  : m_kernels(kernels),
    m_average(average),
    m_weights(weights),
    m_rotmats(rotmats),
    m_details(new Details(*this))
{
  assert(m_kernels.size() == m_weights.size());
  assert(m_rotmats.size() == m_weights.size());
  
  // find if one of the elemental kernel claims it does total scattering
  // make sure there is at most one such kernel. 
  // if there is one such kernel, record its index as 
  // m_details->total_scattering_ind
  int n_total_scatt = 0, total_scatt_ind = -1;
  for (int i=0; i<m_kernels.size(); i++) {
    if (m_kernels[i]->total_scattering()) {
      n_total_scatt ++; total_scatt_ind = i;
    }
    if (n_total_scatt > 1) {
      std::string m = "more than one kernel have total scattering. should rearrange kernel composite.";
      throw Exception(m);
    }
  }
  m_details->total_scattering_ind = total_scatt_ind;
  // std::cout << " * In CompositeScatteringKernel ctor, computed total_scattering_ind=" << total_scatt_ind << std::endl;
  
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
  for (size_t i=0; i<m_kernels.size(); i++)  {
    double tmp = m_kernels[i]->absorption_coefficient( ev );
    ret += tmp;
  }
  
  // always average the absorption coefficient??????????????
  ret/=m_kernels.size();
  
  return ret;
}

double
mccomponents::CompositeScatteringKernel::scattering_coefficient
( const mcni::Neutron::Event & ev ) 
{
  // if one of the element declares that it defines total_scattering
  // just use that one
  if (m_details->total_scattering_ind >= 0)
    return m_kernels[m_details->total_scattering_ind]->scattering_coefficient(ev);
  
  // otherwise, accumulate
  double ret = 0.;
  for (size_t i=0; i<m_kernels.size(); i++) {
    double c = m_kernels[i]->scattering_coefficient( ev );
    ret += c;
  }
  // if user requested average, do that
  if (m_average) ret/=m_kernels.size();
  return ret;
}

void mccomponents::CompositeScatteringKernel::scatter
( mcni::Neutron::Event & ev )
{
  size_t index = m_details->select_kernel();
  ev.probability /= m_weights[index];
  const rotmat_t &rotmat = m_rotmats[index];
  tosubkernel(ev.state.velocity, rotmat);
  m_kernels[index]->scatter( ev );
  tohostkernel(ev.state.velocity, rotmat);
}

void mccomponents::CompositeScatteringKernel::absorb
( mcni::Neutron::Event & ev )
{
  size_t index = m_details->select_kernel();
  ev.probability /= m_weights[index];
  const rotmat_t &rotmat = m_rotmats[index];
  tosubkernel(ev.state.velocity, rotmat);
  m_kernels[index]->absorb( ev );
  tohostkernel(ev.state.velocity, rotmat);
}

// version
// $Id$

// End of file 
