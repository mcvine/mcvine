// -*- c++ -*-

#include "DWFromDOS_Example.h"
#include "LinearlyInterpolatedDispersionOnGrid_3D_Example.h"
#include "mccomponents/kernels/sample/phonon/CoherentInelastic_PolyXtal.h"


namespace test {

  using namespace DANSE::phonon;
  using namespace mccomponents::kernels::phonon;
  

  struct CoherentInelastic_PolyXtal_Example{
    
    typedef CoherentInelastic_PolyXtal w_t;
    
    w_t::float_t max_omega, temperature;
    w_t::float_t a, b, c;
    
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

    CoherentInelastic_PolyXtal_Example() 
      :
      max_omega( 60 ), temperature( 300 ),
      a(2), b(2), c(2),
      dispersion_example(),
      atoms( create_atoms() ),
      DW_calculator_example(  ),
      kernel
      ( dispersion_example.disp,
	atoms,
	a, b, c,
	DW_calculator_example.DW_calculator,
	temperature,
	max_omega
	)
    {}
    
    LinearlyInterpolatedDispersionOnGrid_3D_Example dispersion_example;
    w_t::atoms_t atoms;
    DWFromDOS_Example DW_calculator_example;
    CoherentInelastic_PolyXtal kernel;
  };

} // test::
