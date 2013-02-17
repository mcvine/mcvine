// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                      (C) 2005-2013 All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//


#include <boost/python.hpp>


#include "wrap_E_Q_Kernel.h"
#include "wrap_E_vQ_Kernel.h"
#include "wrap_Broadened_E_Q_Kernel.h"


namespace wrap_mccomponents{
  
  void wrap_basic_containers();

  void wrap_HomogeneousNeutronScatterer();
  void wrap_AbstractScatteringKernel();
  void wrap_CompositeScatteringKernel();
  void wrap_kernelcontainer();

  void wrap_IsotropicKernel();

  void wrap_He3TubeKernel();
  void wrap_EventModeMCA();
  void wrap_ConstantEnergyTransferKernel();
  void wrap_ConstantQEKernel();
  void wrap_SQEkernel();
  void wrap_SQkernel();
  void wrap_GridSQE();
  void wrap_SQE_fromexpression();

  void wrap_NdArray();
  void wrap_AbstractDOS();
  void wrap_LinearlyInterpolatedDOS();
  void wrap_LinearlyInterpolatableAxis();
  void wrap_epsilon_t();
  void wrap_AbstractDebyeWallerFactorCalculator();
  void wrap_DWFromDOS();
  void wrap_AbstractDispersion_3D();
  void wrap_PeriodicDispersion_3D();
  void wrap_ChangeCoordinateSystem_forDispersion_3D();
  void wrap_LinearlyInterpolatedDispersionOnGrid_3D();
  void wrap_AtomicScatterer();
  void wrap_Phonon_IncoherentElastic_kernel();
  void wrap_Phonon_IncoherentInelastic_kernel();
  void wrap_Phonon_CoherentInelastic_PolyXtal_kernel();
  void wrap_rootsfinders();
  void wrap_targetregion();
  void wrap_Phonon_CoherentInelastic_SingleXtal_kernel();
  void wrap_RandomNumberGenerator();
  void wrap_SimplePowderDiffractionKernel();

  struct Wrap_E_Q_Kernel;
  struct Wrap_Broadened_E_Q_Kernel;
  struct Wrap_E_vQ_Kernel;
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

  wrap_IsotropicKernel();

  wrap_He3TubeKernel();
  wrap_EventModeMCA();

  wrap_ConstantEnergyTransferKernel();
  wrap_ConstantQEKernel();
  wrap_SQEkernel();
  wrap_SQkernel();

  wrap_GridSQE();
  wrap_SQE_fromexpression();

  wrap_NdArray();
  wrap_AbstractDOS();
  wrap_LinearlyInterpolatedDOS();
  wrap_LinearlyInterpolatableAxis();
  wrap_epsilon_t();
  wrap_AbstractDebyeWallerFactorCalculator();
  wrap_DWFromDOS();
  wrap_AbstractDispersion_3D();
  wrap_PeriodicDispersion_3D();
  wrap_ChangeCoordinateSystem_forDispersion_3D();
  wrap_LinearlyInterpolatedDispersionOnGrid_3D();

  wrap_Phonon_IncoherentElastic_kernel();
  wrap_Phonon_IncoherentInelastic_kernel();
  
  wrap_AtomicScatterer();
  wrap_Phonon_CoherentInelastic_PolyXtal_kernel();

  wrap_rootsfinders();
  wrap_targetregion();
  wrap_Phonon_CoherentInelastic_SingleXtal_kernel();

  wrap_RandomNumberGenerator();

  wrap_SimplePowderDiffractionKernel();

  Wrap_E_Q_Kernel wrap_e_q_kernel;
  Wrap_Broadened_E_Q_Kernel wrap_broadened_e_q_kernel;
  Wrap_E_vQ_Kernel wrap_e_vq_kernel;
}


// version
// $Id$

// End of file 
