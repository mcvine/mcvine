// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2006-2013  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


// kernel base class.
// compared to abstractscatteringkernel, it adds the method "S" 
// which is a representation of the scattering function S,
// and the scatter method basially delgates to S


#ifndef MCCOMPONENTS_KERNELS_KERNELBASE_H
#define MCCOMPONENTS_KERNELS_KERNELBASE_H


#include <iostream>
#include <typeinfo>
#include "mccomponents/homogeneous_scatterer/AbstractScatteringKernel.h"


namespace mccomponents {

  namespace kernels {


    class KernelBase : public AbstractScatteringKernel {
    public:
      
      // meta methods
      virtual ~KernelBase() {};
      
      // methods
      virtual double absorption_coefficient( const mcni::Neutron::Event & ev )=0;
      virtual double scattering_coefficient( const mcni::Neutron::Event & ev )=0;
      virtual void scatter( mcni::Neutron::Event & ev )
      {
	S(ev);
	// check velocity and make sure it is sane
	typedef mcni::Vector3<double> V3d;
	V3d& vel = ev.state.velocity;
	if (ev.probability >= 0 && (vel.x!=vel.x || vel.y!=vel.y || vel.z!= vel.z)) {
	  std::cerr << "In kernel " << typeid(*this).name()
		    << ", neutron velocity turns invalid: "
		    << ev
		    << std::endl;
	  // invalidate the neutron
	  ev.probability = -1;
	}
	
	if (ev.probability>0) {
	  double sigma = scattering_coefficient(ev);
	  ev.probability *= sigma;
	}
      }
      
      virtual void absorb( mcni::Neutron::Event & ev )=0;
      
      virtual void S( mcni::Neutron::Event & ev )=0;
    }; // class KernelBase
    
  } // kernels::
} // mccomponents::


#endif // MCCOMPONENTS_KERNELS_KERNELBASE_H

// version
// $Id$

// End of file 
