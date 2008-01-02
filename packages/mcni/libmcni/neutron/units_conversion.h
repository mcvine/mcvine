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

  namespace neutron_units_conversion{

      //! Temperature to Energy
      const double Kelvin2meV = (1/11.605);

      //! neutron wave vector k (AA^-1) to velocity (m/s)
      const double k2v = 629.719; 
      //! neutron velocity (m/s) to wave vector k (AA^-1)
      const double v2k = 1.58801E-3;

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
