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
PACKAGE = kernels/sample


PROJ_TMPDIR = $(BLD_TMPDIR)/$(PROJECT)/$(PACKAGE)


# directory structure

BUILD_DIRS = \
	SQE \
	diffraction \
	phonon \

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
	AbstractScatteringKernel.h \
	AbstractSQ.h \
	AbstractSQE.h \
	Broadened_E_Q_Kernel.h Broadened_E_Q_Kernel.icc \
	ConstantEnergyTransferKernel.h \
	ConstantQEKernel.h \
	E_Q_Kernel.h \
	E_Q_Kernel.icc \
	E_Q_Kernel_helpers.h \
	E_vQ_Kernel.h \
	E_vQ_Kernel.icc \
	SQAdaptor.h \
	SQkernel.h \
	SQEkernel.h \


# version
# $Id$

#
# End of file
