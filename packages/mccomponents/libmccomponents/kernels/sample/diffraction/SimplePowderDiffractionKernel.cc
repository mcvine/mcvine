// -*- C++ -*-
//
// Li Li
// Jiao Lin
//


#include <cmath>
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionData.h"
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mcni/geometry/utils.h"
#include "mcni/neutron/units_conversion.h"
#include "mccomponents/math/random.h"

#ifdef DEBUG
#include "journal/debug.h"
#endif

using namespace std;


struct mccomponents::kernels::SimplePowderDiffractionKernel::Details {

  // data
#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
#endif
  
  double absorption_cross_section;
  double incoherent_cross_section;
  
  double absorption_coeff;
  double *q_v, *w_v, *my_s_v2;
  size_t Npeaks;
  double unitcell_volume;

  // ???
  double pack;
  double XsectionFactor;
  
  // methods
  Details(const SimplePowderDiffractionData &data);
  ~Details();

};


#ifdef DEBUG
const char mccomponents::kernels::SimplePowderDiffractionKernel::Details::jrnltag[] = "SimplePowderDiffractionKernel";
#endif

mccomponents::kernels::SimplePowderDiffractionKernel::Details::Details
(const SimplePowderDiffractionData & data)
  :
#ifdef DEBUG
  debug( jrnltag ),
#endif
  pack(1.),
  XsectionFactor(1.)
{
  using mcni::PI;
  using namespace mcni::neutron_units_conversion;
  
  const std::vector<SimplePowderDiffractionData::Peak>& peaks = data.peaks;

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
	*XsectionFactor;
      /* Is not yet divided by v^2 */
      /* Squires [3.103] */
      q_v[i] = peaks[i].q*k2v;
      /*to be updated for size broadening*/
      w_v[i] = peaks[i].intrinsic_line_width;  
    }
  
  //coherent_cross_section = scattering_coefficient(const mcni::Neutron::Event& ev );
  
  /*coherent cross section is calculated under scattering_coefficient function, as it
    depends on the incident neutron velocity. */

  //total_scattering_cross_section = pack*( coherent_cross_section + data.incoherent_cross_section); // barn
  //total_scattering_coeff = total_scattering_cross_section/unitcell_volume * 100; // converted to 1/meter
  absorption_cross_section = pack * data.absorption_cross_section; // barn
  absorption_coeff = absorption_cross_section/unitcell_volume * 100; // converted to 1/meter
  
  incoherent_cross_section = data.incoherent_cross_section;
  /*
  // Is not yet divided by v 
  double my_a_v = pack*sigma_a/unitcell_volume*2200*100;   // Factor 100 to convert from barns to fm^2
  double my_inc = pack*sigma_i/unitcell_volume*100;   // Factor 100 to convert from barns to fm^2
  */
}


mccomponents::kernels::SimplePowderDiffractionKernel::Details::~Details()
{
  delete [] q_v;
  delete [] w_v;
  delete [] my_s_v2;
}


mccomponents::kernels::SimplePowderDiffractionKernel::SimplePowderDiffractionKernel
( const SimplePowderDiffractionData & data, double d_phi)
  : m_details( new Details (data) ),
    m_d_phi(d_phi)
{}


double
mccomponents::kernels::SimplePowderDiffractionKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  const mcni::Neutron::State &state = ev.state;
  double v_l = state.velocity.length();

  return m_details->absorption_coeff*2200/v_l;  //inversely proportional to velocity
}


double
mccomponents::kernels::SimplePowderDiffractionKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  //add all the available scattering crossing together
  
  const mcni::Neutron::State &state = ev.state;
  double v_l = state.velocity.length();
  double total_scattering_cross_v = 0.0;
  double total_scattering_coeff;
  
  cout << "magnitude of v: " << v_l << endl;
  
  for (int i=0; i<m_details->Npeaks; i++)
    {
      if (v_l >= m_details->q_v[i]/2)
	{
	  //find out the one which can be diffracted
	  total_scattering_cross_v += m_details->my_s_v2[i];
	  cout << "to velocity: " << m_details->q_v[i] << endl;
	}
    } 
  total_scattering_cross_v /= (v_l*v_l); //devided by v**2 at this step
  total_scattering_cross_v += m_details->incoherent_cross_section;
  total_scattering_coeff = total_scattering_cross_v/m_details->unitcell_volume*100; // Factor 100 to convert from barns to fm^2
  
  return total_scattering_coeff;
}


