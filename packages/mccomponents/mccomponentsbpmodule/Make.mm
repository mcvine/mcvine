# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = mccomponents
MODULE = mccomponents
PACKAGE = mccomponentsbpmodule

include std-pythonmodule.def
include local.def


PROJ_CXX_SRCLIB = -lboost_python  -L$(BOOSTPYTHON_LIBDIR) -ljournal -lmccomposite -lmcni -lmccomponents -lfparser


PROJ_SRCS = \
	wrap_basic_containers.cc \
	wrap_HomogeneousNeutronScatterer.cc \
	wrap_AbstractScatteringKernel.cc \
	wrap_CompositeScatteringKernel.cc \
	wrap_kernelcontainer.cc \
	wrap_He3TubeKernel.cc \
	wrap_EventModeMCA.cc \
	wrap_ConstantEnergyTransferKernel.cc \
	wrap_ConstantQEKernel.cc \
	wrap_E_Q_Kernel.cc \
	wrap_SQEkernel.cc \
	wrap_SQkernel.cc \
	wrap_GridSQE.cc \
	wrap_SQE_fromexpression.cc \
	wrap_IsotropicKernel.cc \
	wrap_AtomicScatterer.cc \
	wrap_NdArray.cc \
	wrap_AbstractDOS.cc \
	wrap_LinearlyInterpolatedDOS.cc \
	wrap_AbstractDebyeWallerFactorCalculator.cc \
	wrap_DWFromDOS.cc \
	wrap_LinearlyInterpolatableAxis.cc \
	wrap_epsilon_t.cc \
	wrap_AbstractDispersion_3D.cc \
	wrap_PeriodicDispersion_3D.cc \
	wrap_ChangeCoordinateSystem_forDispersion_3D.cc \
	wrap_LinearlyInterpolatedDispersionOnGrid_3D.cc \
	wrap_Phonon_CoherentInelastic_PolyXtal_kernel.cc \
	wrap_rootsfinders.cc \
	wrap_targetregion.cc \
	wrap_Phonon_CoherentInelastic_SingleXtal_kernel.cc \
	wrap_RandomNumberGenerator.cc \
	wrap_SimplePowderDiffractionKernel.cc \


TOUCH=touch

wrap_basic_containers.cc: wrap_vector.h
	$(TOUCH) wrap_basic_containers.cc

wrap_kernelcontainer.cc: wrap_vector.h
	$(TOUCH) wrap_kernelcontainer.cc


include doxygen/default.def
docs: export-doxygen-docs



# version
# $Id$

# End of file
