// -*- c++ -*-

#include "DWFromDOS_Example.h"
#include "LinearlyInterpolatedDispersionOnGrid_3D_Example.h"
#include "mccomponents/math/rootfinding.h"
#include "mccomponents/kernels/sample/phonon/TargetCone.h"
#include "mccomponents/kernels/sample/phonon/CoherentInelastic_SingleXtal.h"


namespace test {

  using namespace mccomponents::kernels::phonon;
  using namespace mccomponents;
  

  struct CoherentInelastic_SingleXtal_Example{
    
    typedef CoherentInelastic_SingleXtal w_t;
    
    w_t::float_t Ei, max_omega, max_Q, temperature;
    w_t::float_t unitcell_vol;
    w_t::float_t deltaV_Jacobi;
    
    w_t::atoms_t create_atoms()
    {
      w_t::atoms_t atoms;
      w_t::float_t mass(10), coherent_scattering_length(sqrt(5)), 
	coherent_cross_section(5);
      w_t::atom_t atom;
      atom.mass = mass; atom.position = w_t::R_t(0,0,0);
      atom.coherent_cross_section = coherent_cross_section;
      atom.coherent_scattering_length = coherent_scattering_length;

      for (unsigned int i=0; i<5; i++)
	atoms.push_back( atom );
  
      return atoms;
    }

    CoherentInelastic_SingleXtal_Example() 
      :
      Ei( 70 ), max_omega( 60 ), max_Q (13), temperature( 300 ),
      unitcell_vol( 10 ),
      deltaV_Jacobi(0.001),
      dispersion_example(),
      atoms( create_atoms() ),
      DW_calculator_example(  ),
      root_finder(1.e-7),
      nSteps(10000),
      roots_finder(root_finder, nSteps),
      kernel
      ( dispersion_example.disp,
	atoms,
	unitcell_vol,
	DW_calculator_example.DW_calculator,
	temperature,
	deltaV_Jacobi,
	roots_finder,
	target_region
	)
    {}
    
    LinearlyInterpolatedDispersionOnGrid_3D_Example dispersion_example;
    w_t::atoms_t atoms;
    DWFromDOS_Example DW_calculator_example; 
    
    math::Algorithms::Bracketing::Ridder::ZRidd root_finder;
    size_t nSteps;
    math::FindRootsEvenly roots_finder;

    mccomponents::kernels::TargetCone target_region;
    
    CoherentInelastic_SingleXtal kernel;
  };

} // test::