void
mccomponents::kernels::SimplePowderDiffractionKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::SimplePowderDiffractionKernel::scatter
( mcni::Neutron::Event & ev )
{
  using mcni::DEG2RAD;
  using mcni::PI;
  using std::sin;
  using std::asin;
  using std::abs;
  
  static V_t ex(1,0,0), ey(0,1,0), ez(0,0,1);
  
  const mcni::Neutron::State  &state  = ev.state;

  int peakindex;
  double arg;
  double alpha;
  double theta;
  double alpha0;
  int nx, ny, nz;
  double scatter_intensity;
  
  double v = state.velocity.length();
  /* Make coherent scattering event */
  const double * w_v = m_details->w_v;
  const double * q_v = m_details->q_v;
  const double * my_s_v2 = m_details->my_s_v2;
  
  const size_t & Npeaks = m_details->Npeaks;
  if (Npeaks > 0) {
    if (Npeaks > 1) 
      {
	peakindex=floor(math::random(0,Npeaks));  /* select a peak */
      }
    else peakindex = 0;
    if (w_v[peakindex])
      {
	arg = q_v[peakindex]*(1+w_v[peakindex]*math::random(-1,1))/(2.0*v); /*normal*/
#ifdef DEBUG
	m_details->debug << "arg: " << arg << journal::endl;
#endif
      }
    else
      arg = q_v[peakindex]/(2.0*v);
    scatter_intensity= my_s_v2[peakindex]/(v*v);
#ifdef DEBUG
    m_details->debug << "intensity: " << scatter_intensity << journal::endl;
#endif
    theta = asin(arg);
    
    // Choose point on Debye-Scherrer cone
    if (m_d_phi)
      { // relate height of detector to the height on DS cone 
	arg = sin(m_d_phi*DEG2RAD/2)/sin(2*theta);
	/* If full Debye-Scherrer cone is within d_phi, don't focus */
	if (arg < -1 || arg > 1) m_d_phi = 0;
	/* Otherwise, determine alpha to rotate from scattering plane
	   into d_phi focusing area*/
	else alpha = 2*asin(arg);
      }
    if (m_d_phi) {
      /* Focusing */
      alpha = abs(alpha);
      /* Trick to get scattering for pos/neg theta's */
      alpha0= 2*math::random(0,1)*alpha;
      if (alpha0 > alpha) {
	alpha0=PI+(alpha0-1.5*alpha);
      } else {
	alpha0=alpha0-0.5*alpha;
      }
    }
    else
      alpha0 = PI*math::random(-1,1);

    alpha = abs(alpha);

    /* Trick to get scattering for pos/neg theta's */
    alpha0= 2*math::random(0,1)*alpha;
    if (alpha0 > alpha) {
      alpha0=PI+(alpha0-1.5*alpha);
    } else {
      alpha0=alpha0-0.5*alpha;
    }
  }
  else
    {
      alpha0 = PI*math::random(-1,1);
#ifdef DEBUG
      m_details->debug << "angle: " << alpha0 << journal::endl;
#endif
    }
  /* now find a nearly vertical rotation axis:
   * Either
   *  (v along Z) x (X axis) -> nearly Y axis
   * Or
   *  (v along X) x (Z axis) -> nearly Y axis
   */
  if ( abs( (ex|state.velocity) ) < abs( (ez|state.velocity) ) )
    {
      nx = 1; ny = 0; nz = 0;
    } 
  else 
    {
      nx = 0; ny = 0; nz = 1;
    }
  V_t tmp_v = state.velocity * V_t(nx,ny,nz);
  
  // vout is incident v rotated by 2*theta around tmp_v
  V_t vout(state.velocity);
  rotate(vout, tmp_v, 2*theta);
  
  /* rotate vout by alpha0 around incident direction (Debye-Scherrer cone) */
  rotate(vout, state.velocity, alpha0);
  
  // change event
  ev.state.velocity = vout;
  ev.probability *= scatter_intensity;
}


// version
// $Id$

// End of file 
