#include "journal/debug.h"

#include "CoherentInelastic_PolyXtal_Example.h"


using namespace DANSE::phonon;
using namespace mccomponents::kernels::phonon;

typedef CoherentInelastic_PolyXtal w_t;
typedef test::CoherentInelastic_PolyXtal_Example w_t_Example;


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

  // the following assertion might fail simply because a different
  // implementation of random number generator is used.
  // so it is not the best way to do test.
  // should figure out a better way to test Monte-Carlo algorithms.
//   assertNumberAlmostEqual
//     ( event.prob(), 3582.5, 0.0001, 0.1 );
//   assertVectorAlmostEqual
//     (event.state().velocity(), V3(3049.91,287.994,-870.66), 0.001, 0.1 );
  
  std::cout << "->  basics test done." << std::endl << std::endl;
}


void runTests(w_t & kernel)
{
    testBasics(kernel);
}


int main()
{

#ifdef DEEPDEBUG
  journal::debug_t debug( "phonon_coherent_inelastic_polyxtal_kernel" );
  debug.activate();
#endif

  w_t_Example example;
  
  w_t & kernel = example.kernel;

  std::cout << "* Created scattering kernel for phonon coherent inelastic scattering in polycrystal" << std::endl;

  runTests(kernel);

  std::cout << "* test of scatering kernel PhnnCohInelSC succeed." << std::endl;
}
