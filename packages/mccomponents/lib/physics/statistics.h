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

#ifndef MCCOMPONENTS_PHYSICS_STATISTICS_H
#define MCCOMPONENTS_PHYSICS_STATISTICS_H


namespace mccomponents {

  namespace physics {
    
    //! Bose Einstein Distribution
    /*!
      \param energy energy in (meV)
      \param temperature temperature in (Kelvin)
    */
    double BoseEinsteinDistribution(double energy, double temperature); 

  }

}


#endif


// version
// $Id$

// End of file 
