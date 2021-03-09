// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//
// The implementation here is borrowed from that of SingleCrystal component in mcstas.
// * Written by: Kristian Nielsen
// * Date: December 1999
// * Version: $Revision: 1.43 $

#include <cmath>
#include <cassert>
#include <iostream>
#include "mccomponents/kernels/sample/diffraction/SingleCrystalDiffractionData.h"
#include "mccomponents/kernels/sample/diffraction/SingleCrystalDiffractionKernel.h"
#include "mccomponents/exception.h"
#include "mcni/math/number.h"
#include "mcni/geometry/utils.h"
#include "mcni/neutron/units_conversion.h"
#include "mccomponents/math/random.h"
#include "mccomponents/math/random/gaussian.h"

// uncomment to debug tau_info_list creation
// #define DEBUG_SETUP_TAU_INFO_LIST

#ifdef DEBUG_SETUP_TAU_INFO_LIST
#define DEBUG
#endif

#ifdef DEBUG
#include "journal/debug.h"
#endif

#define FWHM2RMS 0.424660900144    /* Convert between full-width-half-max and */
#define RMS2FWHM 2.35482004503     /* root-mean-square (standard deviation) */


namespace {
  // copied from mcstas
  void normal_vec(double *nx, double *ny, double *nz,
                  double x, double y, double z)
  {
    using namespace std;
    double ax = abs(x);
    double ay = abs(y);
    double az = abs(z);
    double l;
    if(x == 0 && y == 0 && z == 0)
    {
      *nx = 0;
      *ny = 0;
      *nz = 0;
      return;
    }
    if(ax < ay)
    {
      if(ax < az)
      {                           /* Use X axis */
        l = sqrt(z*z + y*y);
        *nx = 0;
        *ny = z/l;
        *nz = -y/l;
        return;
      }
    }
    else
    {
      if(ay < az)
      {                           /* Use Y axis */
        l = sqrt(z*z + x*x);
        *nx = z/l;
        *ny = 0;
        *nz = -x/l;
        return;
      }
    }
    /* Use Z axis */
    l = sqrt(y*y + x*x);
    *nx = y/l;
    *ny = -x/l;
    *nz = 0;
  }
}

struct mccomponents::kernels::SingleCrystalDiffractionKernel::Details {

  // types
  typedef SingleCrystalDiffractionKernel kernel_t;
  typedef SingleCrystalDiffractionData::HKLData hkldata_t; // special hkl data type used by diffraction
  typedef std::vector<hkldata_t> hkllist_t;
  typedef SingleCrystalDiffractionData::TauData taudata_t;
  typedef std::vector<taudata_t> taulist_t;
  typedef mcni::Neutron::Event neutron_t;

  // data
#ifdef DEBUG
  const static char jrnltag[];
  journal::debug_t debug;
#endif

  kernel_t *kernel;
  //
  hkllist_t hkllist;
  taulist_t taulist;
  float_t total_refl; // units: 1
  float_t total_xs;   // units: barn
  size_t n_reflections;
  const neutron_t * neutron_ptr;
  neutron_t neutron;
  // meta methods
  Details(kernel_t *kernel);
  ~Details();
  // methods
  // xs: barn
  double scattering_xs(const mcni::Neutron::Event & ev );
  void setup_tau_info_list(const mcni::Neutron::Event &ev, bool verbose=false);
};


#ifdef DEBUG
const char mccomponents::kernels::SingleCrystalDiffractionKernel::Details::jrnltag[] = "SingleCrystalDiffractionKernel";
#endif

mccomponents::kernels::SingleCrystalDiffractionKernel::Details::Details
(kernel_t * i_kernel)
  :
#ifdef DEBUG
  debug( jrnltag ),
