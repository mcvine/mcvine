// -*- C++ -*-
//
//


#include <limits>
#include "mccomponents/homogeneous_scatterer/DGSSXResPixel.h"
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"
#include "mccomposite/neutron_propagation.h"
#include "mccomponents/math/random.h"


// #define DEBUG
// #define DEBUG2  // for debugging distribution of random x (position along path)

#ifdef DEBUG
#include "portinfo"
#include "journal/debug.h"
#endif

#ifdef DEBUG2
#include "mcni/neutron/units_conversion.h"
#endif


namespace mccomponents {
  namespace DGSSXResPixel_Impl {
    char jrnltag [] = "DGSSXResPixel";
  }
}

#include "mccomponents/kernels/detector/He3.h"
class mccomponents::DGSSXResPixel::Kernel : public mccomponents::kernels::He3{
public:
  Kernel(double pressure)
    : He3(pressure) 
  {}
  void absorb( mcni::Neutron::Event & ev ) {};
};

mccomponents::DGSSXResPixel::~DGSSXResPixel
()
{
}

mccomponents::DGSSXResPixel::DGSSXResPixel
( double tof, double pressure, const AbstractShape & shape)
  // AbstractScatteringKernel & kernel)
  : base_t( shape ),
    m_tof(tof),
    m_kernel(new Kernel(pressure))
{
}


mccomponents::DGSSXResPixel::InteractionType
mccomponents::DGSSXResPixel::interact_path1(mcni::Neutron::Event &ev)
{
#ifdef DEBUG
  journal::debug_t debug(DGSSXResPixel_Impl::jrnltag);
#endif

  using namespace mccomposite;

  // first we need to find where we are
  Location location = locate( ev, shape() );

  // if the neutron is already in this shape, we are good
  // but if it is outside, we need to propagate to the front surface 
  // of the shape.
  if (location != geometry::Locator::inside ) {
    propagate_to_next_incident_surface(ev, shape());
  }

  // if tof is already > desired tof, it means the neutron is
  // too fast for the pixel to catch it
  double epsilon = std::numeric_limits<double>::epsilon();
  if (ev.time>m_tof) ev.probability = epsilon;
  else {
    // tof before exiting the shape
    // IMPORTANT: it is assumed that the pixel is not of hollow shape
    double tof = tof_before_exit( ev, shape() );
    // neutron too slow:
    if (ev.time+tof < m_tof) ev.probability = epsilon;
    else {

      // tof to detection
      double tof1 = m_tof - ev.time;
      
      // absorption
      double mu = m_kernel->absorption_coefficient( ev );
      // scattering
      double sigma = m_kernel->scattering_coefficient( ev );
      
      // distance of flight
      double v = ev.state.velocity.length();
      double x = tof1*v, distance = tof*v;
      
      // probability of detection
      double prob = mu * distance * std::exp( -(mu+sigma) * x );
      ev.probability *= prob;
    }
  }
  propagate_to_next_exiting_surface( ev, shape());
  return base_t::none;
}


mccomponents::DGSSXResPixel::InteractionType 
mccomponents::DGSSXResPixel::interactM_path1
(const mcni::Neutron::Event &ev, mcni::Neutron::Events &evts)
{
  const char *msg = "multiple scattering for DGSSXResPixel not implemented.";
  std::cerr << msg << std::endl;
  throw mccomposite::Exception(msg);
}


void
mccomponents::DGSSXResPixel::print(std::ostream &os) const {
  os << "mccomponents::DGSSXResPixel(tof=" << m_tof << ", shape=" << shape() << ")";
}

// End of file 
