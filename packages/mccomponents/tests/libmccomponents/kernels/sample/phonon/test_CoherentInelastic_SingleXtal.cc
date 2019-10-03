#include <cassert>

#include "journal/debug.h"

#include "CoherentInelastic_SingleXtal_Example.h"


using namespace DANSE::phonon;
using namespace mccomponents::kernels::phonon;

typedef CoherentInelastic_SingleXtal w_t;
typedef test::CoherentInelastic_SingleXtal_Example w_t_Example;



void testBasics(w_t & kernel)
{  
  std::cout << "-> test basics" << std::endl;

  // create a neutron 
  typedef w_t::neutron_t::state_t state_t;
  typedef state_t::position_t R_t;
  typedef state_t::velocity_t V_t;

  state_t state ( R_t(0,0,0), V_t(0,0,3000), state_t::spin_t() );
  w_t::neutron_t event( state, 0.0, 1.0 );

  std::cout << "* Created a neutron: " << event << std::endl;
  std::cout << "* Send the neutron to the scattering kernel" << std::endl;
  kernel.scatter( event );
  std::cout << "* The neutron is scattered to " << event << std::endl;

  std::cout << "->  basics test done." << std::endl << std::endl;
}


void runTests(w_t &kernel)
{
  testBasics(kernel);
}

int main()
{
  journal::debug_t debug("CoherentInelastic_SingleXtal");
  debug.activate();
  // journal::debug_t debug2("Omega_minus_deltaE");
  // debug2.activate();
  journal::debug_t debug3("Omega_minus_deltaE ctor");
  debug3.activate();
  // Create kernel
  w_t_Example example;
  w_t & kernel = example.kernel;
  // test kernel
  runTests(kernel);

  std::cout << "* test of scatering kernel CoherentInelastic_SingleXtal succeed." << std::endl;
}
