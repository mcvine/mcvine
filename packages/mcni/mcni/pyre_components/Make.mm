# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               T. M. Kelley
#                        (C) 1998-2003 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mcni
PACKAGE = pyre_components

#--------------------------------------------------------------------------
#

all: export

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	Dummy.py \
	Monitor1D.py \
	Monitor2D.py \
	MonochromaticSource.py \
	MultiMonitors.py \
	NeutronFromStorage.py \
	NeutronPrinter.py \
	NeutronToStorage.py \
	NeutronsOnCone_FixedQE.py \
	Registry.py \
	__init__.py \
	beam_analyzer.py \
	repositories.py \


export:: export-package-python-modules



# version
# $Id$

# End of file
