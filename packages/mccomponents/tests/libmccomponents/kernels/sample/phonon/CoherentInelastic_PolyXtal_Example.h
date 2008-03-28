// -*- c++ -*-

#include "DWFromDOS_Example.h"
#include "LinearlyInterpolatedDispersionOnGrid_3D_Example.h"
#include "mccomponents/kernels/sample/phonon/CoherentInelastic_PolyXtal.h"


namespace test {

  using namespace DANSE::phonon;
  using namespace mccomponents::kernels::phonon;
  

  struct CoherentInelastic_PolyXtal_Example{
    
    typedef CoherentInelastic_PolyXtal w_t;
    
    w_t::float_t Ei, max_omega, max_Q, temperature;
    w_t::float_t unitcell_vol;
    
    size_t nMCsteps_to_calc_RARV;
  
    w_t::atoms_t create_atoms()
    {
      w_t::atoms_t atoms;
      w_t::float_t mass(10), coherent_scattering_length(sqrt(5)), 
	coherent_cross_section(5);
      w_t::atom_t atom
	( w_t::R_t(0,0,0), mass, 
	  coherent_scattering_length, coherent_cross_section );

      for (unsigned int i=0; i<5; i++)
	atoms.push_back( atom );
  
      return atoms;
    }

    CoherentInelastic_PolyXtal_Example() 
      :
      Ei( 70 ), max_omega( 60 ), max_Q (13), temperature( 300 ),
      unitcell_vol( 10 ),
      nMCsteps_to_calc_RARV( 10000 ),
      dispersion_example(),
      atoms( create_atoms() ),
      DW_calculator_example(  ),
      kernel
      ( random_number_generator,
	dispersion_example.disp,
	atoms,
	unitcell_vol,
	DW_calculator_example.DW_calculator,
	temperature,
	Ei, 
	max_omega, max_Q,
	nMCsteps_to_calc_RARV 
	)
    {}
    
    LinearlyInterpolatedDispersionOnGrid_3D_Example dispersion_example;
    w_t::atoms_t atoms;
    DWFromDOS_Example DW_calculator_example;
    CoherentInelastic_PolyXtal kernel;
    mccomponents::random::Generator random_number_generator;
  };

} // test::