#endif
  kernel(i_kernel),
  hkllist(kernel->m_hkllist->size()),
  taulist(kernel->m_hkllist->size()),
  neutron_ptr(NULL)
{
  using namespace std;
  using namespace mcni::neutron_units_conversion;
  using mcni::PI;
  float_t delta_d_d = kernel->m_delta_d_d;
  const Lattice &lattice = *(kernel->m_lattice);
  float_t mosaic = kernel->m_mosaic;
  for (size_t i=0; i<kernel->m_hkllist->size(); i++) {
    hkldata_t &hklinfo = hkllist[i];
    hklinfo.hkl = (*(kernel->m_hkllist))[i];
    const mccomponents::kernels::HKL &hkl = hklinfo.hkl;
    hklinfo.tau = lattice.ra*hkl.h + lattice.rb*hkl.k + lattice.rc*hkl.l;
#ifdef DEEPDEBUG
    debug
      << journal::at(__HERE__)
      << "reciprocal lattice vectors:"
      << journal::newline << lattice.ra
      << journal::newline << lattice.rb
      << journal::newline << lattice.rc
      << journal::endl;
#endif
     hklinfo.tau_length = hklinfo.tau.length();
    // calc u1,u2,u3. local coordinate system
    // assume isotropic mosaic
    hklinfo.u1 = hklinfo.tau*(1./hklinfo.tau_length);
    hklinfo.sig.x = FWHM2RMS*delta_d_d*hklinfo.tau_length;
    normal_vec
      (&(hklinfo.u2.x), &(hklinfo.u2.y), &(hklinfo.u2.z),
       hklinfo.u1.x, hklinfo.u1.y, hklinfo.u1.z);
    hklinfo.u3 = hklinfo.u1*hklinfo.u2;
    // u^-1 is u.T. keep it with u for easier transformation back and forth
    hklinfo.uT1 = K_t(hklinfo.u1.x, hklinfo.u2.x, hklinfo.u3.x);
    hklinfo.uT2 = K_t(hklinfo.u1.y, hklinfo.u2.y, hklinfo.u3.y);
    hklinfo.uT3 = K_t(hklinfo.u1.z, hklinfo.u2.z, hklinfo.u3.z);
    hklinfo.sig.y = hklinfo.sig.z = FWHM2RMS * hklinfo.tau_length * mosaic;
    hklinfo.sig123 = hklinfo.sig.x * hklinfo.sig.y * hklinfo.sig.z;
    hklinfo.m1 = 1./(2*hklinfo.sig.x*hklinfo.sig.x);
    hklinfo.m2 = 1./(2*hklinfo.sig.y*hklinfo.sig.y);
    hklinfo.m3 = 1./(2*hklinfo.sig.z*hklinfo.sig.z);
    hklinfo.cutoff = 5*max(hklinfo.sig.x, max(hklinfo.sig.y, hklinfo.sig.z));
  }
}

mccomponents::kernels::SingleCrystalDiffractionKernel::Details::~Details()
{
}

