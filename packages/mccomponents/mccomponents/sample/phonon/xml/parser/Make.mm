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
PACKAGE = sample/phonon/xml/parser


BUILD_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS)

#--------------------------------------------------------------------------
#

all: export

tidy::
	BLD_ACTION="tidy" $(MM) recurse



#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractNode.py \
	Document.py \
	HomogeneousScatterer.py \
	LinearlyInterpolatedDispersion.py \
	Phonon_IncoherentElastic_Kernel.py \
	Phonon_CoherentInelastic_PolyXtal_Kernel.py \
	Phonon_CoherentInelastic_SingleXtal_Kernel.py \
	__init__.py \


export:: export-package-python-modules 
	BLD_ACTION="export" $(MM) recurse


#include doxygen/default.def
#docs: export-doxygen-docs


# version
# $Id$

# End of file
