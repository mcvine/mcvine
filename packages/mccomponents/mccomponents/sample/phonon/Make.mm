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
	AbstractPhononKernel.py \
	CoherentInelastic_PolyXtal_Kernel.py \
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
# $Id: Make.mm 1234 2007-09-18 18:32:56Z linjiao $

# End of file