void
mccomponents::kernels::SingleCrystalDiffractionKernel::Details::setup_tau_info_list
(const mcni::Neutron::Event &ev, bool verbose)
{
  // only when velocity changes we need recalculation
  if (neutron_ptr!=NULL && ev.state.velocity==neutron.state.velocity) return;
  using mcni::PI;
  using std::pow; using std::abs;
  using namespace mcni::neutron_units_conversion;
  V_t v(ev.state.velocity);
  K_t ki = v*v2k;
  float_t ki_length = ki.length();
  /* Max possible tau with 5*sigma delta-d/d cutoff. */
  float_t delta_d_d = kernel->m_delta_d_d;
  float_t tau_max = 2*ki_length/(1 - 5*delta_d_d);
  //
  const Lattice &lattice = *(kernel->m_lattice);
  total_xs = total_refl  = 0.;
  float_t xs_factor = pow(2*PI, 5.0/2.0)/(lattice.V0*ki_length*ki_length); // 1/AA???
  if (verbose) {
    std::cout
        << "v=" << v
        << ", ki=" << ki
        << ", xs_factor=" << xs_factor
        << ", V0=" << lattice.V0
        << ", ki_length=" << ki_length
        << std::endl;
  }
  //
  size_t itau = 0;
  for (size_t i=0; i<hkllist.size(); i++){
    /* Assuming reflections are sorted, stop search when max tau exceeded. */
    const hkldata_t hkldata = hkllist[i];
#ifdef DEBUG_SETUP_TAU_INFO_LIST
    debug << journal::at(__HERE__)
          << "hkl=" << hkldata.hkl.h << ", " << hkldata.hkl.k << ", " << hkldata.hkl.l
          << "tau=" << hkldata.tau << ", "
          << "tau_max=" << tau_max
          << journal::endl;
#endif
    if (hkldata.tau_length>tau_max) break;
    K_t rho = ki - hkldata.tau;
#ifdef DEBUG_SETUP_TAU_INFO_LIST
    debug << journal::at(__HERE__)
          << "ki=" << ki << ", rho=" << rho
          << journal::endl;
#endif
    float_t rho_length = rho.length();
    float_t diff = abs(rho_length-ki_length);
    // Check if scattering is possible (cutoff of Gaussian tails).
    if (diff > hkldata.cutoff) {
      if (verbose) {
        std::cout
          << "hkl=" << hkldata.hkl.h << ", " << hkldata.hkl.k << ", " << hkldata.hkl.l
          << "tau=" << hkldata.tau << ", "
          << "tau_max=" << tau_max
          << "diff, cutoff:" << diff << ", " << hkldata.cutoff
          << std::endl;
      }
      continue;
    }
#ifdef DEBUG_SETUP_TAU_INFO_LIST
    debug << journal::at(__HERE__)
          << "Found a reflection"
          << journal::endl;
#endif
    taudata_t & taudata = taulist[itau];
    /* Store reflection. */
    taudata.index = i;
    /* Get ki vector in local coordinates. */
    // careful with u or u^-1
    taudata.ki = hkldata.uT1*ki.x + hkldata.uT2*ki.y + hkldata.uT3*ki.z;
    taudata.rho = taudata.ki - K_t(hkldata.tau_length, 0., 0.);
    taudata.rho_length = rho_length;
    /* Compute the tangent plane of the Ewald sphere. */
    taudata.n = taudata.rho*(1./taudata.rho_length);
    taudata.o = taudata.n*(ki_length-rho_length);
    /* Compute unit vectors b1 and b2 that span the tangent plane. */
    K_t &b1=taudata.b1, &b2=taudata.b2, &n=taudata.n;
    normal_vec(&(b1.x), &(b1.y), &(b1.z), n.x, n.y, n.z);
    taudata.b2 = n*b1;
    /* Compute the 2D projection of the 3D Gauss of the reflection. */
    /* The symmetric 2x2 matrix N describing the 2D gauss. */
    float_t n11 = hkldata.m1*b1.x*b1.x + hkldata.m2*b1.y*b1.y + hkldata.m3*b1.z*b1.z,
      n12 = hkldata.m1*b1.x*b2.x + hkldata.m2*b1.y*b2.y + hkldata.m3*b1.z*b2.z,
      n22 = hkldata.m1*b2.x*b2.x + hkldata.m2*b2.y*b2.y + hkldata.m3*b2.z*b2.z;
    /* The (symmetric) inverse matrix of N. */
    float_t det_N = n11*n22 - n12*n12; // unit: AA^4
    float_t inv_n11 = n22/det_N, inv_n12 = -n12/det_N, inv_n22 = n11/det_N; // unit: AA^-2
    /* The Cholesky decomposition of 1/2*inv_n (lower triangular L). */
    taudata.l11 = sqrt(inv_n11/2); // unit: AA^-1
    taudata.l12 = inv_n12/(2*taudata.l11);
    taudata.l22 = sqrt(inv_n22/2 - taudata.l12*taudata.l12);
    float_t det_L = taudata.l11*taudata.l22; // unit: AA^-2
    taudata.det_L = det_L;
    /* The product B^T D o. */
    const K_t &o = taudata.o;
    float_t Bt_D_O_x = b1.x*hkldata.m1*o.x + b1.y*hkldata.m2*o.y + b1.z*hkldata.m3*o.z,
      Bt_D_O_y = b2.x*hkldata.m1*o.x + b2.y*hkldata.m2*o.y + b2.z*hkldata.m3*o.z;
    /* Center of 2D Gauss in plane coordinates. */
    float_t y0x = taudata.y0x = -(Bt_D_O_x*inv_n11 + Bt_D_O_y*inv_n12);
    float_t y0y = taudata.y0y = -(Bt_D_O_x*inv_n12 + Bt_D_O_y*inv_n22);
    /* Factor alpha for the distance of the 2D Gauss from the origin. */
    float_t alpha = hkldata.m1*o.x*o.x + hkldata.m2*o.y*o.y + hkldata.m3*o.z*o.z \
      - (y0x*y0x*n11 + y0y*y0y*n22 + 2*y0x*y0y*n12);
    taudata.refl = xs_factor*det_L*exp(-alpha)/hkldata.sig123;  /* intensity of that Bragg */
    total_refl += taudata.refl;                             /* total scatterable intensity */
    // 1e-2 is necessary when F2 is in unit of fm^2 to convert to barn
    // because in this class we assume cross sections are in barn.
    // See later scattering_xs method.
    // The original 1999 Single_crystal mcstas component has a bug about this,
    // which was fixed in a later version.
    // In the Single_crystal component shipped with mcstas 2.6.1,
    // there is a parameter "barns" to indicate whether the lau file
    // provides F2 in barns or fm^2
    taudata.xs = taudata.refl*hkldata.hkl.F2*1e-2;                  // convert to barn
    total_xs += taudata.xs;
    itau++;
    if (verbose) {
      // taudata.o = taudata.n*(ki_length-rho_length);
      std::cout 
          << "itau=" << itau
          << std::endl << "hkl=" << hkldata.hkl.h << ", " << hkldata.hkl.k << ", " << hkldata.hkl.l
          << std::endl << "m1=" << hkldata.m1 << ", m2=" << hkldata.m2
          << std::endl << "ki, rho, tau length" << ki_length << ", "
          << rho_length << ", " << hkldata.tau_length
          << std::endl << "ki vector=" << ki
          << std::endl << "rho=" << rho
          << std::endl << "Li tau=" << hkldata.tau << ", "
          << std::endl << "u1=" << hkldata.u1.x << ", " << hkldata.u1.y << ", " << hkldata.u1.z
          << std::endl << "u2=" << hkldata.u2.x << ", " << hkldata.u2.y << ", " << hkldata.u2.z
          << std::endl << "u3=" << hkldata.u3.x << ", " << hkldata.u3.y << ", " << hkldata.u3.z
          << std::endl << "Tj.ki=" << taudata.ki
          << std::endl << "Tj.rho=" << taudata.rho
          << std::endl << "n=" << taudata.n.x << ", " << taudata.n.y << ", " << taudata.n.z
          << std::endl << "o=" << o.x << ", " << o.y << ", " << o.z
          << std::endl << "n11=" << n11 << ", n12=" << n12 << ", n22=" << n22
          << std::endl << "y0x=" << y0x << ", y0y=" << y0y
          << std::endl << "det_L=" << det_L
          << std::endl << "alpha=" << alpha
          << std::endl << "sig123=" << hkldata.sig123
          << std::endl << "refl, xs=" << taudata.refl << ", " << taudata.xs
          << std::endl << "tau_max=" << tau_max
          << std::endl << "F2=" << hkldata.hkl.F2
          << std::endl;
    } //if verbose
  } //for
  n_reflections = itau;
  if (verbose) {
    std::cout 
      << "total_xs=" << total_xs
      << ", total_refl=" << total_refl
      << ", n_reflections=" << n_reflections
      << std::endl;
  }
  // save
  neutron_ptr = &ev;
  neutron = ev;
}

