# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

include local.def

PROJECT = mccomponents
PACKAGE = libmccomponents


# library
PROJ_SAR = $(BLD_LIBDIR)/$(PACKAGE).$(EXT_SAR)
PROJ_DLL = $(BLD_BINDIR)/$(PACKAGE).$(EXT_SO)
PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)
PROJ_CLEAN += $(PROJ_SAR) $(PROJ_DLL)


#--------------------------------------------------------------------------
# build the library
all: $(PROJ_SAR) export

#--------------------------------------------------------------------------


PROJ_SRCS = \
	HomogeneousNeutronScatterer.cc \
	random.cc \
	rootfinding.cc \
	Functor.cc \
	math_misc.cc \
	random_geometry.cc \
	random_gaussian.cc \
	CompositeScatteringKernel.cc \
	IsotropicKernel.cc \
	EventModeMCA.cc \
	He3.cc \
	He3Tube.cc \
	ConstantEnergyTransferKernel.cc \
	ConstantQEKernel.cc \
	SimplePowderDiffractionKernel.cc \
	SQkernel.cc \
	SQEkernel.cc \
	GridSQE.cc \
	SQE_fromexpression.cc \
	AbstractDispersion_3D.cc \
	AtomicScatterer.cc \
	ChangeCoordinateSystem_forDispersion_3D.cc \
	LinearlyInterpolatedDispersionOnGrid_3D.cc \
	kernels_sample_phonon_utils.cc \
	physics_statistics.cc \
	DWFromDOS.cc \
	CoherentInelastic_PolyXtal.cc \
	CoherentInelastic_SingleXtal.cc \
	IncoherentElastic.cc \
	PeriodicDispersion_3D.cc \
	Omega_minus_deltaE.cc \
	TargetCone.cc \


PROJ_TIDY += $(PROJ_SRCS)


HomogeneousNeutronScatterer.cc: ../homogeneous_scatterer/HomogeneousNeutronScatterer.cc
	cp ../homogeneous_scatterer/HomogeneousNeutronScatterer.cc .

random.cc: ../math/random.cc
	cp ../math/random.cc .

math_misc.cc: ../math/misc.cc
	cp ../math/misc.cc ./math_misc.cc

rootfinding.cc: ../math/rootfinding.cc
	cp ../math/rootfinding.cc .

Functor.cc: ../math/Functor.cc
	cp ../math/Functor.cc .

random_geometry.cc: ../math/random/geometry.cc
	cp ../math/random/geometry.cc ./random_geometry.cc

random_gaussian.cc: ../math/random/gaussian.cc
	cp ../math/random/gaussian.cc ./random_gaussian.cc

CompositeScatteringKernel.cc: ../homogeneous_scatterer/CompositeScatteringKernel.cc
	cp ../homogeneous_scatterer/CompositeScatteringKernel.cc .

IsotropicKernel.cc: ../kernels/IsotropicKernel.cc
	cp ../kernels/IsotropicKernel.cc .

He3.cc: ../kernels/detector/He3.cc
	cp ../kernels/detector/He3.cc .

He3Tube.cc: ../kernels/detector/He3Tube.cc
	cp ../kernels/detector/He3Tube.cc .

EventModeMCA.cc: ../kernels/detector/EventModeMCA.cc
	cp ../kernels/detector/EventModeMCA.cc .

ConstantEnergyTransferKernel.cc: ../kernels/sample/ConstantEnergyTransferKernel.cc
	cp ../kernels/sample/ConstantEnergyTransferKernel.cc .

ConstantQEKernel.cc: ../kernels/sample/ConstantQEKernel.cc
	cp ../kernels/sample/ConstantQEKernel.cc .

SimplePowderDiffractionKernel.cc: ../kernels/sample/diffraction/SimplePowderDiffractionKernel.cc
	cp ../kernels/sample/diffraction/SimplePowderDiffractionKernel.cc .

SQEkernel.cc: ../kernels/sample/SQEkernel.cc
	cp ../kernels/sample/SQEkernel.cc .

