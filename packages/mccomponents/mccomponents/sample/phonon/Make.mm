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

PROJECT = mccomponents
PACKAGE = sample/phonon

BUILD_DIRS = \
	bindings \
	xml \

RECURSE_DIRS = $(BUILD_DIRS)

#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractDOS.py \
	AbstractDispersion.py \
	PeriodicDispersion.py \
	AbstractPhononKernel.py \
	IncoherentElastic_Kernel.py \
	IncoherentInelastic_Kernel.py \
	CoherentInelastic_PolyXtal_Kernel.py \
	CoherentInelastic_SingleXtal_Kernel.py \
	ComputationEngineRendererExtension.py \
	DWFromDOS.py \
	DispersionOnGrid.py \
	LinearlyInterpolatedDOS.py \
	LinearlyInterpolatedDispersionOnGrid.py \
	NdArray.py \
	__init__.py \
	units.py \


export:: export-package-python-modules 


# version
# $Id$

# End of file