double
mccomponents::kernels::SingleCrystalDiffractionKernel::Details::scattering_xs
(const mcni::Neutron::Event & ev)
{
  setup_tau_info_list(ev);
  return total_xs;
}


mccomponents::kernels::SingleCrystalDiffractionKernel::SingleCrystalDiffractionKernel
(const lattice_t &lattice, const hkllist_t &hkllist,
 float_t mosaic, float_t delta_d_d,
 float_t abs_xs
 )
  : m_lattice(&lattice),
    m_hkllist(&hkllist),
    m_mosaic(mosaic),
    m_delta_d_d(delta_d_d),
    m_abs_xs(abs_xs),
    m_details( new Details (this) )
{
  // xs: barn. V0: \AA^3
  m_abs_coeff = m_abs_xs/m_lattice->V0*100;
}


double
mccomponents::kernels::SingleCrystalDiffractionKernel::absorption_coefficient(const mcni::Neutron::Event & ev )
{
  const mcni::Neutron::State &state = ev.state;
  float_t v_l = state.velocity.length();
  float_t ret = m_abs_coeff*2200./v_l;  //inversely proportional to velocity
  return ret;
}


double
mccomponents::kernels::SingleCrystalDiffractionKernel::scattering_coefficient(const mcni::Neutron::Event & ev )
{
  double xs = m_details->scattering_xs(ev),
    v0 = m_lattice->V0,
    ret = xs/v0*100;
  return ret;
}


void
mccomponents::kernels::SingleCrystalDiffractionKernel::absorb
( mcni::Neutron::Event & ev )
{
}


void
mccomponents::kernels::SingleCrystalDiffractionKernel::check_reflections
( const mcni::Neutron::Event & ev )
{
  m_details->setup_tau_info_list(ev, true);
}

