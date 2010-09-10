// -*- C++ -*-
//
// Li Li
// Jiao Lin
//


#ifndef MCCOMPONENTS_KERNELS_SIMPLEPOWDERDIFFRACTIONPEAKDATA_H
#define MCCOMPONENTS_KERNELS_SIMPLEPOWDERDIFFRACTIONPEAKDATA_H


#include <vector>

namespace mccomponents {

  namespace kernels {

    // a simple structure describing a powder diffraction 
    struct SimplePowderDiffractionData {
      struct Peak{
	// Q length
	double q; 
	// squared structure factor
	double F_squared; 
	// multiplicity
	int multiplicity; 
	// intrinsic line width
	double intrinsic_line_width; 
	// Debye-Waller factor 
	double DebyeWaller_factor; 

	bool operator== (const Peak &rhs) {
	  return q == rhs.q				      \
	  && F_squared == rhs.F_squared			      \
	  && multiplicity == rhs.multiplicity		      \
	  && intrinsic_line_width == rhs.intrinsic_line_width \
	  && DebyeWaller_factor == rhs.DebyeWaller_factor     \
	  ;
	}
      };
      
      // peaks
      std::vector<Peak> peaks;
      // relative line width Delta_d/d
      double Dd_over_d;
      // Debye-Waller factor
      double DebyeWaller_factor;
      // density of material. [g/cm^3]
      double density;
      // atomic/molecular weight of material [g/mol]
      double atomic_weight; 
      // volume of unit cell [Angstrom^3]
      double unitcell_volume;
      // number of atoms per unit cell
      double number_of_atoms;   
      // absorption cross section per unit cell at 2200m/s [barns] 
      double absorption_cross_section;
      // incoherent cross section per unit cell [barns]
      double incoherent_cross_section;
      
    };
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_SIMPLEPOWDERDIFFRACTIONPEAKDATA_H

// version
// $Id$

// End of file 