SQkernel.cc: ../kernels/sample/SQkernel.cc
	cp ../kernels/sample/SQkernel.cc .

GridSQE.cc: ../kernels/sample/SQE/GridSQE.cc
	cp ../kernels/sample/SQE/GridSQE.cc .

SQE_fromexpression.cc: ../kernels/sample/SQE/SQE_fromexpression.cc
	cp ../kernels/sample/SQE/SQE_fromexpression.cc .

AtomicScatterer.cc: ../kernels/sample/phonon/AtomicScatterer.cc
	cp ../kernels/sample/phonon/AtomicScatterer.cc .

AbstractDispersion_3D.cc: ../kernels/sample/phonon/AbstractDispersion_3D.cc
	cp ../kernels/sample/phonon/AbstractDispersion_3D.cc .

PeriodicDispersion_3D.cc: ../kernels/sample/phonon/PeriodicDispersion_3D.cc
	cp ../kernels/sample/phonon/PeriodicDispersion_3D.cc .

ChangeCoordinateSystem_forDispersion_3D.cc: ../kernels/sample/phonon/ChangeCoordinateSystem_forDispersion_3D.cc
	cp ../kernels/sample/phonon/ChangeCoordinateSystem_forDispersion_3D.cc .

LinearlyInterpolatedDispersionOnGrid_3D.cc: ../kernels/sample/phonon/LinearlyInterpolatedDispersionOnGrid_3D.cc
	cp ../kernels/sample/phonon/LinearlyInterpolatedDispersionOnGrid_3D.cc .

kernels_sample_phonon_utils.cc: ../kernels/sample/phonon/utils.cc
	cp ../kernels/sample/phonon/utils.cc kernels_sample_phonon_utils.cc

physics_statistics.cc: ../physics/statistics.cc
	cp ../physics/statistics.cc physics_statistics.cc

CoherentInelastic_PolyXtal.cc: ../kernels/sample/phonon/CoherentInelastic_PolyXtal.cc
	cp ../kernels/sample/phonon/CoherentInelastic_PolyXtal.cc CoherentInelastic_PolyXtal.cc

CoherentInelastic_SingleXtal.cc: ../kernels/sample/phonon/CoherentInelastic_SingleXtal.cc
	cp ../kernels/sample/phonon/CoherentInelastic_SingleXtal.cc CoherentInelastic_SingleXtal.cc

IncoherentElastic.cc: ../kernels/sample/phonon/IncoherentElastic.cc
	cp ../kernels/sample/phonon/IncoherentElastic.cc IncoherentElastic.cc

DWFromDOS.cc: ../kernels/sample/phonon/DWFromDOS.cc
	cp ../kernels/sample/phonon/DWFromDOS.cc DWFromDOS.cc

Omega_minus_deltaE.cc: ../kernels/sample/phonon/Omega_minus_deltaE.cc
	cp ../kernels/sample/phonon/Omega_minus_deltaE.cc Omega_minus_deltaE.cc

TargetCone.cc: ../kernels/sample/phonon/TargetCone.cc
	cp ../kernels/sample/phonon/TargetCone.cc TargetCone.cc


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ifeq (Win32, ${findstring Win32, $(PLATFORM_ID)})

# build the shared object
$(PROJ_SAR): product_dirs $(PROJ_OBJS)
	$(CXX) $(LCXXFLAGS) -o $(PROJ_DLL) \
	-Wl,--out-implib=$(PROJ_SAR) $(PROJ_OBJS)

# export
export:: export-headers export-libraries export-binaries

else

# build the shared object
$(PROJ_SAR): product_dirs $(PROJ_OBJS)
	$(CXX) $(LCXXFLAGS) -o $(PROJ_SAR) $(PROJ_OBJS)

# export
export:: export-headers export-libraries

endif

EXPORT_HEADERS = \


EXPORT_LIBS = $(PROJ_SAR)
EXPORT_BINS = $(PROJ_DLL)


# version
# $Id$

#
# End of file