void
mccomponents::kernels::SingleCrystalDiffractionKernel::scatter
( mcni::Neutron::Event & ev )
{
  using namespace mcni::neutron_units_conversion;
  m_details->setup_tau_info_list(ev);
  if(m_details->total_refl <= 0) {
    ev.probability = -1.;
    return;
  }
  float_t r = math::random(0., m_details->total_refl);
  // find the reflection
  float_t sum = 0;
  size_t j; // reflection index in taulist
  for(j = 0; j < m_details->n_reflections; j++) {
    sum += m_details->taulist[j].refl;
    if(sum > r) break;
  }
  if(j >= m_details->n_reflections) {
    std::cerr << "Single_crystal: Error: Illegal tau search "
              << "(r = " << r << ", sum = " << sum << ").\n";
    j = m_details->n_reflections - 1;
  }
  typedef SingleCrystalDiffractionData::TauData taudata_t;
  const taudata_t &taudata = m_details->taulist[j];
  size_t i = taudata.index;
  typedef SingleCrystalDiffractionData::HKLData hkldata_t; // special hkl data type used by diffraction
  const hkldata_t & hkldata = m_details->hkllist[i];
  /* Pick scattered wavevector kf from 2D Gauss distribution. */
  float_t z1 = math::normal_distrib_rand();
  float_t z2 = math::normal_distrib_rand();
  float_t y1 = taudata.l11*z1 + taudata.y0x;
  float_t y2 = taudata.l12*z1 + taudata.l22*z2 + taudata.y0y;
  float_t kfx = taudata.rho.x + taudata.o.x + taudata.b1.x*y1 + taudata.b2.x*y2;
  float_t kfy = taudata.rho.y + taudata.o.y + taudata.b1.y*y1 + taudata.b2.y*y2;
  float_t kfz = taudata.rho.z + taudata.o.z + taudata.b1.z*y1 + taudata.b2.z*y2;

  /* Normalize kf to length of ki, to account for planer
     approximation of the Ewald sphere. */
  float_t ki_length = ev.state.velocity.length()*v2k;
  float_t adjust = ki_length/sqrt(kfx*kfx + kfy*kfy + kfz*kfz);
  kfx *= adjust;
  kfy *= adjust;
  kfz *= adjust;
#ifdef DEBUG
  m_details->debug
    << journal::at(__HERE__)
    << "vi_length=" << ev.state.velocity.length()
    << ", ki_length=" << ki_length
    << ", prob=" << ev.probability
    << journal::endl;
#endif
  /* Adjust neutron weight */
  ev.probability *= taudata.xs*m_details->total_refl/(m_details->total_xs*taudata.refl);
  // see difference between "scatter" method and "S" method in kernels/KernelBase.h
  ev.probability *= scattering_coefficient(ev);
#ifdef DEBUG
  m_details->debug
    << journal::at(__HERE__)
    << "Reflection " << j << " was selected"
    << journal::newline << "hkl=" << hkldata.hkl.h << ", " << hkldata.hkl.k << ", " << hkldata.hkl.l
    << journal::newline << "u1=" << hkldata.u1.x << ", " << hkldata.u1.y << ", " << hkldata.u1.z
    << journal::newline << "u2=" << hkldata.u2.x << ", " << hkldata.u2.y << ", " << hkldata.u2.z
    << journal::newline << "u3=" << hkldata.u3.x << ", " << hkldata.u3.y << ", " << hkldata.u3.z
    << journal::newline << "rho=" << taudata.rho.x << ", " << taudata.rho.y << ", " << taudata.rho.z
    << journal::newline << "kf=" << kfx << ", " << kfy << ", " << kfz
    << journal::newline << "total_xs=" << m_details->total_xs
    << journal::newline << "total_refl=" << m_details->total_refl
    << journal::newline << "taudata.xs=" << taudata.xs
    << journal::newline << "taudata.refl=" << taudata.refl
    << journal::newline << "prob_factor=" << taudata.xs*m_details->total_refl/(m_details->total_xs*taudata.refl)
    << journal::newline << "prob=" << ev.probability
    << journal::endl;
#endif
  //
  float_t vx = k2v*(hkldata.u1.x*kfx + hkldata.u2.x*kfy + hkldata.u3.x*kfz);
  float_t vy = k2v*(hkldata.u1.y*kfx + hkldata.u2.y*kfy + hkldata.u3.y*kfz);
  float_t vz = k2v*(hkldata.u1.z*kfx + hkldata.u2.z*kfy + hkldata.u3.z*kfz);
  V_t &v = ev.state.velocity;
  v.x = vx; v.y = vy; v.z = vz;
}

// End of file
