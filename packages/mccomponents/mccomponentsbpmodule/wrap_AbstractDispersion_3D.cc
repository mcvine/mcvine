// -*- C++ -*-
//
// Jiao Lin <jiao.lin@gmail.com>
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/phonon/AbstractDispersion_3D.h"
#include "histogram/NdArray.h"

namespace wrap_mccomponents {

  // helper functions
  typedef DANSE::Histogram::NdArray<double *, double, unsigned int, size_t, 2> array_2d_t;
  typedef DANSE::Histogram::NdArray<double *, double, unsigned int, size_t, 3> array_3d_t;
  // Qarr: NQX3 array
  // Earr: NQXnbranches array
  void disp_energies(DANSE::phonon::AbstractDispersion_3D &disp, const array_2d_t &Qarr, array_2d_t &Earr)
  {
    typedef mcni::Vector3<double> V3;
    size_t nbr = disp.nBranches();
    size_t nQ = Qarr.shape()[0];
    assert (Qarr.shape()[1]==3);
    array_2d_t::index_t xind[2], yind[2], zind[2];
    xind[1]=0; yind[1]=1; zind[1]=2;
    array_2d_t::index_t Eind[2];
    for (int iQ=0; iQ<nQ; iQ++) {
      xind[0]=yind[0]=zind[0]=Eind[0] = iQ;
      V3 Q(Qarr[xind], Qarr[yind], Qarr[zind]);
      for (int ibr=0; ibr<nbr; ibr++) {
	Eind[1] = ibr;
	Earr[Eind] = disp.energy(ibr, Q);
      }
    }
  }

  void wrap_AbstractDispersion_3D()
  {
    using namespace boost::python;
    typedef DANSE::phonon::AbstractDispersion_3D w_t;

    class_<w_t, boost::noncopyable>
      ("AbstractDispersion_3D", no_init)
      .def("nBranches", &w_t::nBranches )
      .def("nAtoms", &w_t::nAtoms )
      .def("energy", &w_t::energy )
      .def("polarization", &w_t::polarization )
      .def("energy_arr", disp_energies)
      ;
  }

}


// End of file 
