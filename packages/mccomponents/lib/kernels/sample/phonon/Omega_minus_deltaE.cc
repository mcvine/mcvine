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

#include <iostream>
#include <cmath>
//#include <portinfo>
#include "journal/debug.h"
#include "mcni/neutron/units_conversion.h"
#include "mccomponents/kernels/sample/phonon/vector3.h"
#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"
#include "mccomponents/kernels/sample/phonon/Omega_minus_deltaE.h"


namespace mccomponents{ namespace kernels { namespace phonon{


static char Omega_minus_deltaE_debug_channel[] = "Omega_minus_deltaE";

Omega_q_minus_deltaE::Omega_q_minus_deltaE
(int branch,
 const V_t &vf_dir, const V_t &vi,
 float_t abs_vi, const dispersion_t &disp)
  :_branch(branch),
   _vf_direction(vf_dir), _vi(vi),
   _abs_vi(abs_vi), _disp(&disp) 
{
#ifdef DEBUG
  journal::debug_t debug("Omega_minus_deltaE ctor");
#endif

#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "vf direction=" << vf_dir 
	<< journal::endl;
#endif
}


//! w(q)-abs(Ei-Ef)
Omega_q_minus_deltaE::float_t mccomponents::kernels::phonon::Omega_q_minus_deltaE::evaluate( float_t vf ) const
{
#ifdef DEBUG
  journal::debug_t debug(Omega_minus_deltaE_debug_channel);
#endif

  const float_t &vv_x = _vf_direction.x, 
    &vv_y = _vf_direction.y, &vv_z = _vf_direction.z;

  const float_t &vi_x = _vi.x, &vi_y = _vi.y, &vi_z = _vi.z;

#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "vi=" << vi_x << ", " << vi_y << ", " << vi_z
	<< journal::newline
	<< "vf_direction" << _vf_direction
	<< journal::newline
	<< "vf length" << vf
	<< journal::endl;
#endif

  float_t qx, qy, qz, res_phonon, res_neutron;  
  
  using mcni::neutron_units_conversion::v2k;

  qx=v2k*(vi_x-vf*vv_x);
  qy=v2k*(vi_y-vf*vv_y);
  qz=v2k*(vi_z-vf*vv_z);
  
#ifdef DEBUG
  debug << journal::at(__HERE__)
	<< "q=" << qx << ", " << qy << ", " << qz 
	<< journal::endl;
#endif

  res_phonon = _disp->energy(_branch, K_t(qx, qy, qz));
  //cout << "vf" << vf << endl;
  //cout << "qx,qy,qz" << qx <<"," << qy <<"," << qz << endl;
  //cout << "res_phonon = " << res_phonon << endl;

  using mcni::neutron_units_conversion::vsquare2E;
  using std::abs;
  res_neutron = vsquare2E(abs(_abs_vi*_abs_vi-vf*vf));
  
  return (res_phonon - res_neutron);  
}

template <typename T>
std::ostream & operator << (std::ostream &os, const std::vector<T> &v)
{
  for (size_t i = 0; i<v.size(); i++) {
    os << v[i] << ", " ;
  }
  return os;
}

void mccomponents::kernels::phonon::Omega_q_minus_deltaE::print(std::ostream & os, float_t x0, float_t x1, float_t dx) const
{
  std::vector<float_t> xarr, yarr;
  for (float_t x =x0; x<x1; x+=dx) {
    xarr.push_back(x);
    yarr.push_back(evaluate(x));
  }
  os << "omega(q)-deltaE(" 
     << "branch=" << _branch << ", "
  // os << "vf direction=" << _vf_direction << ", ";
  // os << _vf_direction;
  // os << "vi=" << _vi << ", "
     << "abs vi=" << _abs_vi << ", "
     << ")"
     << "[x=" << xarr << ","
     << "y=" << yarr << "]"
    ;
}


}}} // mccomponents::kernels::phonon

// version
// $Id$

// End of file 
