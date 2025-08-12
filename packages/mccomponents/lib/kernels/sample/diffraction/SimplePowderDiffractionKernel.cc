// -*- C++ -*-
//
// Li Li
// Jiao Lin
//
// The implementation here is following that of PowderN component in mcstas.


#include <cmath>
#include <cassert>
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionData.h"
#include "mccomponents/kernels/sample/diffraction/SimplePowderDiffractionKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mcni/geometry/utils.h"
#include "mcni/neutron/units_conversion.h"
#include "mccomponents/math/random.h"


using namespace std;


struct mccomponents::kernels::SimplePowderDiffractionKernel::Details {

  // types
  typedef SimplePowderDiffractionKernel kernel_t;

  kernel_t *kernel;
  
  double absorption_cross_section;
  double incoherent_cross_section;
  double coherent_cross_section;
  
  double absorption_coeff;
  double scattering_coeff;
  double *q_v, *w_v, *my_s_v2;
  size_t Npeaks;
  double unitcell_volume;

  // ???
  double pack;
  double XsectionFactor;
  
  // meta methods
  Details(const SimplePowderDiffractionData &data, kernel_t *kernel);
  ~Details();

  // methods
  double scattering_xs(const mcni::Neutron::Event & ev );

};



mccomponents::kernels::SimplePowderDiffractionKernel::Details::Details
(const SimplePowderDiffractionData & data, kernel_t * i_kernel)
  :
  kernel(i_kernel),
  pack(1.),
  // XsectionFactor = 1, if cross-section in fm^2, or XsectionFactor = 100, if cross-section in barns
  XsectionFactor(100.)
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
	/ unitcell_volume
	/(v2k*v2k)
	*(peaks[i].multiplicity * peaks[i].F_squared / peaks[i].q)
	*XsectionFactor; 
      // unit is cross_section * v**2

      /* Squires [3.103] */
      q_v[i] = peaks[i].q*k2v;
      /*to be updated for size broadening*/
      w_v[i] = peaks[i].intrinsic_line_width;  

      // make sure the list is sorted
      if (i>0) assert(q_v[i-1] <= q_v[i]);
    }
  
  //coherent_cross_section = scattering_coefficient(const mcni::Neutron::Event& ev );
  
  /*coherent cross section is calculated under scattering_coefficient function, as it
    depends on the incident neutron velocity. */

  //total_scattering_cross_section = pack*( coherent_cross_section + data.incoherent_cross_section); // barn
  //total_scattering_coeff = total_scattering_cross_section/unitcell_volume * 100; // converted to 1/meter
  absorption_cross_section = pack * data.absorption_cross_section; // barn
  absorption_coeff = absorption_cross_section/unitcell_volume * 100; // converted to 1/meter
  
  incoherent_cross_section = data.incoherent_cross_section;
  coherent_cross_section = data.coherent_cross_section;
  
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


double
mccomponents::kernels::SimplePowderDiffractionKernel::Details::scattering_xs
(const mcni::Neutron::Event & ev)
{
  //add all the available scattering crossing together
  const mcni::Neutron::State &state = ev.state;
  V_t v(state.velocity);
  double v_l = v.length();
  double xs_v2 = 0.0;
  
  //printf("(Vx, Vy, Vz, V) = (%f, %f, %f, %f)\n", v.x, v.y, v.z, v_l);
  for (int i=0; i<this->Npeaks; i++)
    {
      if (v_l >= this->q_v[i]/2)
	//find out the one to be diffracted
	xs_v2 += this->my_s_v2[i];
    } 
  // std::cout << "xs_v2=" << xs_v2 << "v=" << v_l << std::endl;
  return xs_v2 / (v_l*v_l); //devided by v**2 at this step
}


mccomponents::kernels::SimplePowderDiffractionKernel::SimplePowderDiffractionKernel
( const SimplePowderDiffractionData & data, double d_phi)
  : m_details( new Details (data, this) ),
    m_d_phi(d_phi)
{}


double
mccomponents::kernels::SimplePowderDiffractionKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  const mcni::Neutron::State &state = ev.state;
  double v_l = state.velocity.length();
  double ret = m_details->absorption_coeff*2200/v_l;  //inversely proportional to velocity
  return ret;
}


double
mccomponents::kernels::SimplePowderDiffractionKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  double xs = m_details->scattering_xs(ev),
    v0 = m_details->unitcell_volume,
    ret = xs/v0;
  return ret;
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

    double v = state.velocity.length();
    /* Make coherent scattering event */
    const double * w_v = m_details->w_v;
    const double * q_v = m_details->q_v;
    const double * my_s_v2 = m_details->my_s_v2;

    // if incident energy is too low, no scattering
    if (v<q_v[0]/2) {ev.probability=-1; return;}
    
    // find the peak with the largest Q that is still scatterable
    size_t Npeaks = m_details->Npeaks;
    for (peakindex=1; peakindex<Npeaks; peakindex++) {
      if (v<q_v[peakindex]/2) break;
    }
    Npeaks = peakindex;
    
    if (Npeaks > 1)
      peakindex=math::random(size_t(0),Npeaks);  /* select a diffraction order */
    else
      peakindex = 0;

    if (w_v[peakindex])
      {
	arg = q_v[peakindex]*(1+w_v[peakindex]*math::random(-1.,1.))/(2.0*v); /* XXX: Implement "randnorm()",  normal*/
      }
    else
      arg = q_v[peakindex]/(2.0*v);

    // be very careful here
    double scatter_xs= my_s_v2[peakindex]/(v*v); // this is the cross section for this peak
    scatter_xs*=Npeaks; // from randomly choosing one peak
    
    theta = asin(arg);
    
    // Choose point on Debye-Scherrer cone
    if (m_d_phi)
      {   // relate height of detector to the height on DS cone
	arg = sin(m_d_phi*DEG2RAD/2)/sin(2*theta);
	/* If full Debye-Scherrer cone is within d_phi, don't focus */
	if (arg < -1 || arg > 1)
	  m_d_phi = 0;
	else    /* Otherwise, determine alpha to rotate from scattering plane into d_phi focusing area*/
	  alpha = 2*asin(arg);
      }
    
    if (m_d_phi)
      {
	/* Focusing */
	alpha = abs(alpha);
	/* Trick to get scattering for pos/neg theta's */
	alpha0= 2*math::random(0.,1.)*alpha;

	if (alpha0 > alpha)
	  {
	    alpha0=PI+(alpha0-1.5*alpha);
	  }
	else
	  {
	    alpha0=alpha0-0.5*alpha;
	  }
      }
    else
      {
	alpha0 = PI*math::random(-1.,1.);
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

    //V_t vtest(vout);
    //printf("(Vx, Vy, Vz) = (%f, %f, %f)\n", vtest.x, vtest.y, vtest.z);

    // change event
    ev.state.velocity = vout;

    if (isnan(vout[0]) || isnan(vout[1]) || isnan(vout[2]))
      {
	// XXX: Hack, in case the engine is not working rationally, for now let us ignore them
	ev.probability = -1;
	return;
      }
    ev.probability *= scatter_xs/m_details->unitcell_volume;
    /*
    std::cout 
      << peakindex << ": " 
      << q_v[peakindex] << ", " << v*2 << ", "
      << scatter_xs/m_details->unitcell_volume << std::endl;
    */
}


// version
// $Id$

// End of file 
