// -*- C++ -*-
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 
//                                  Jiao Lin
//                        California Institute of Technology
//                        (C) 1998-2004  All Rights Reserved
// 
//  <LicenseText>
// 
//  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// 



#include "mccomponents/kernels/sample/phonon/LinearlyInterpolatedDispersionOnGrid_3D.h"
#include "histogram/NdArray.h"


namespace test {

  using namespace DANSE::Histogram;
  using namespace DANSE::phonon;

  const unsigned int nQs = 11, nAtoms = 5, nDims = 3, nBranches = nAtoms*nDims;
  
    
  struct LinearlyInterpolatedDispersionOnGrid_3D_Example {
    
    typedef NdArray<double *, double, unsigned int, size_t, 7> array_7d_t;
    typedef NdArray<double *, double, unsigned int, size_t, 4> array_4d_t;
  
    typedef LinearlyInterpolatedDispersionOnGrid_3D< array_7d_t, array_4d_t > w_t;

    double eps_data[ nQs*nQs*nQs*nBranches*nAtoms*nDims*2 ];
    const static w_t::n_t eps_shape[7];

    double E_data[ nQs*nQs*nQs*nBranches ];
    const static w_t::n_t E_shape[4];

    array_7d_t eps_array;
    array_4d_t E_array;

    const w_t::axis_t QX, QY, QZ;

    w_t disp;

    LinearlyInterpolatedDispersionOnGrid_3D_Example()
      : eps_array( eps_data, eps_shape ),
	E_array( E_data, E_shape ),
	QX(-15, 3, nQs-1), QY(-15, 3, nQs-1), QZ(-15, 3, nQs-1),
	disp( nAtoms, QX,QY,QZ, eps_array, E_array )
    {
      
      w_t::n_t indexes[7];
      w_t::n_t & ix = indexes[0];
      w_t::n_t & iy = indexes[1];
      w_t::n_t & iz = indexes[2];
      w_t::n_t & ibranch = indexes[3];
      w_t::n_t & iatom = indexes[4];
      w_t::n_t & idir = indexes[5];
      w_t::n_t & iri = indexes[6];
      
      for (ix = 0; ix <= QX.n; ix ++ )
	for (iy = 0; iy <= QY.n; iy ++ )
	  for (iz = 0; iz <= QZ.n; iz ++ ) {
	    double x = QX.start + QX.step * ix;
	    double y = QY.start + QY.step * iy;
	    double z = QZ.start + QZ.step * iz;
	    
	    for (ibranch = 0; ibranch<nBranches; ibranch++) {
	      for (iatom = 0; iatom < nAtoms; iatom ++ )
		for (idir =0; idir<nDims; idir ++) 
		  for (iri = 0; iri<2; iri++) {
		    eps_array[ indexes ] = (iri?1/std::sqrt(3):0);
		  }
	      E_array[indexes] = std::abs( (x*x+y*y+z*z)/15/15/3 ) * 50;
	    }
	  }

    } 

  };// LinearlyInterpolatedDispersionOnGrid_3D_Example


  const unsigned int LinearlyInterpolatedDispersionOnGrid_3D_Example::eps_shape[7] = {nQs,nQs,nQs,nBranches,nAtoms,nDims,2};
  const unsigned int LinearlyInterpolatedDispersionOnGrid_3D_Example::E_shape[4] = {nQs,nQs,nQs,nBranches};

} //test::


// version
// $Id$

// End of file
