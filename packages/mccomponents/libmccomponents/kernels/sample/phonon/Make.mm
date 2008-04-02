# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

include local.def

PROJECT = mccomponents
PACKAGE = kernels/sample/phonon


PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)


# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)



all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
export:: export-package-headers

EXPORT_HEADERS = \
	AbstractDispersion_3D.h \
	PeriodicDispersion_3D.h \
	AbstractDebyeWallerFactor.h \
	AbstractDOS.h \
	AbstractScatteringKernel.h \
	AtomicScatterer.h \
	CoherentInelastic_PolyXtal.h \
	DWFromDOS.h \
	DWFromDOS.icc \
	LinearlyInterpolatableAxis.h \
	LinearlyInterpolatedDOS.h \
	LinearlyInterpolatedDOS.icc \
	LinearlyInterpolatedGridData_1D.h \
	LinearlyInterpolatedGridData_1D.icc \
	LinearlyInterpolatedGridData_3D.h \
	LinearlyInterpolatedGridData_3D.icc \
	LinearlyInterpolatedDispersionOnGrid_3D.h \
	LinearlyInterpolatedDispersionOnGrid_3D.icc \
	LinearlyInterpolatedPolarizationOnGrid_3D.h \
	LinearlyInterpolatedPolarizationOnGrid_3D.icc \
	exception.h \
	generateQ.h generateQ.icc \
	interpolate.h \
	scattering_length.h scattering_length.icc \
	utils.h \
	vector3.h \


# version
# $Id: Make.mm,v 1.1.1.1 2005/03/08 16:13:51 aivazis Exp $

#
# End of file
