// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2007 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>

namespace wrap_mccomponents{
  void wrap_basic_containers();

  void wrap_HomogeneousNeutronScatterer();
  void wrap_AbstractScatteringKernel();
  void wrap_CompositeScatteringKernel();
  void wrap_kernelcontainer();

  void wrap_He3TubeKernel();
  void wrap_EventModeMCA();
  void wrap_SQEkernel();
  void wrap_GridSQE();

  void wrap_NdArray();
  void wrap_LinearlyInterpolatableAxis();
  void wrap_LinearlyInterpolatedDispersionOnGrid_3D();
  void wrap_epsilon_t();
  void wrap_AbstractDispersion_3D();
  void wrap_Phonon_CoherentInelastic_PolyXtal_kernel();
}


BOOST_PYTHON_MODULE(mccomponentsbp)
{
  using namespace boost::python;
  using namespace wrap_mccomponents;
  
  wrap_basic_containers();

  wrap_HomogeneousNeutronScatterer();
  wrap_AbstractScatteringKernel();
  wrap_CompositeScatteringKernel();
  wrap_kernelcontainer();

  wrap_He3TubeKernel();
  wrap_EventModeMCA();
  wrap_SQEkernel();
  wrap_GridSQE();

  wrap_NdArray();
  wrap_LinearlyInterpolatableAxis();
  wrap_LinearlyInterpolatedDispersionOnGrid_3D();
  wrap_epsilon_t();
  wrap_AbstractDispersion_3D();
  wrap_Phonon_CoherentInelastic_PolyXtal_kernel();

}


// version
// $Id: mccompositebpmodule.cc 658 2007-10-24 21:33:08Z linjiao $

// End of file 
