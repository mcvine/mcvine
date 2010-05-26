// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#ifndef MCNI_NEUTRON_UNITS_CONVERSION_H
#define MCNI_NEUTRON_UNITS_CONVERSION_H



namespace mcni{

  namespace physical_constants {
    const double neutron_mass = 1.6749286e-27;
    const double mN = neutron_mass;

    const double electron_charge = 1.60217733e-19;
    const double e = electron_charge;

    const double boltzman_constant = 1.3806504e-23;
    const double kB = boltzman_constant;

    const double hbar = 1.054571628e-34;
    
  } // physical_constants

  namespace neutron_units_conversion{

    using namespace physical_constants;
    
    //! Temperature to Energy
    const double Kelvin2meV = kB/(1e-3*e);
    // const double Kelvin2meV = 0.08617;

    //! neutron wave vector k (AA^-1) to velocity (m/s)
    const double k2v = hbar/mN * 1e10;
    // const double k2v = 629.719; 

    //! neutron velocity (m/s) to wave vector k (AA^-1)
    const double v2k = 1/k2v;
    // const double v2k = 1.58801E-3;

    //! sqrt of energy (meV) to velocity (m/s)
    using std::sqrt;
    const double sqrte2v = sqrt(2e-3*e/mN);
    //const double sqrte2v = 437.3949;

    //! square of velocity (m/s) to energy (meV)
    const double vsq2e = mN/(2e-3*e);
    //const double vsq2e = 5.227e-6;

    //! neutron energy (meV) to velocity (m/s)
    double E2v( double energy );
    //! neutron velocity to energy 
    double v2E( double velocity);
    //! square of neutron velocity to energy
    double vsquare2E( double vsquare);
    //! square of neutron k vector to energy
    double ksquare2E( double ksquare);
    //!  neutron k vector to energy
    double k2E( double k);
    //!  neutron energy to k
    double E2k( double E);

  } // neutron_units_conversion::

} // mcni::

#endif //MCNI_NEUTRON_UNITS_CONVERSION_H


// version
// $Id$

// End of file 
