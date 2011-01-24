//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                               Alex Dementsov
//                      California Institute of Technology
//                        (C) 2009  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// This code is a C++ implementation of Python scripts written by Li Li
//  See: http://dev.danse.us/trac/EngDiffSimulation/browser/SMARTSsimulation/trunk/SMARTS/Sample_Kernel/Polycrystal_EPSC_New

#include <cmath>
#include "mccomponents/kernels/sample/diffraction/EPSCDiffractionData.h"
#include "mccomponents/kernels/sample/diffraction/EPSCDiffractionKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mcni/geometry/utils.h"
#include "mcni/neutron/units_conversion.h"
#include "mccomponents/math/random.h"


#ifdef DEBUG
#include "journal/debug.h"
#endif

#ifdef DEBUG
// Example of debugging
m_details->debug  << "theta: " << theta << journal::endl;
#endif


struct mccomponents::kernels::EPSCDiffractionKernel::Details {
  double absorption_cross_section;
  double incoherent_cross_section;

  double absorption_coeff;
  double *q_v, *w_v, *my_s_v2;
  size_t Npeaks;
  double unitcell_volume;

  double pack;
  double XsectionFactor;

  // methods
  Details(const EPSCDiffractionData &data);
  ~Details();
};

mccomponents::kernels::EPSCDiffractionKernel::Details::Details
(const EPSCDiffractionData & data):
  pack(1.),
  XsectionFactor(1.)
{
  using mcni::PI;
  using namespace mcni::neutron_units_conversion;

  const std::vector<EPSCDiffractionData::Peak>& peaks = data.peaks;

  Npeaks  = peaks.size();
  q_v = new double[Npeaks];
  w_v = new double[Npeaks];
  my_s_v2 = new double[Npeaks];

  unitcell_volume = data.unitcell_volume;

  for(int i=0; i<Npeaks; i++)
    {
      my_s_v2[i] = 4*PI*PI*PI*pack
	*(peaks[i].DebyeWaller_factor ? peaks[i].DebyeWaller_factor : 1)
	/(unitcell_volume*unitcell_volume*v2k*v2k)
	*(peaks[i].multiplicity * peaks[i].F_squared / peaks[i].q)
	*XsectionFactor;      /* Is not yet divided by v^2 */

      /* Squires [3.103] */
      q_v[i] = peaks[i].q*k2v;
      /*to be updated for size broadening*/
      w_v[i] = peaks[i].intrinsic_line_width;
    }

  absorption_cross_section = pack * data.absorption_cross_section; // barn
  absorption_coeff = absorption_cross_section/unitcell_volume * 100; // converted to 1/meter

  incoherent_cross_section = data.incoherent_cross_section;

}


mccomponents::kernels::SimplePowderDiffractionKernel::Details::~Details()
{
  delete [] q_v;
  delete [] w_v;
  delete [] my_s_v2;
}


mccomponents::kernels::EPSCDiffractionKernel::EPSCDiffractionKernel
( const EPSCDiffractionData &data )
  : m_details( new Details(data) )
{}


double
mccomponents::kernels::EPSCDiffractionKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  const mcni::Neutron::State &state = ev.state;
  double v_l = state.velocity.length();
  return m_details->absorption_coeff*2200/v_l;  //inversely proportional to velocity
}


double
mccomponents::kernels::EPSCDiffractionKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
    const mcni::Neutron::State &state = ev.state;
    double v_l = state.velocity.length();
    double total_scattering_cross_v = 0.0;
    double total_scattering_coeff;

    for (int i=0; i<m_details->Npeaks; i++)
    {
      if (v_l >= m_details->q_v[i]/2)
        {
          //find out the one to be diffracted
          total_scattering_cross_v += m_details->my_s_v2[i];
        }
    }


    ////
        data = self.data
#        sample_pos = self.sample_pos
        grain_size = self.grain_size
        lattice_parameters = self.lattice_parameters
        hkl_len = self.hkl_len
        try_num = 5 # make neutron select hkl for 10 times
        Debye_v = 1
        f = 1
        size = grain_size
        hkl_infor = data.hklinfor(hkl_len)
        vlen = PN.vector_length(neu_vel)
        klen = PN.v_to_k(vlen)
        # randomly choose hkl information

        for j in range(0, try_num):
              i = randrange(0, hkl_len)
              h, k, l, Fq, jq = hkl_infor[i]
              hkl = h, k, l
              if PN.compare_value(hkl,
                                  lattice_parameters, klen)==1:
                    break
              elif j == try_num-1:
                    hkl = []
#                    raise NoDiffNeutron
        if len(hkl) != 0:
              cross_section = PN.crosssection(lattice_parameters,
                                              size, Debye_v,
                                              f, neu_vel,
                                              hkl, jq, Fq)
              v_abs = self.diff_v(neu_vel, hkl)
        else:
              cross_section = []
              v_abs = []
    ////

    total_scattering_cross_v /= (v_l*v_l); //devided by v**2 at this step
    total_scattering_cross_v += m_details->incoherent_cross_section;
    total_scattering_coeff = total_scattering_cross_v/m_details->unitcell_volume*100; // Factor 100 to convert from barns to fm^2

    return total_scattering_coeff;

}


void
mccomponents::kernels::EPSCDiffractionKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::EPSCDiffractionKernel::scatter
( mcni::Neutron::Event & ev )
{
#ifdef DEBUG
  m_details->debug << "in" << ev << journal::endl;
#endif

  // input neutron state
  mcni::Neutron::State & state = ev.state;
  // incident neutron velocity
  double vi = state.velocity.length();

  // theta, phi
  double theta = math::random(0, mcni::PI);
  double phi = math::random(0, mcni::PI*2);

  // scattered neutron velocity vector
  double vx = vi*sin(theta)*cos(phi);
  double vy = vi*sin(theta)*sin(phi);
  double vz = vi*cos(theta);

  // adjust probability of neutron event
  // normalization factor is 2pi*pi/4pi = pi/2
  ev.probability *= sin(theta) * (mcni::PI/2);

  typedef mcni::Vector3<double> V3d;
  V3d vf(vx,vy,vz);
  state.velocity = vf;

#ifdef DEBUG
  m_details->debug
    << "out" << ev
    << journal::endl;
#endif

}



