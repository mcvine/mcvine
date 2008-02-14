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
	MonochromaticSource.py \
	NeutronFromStorage.py \
	NeutronToStorage.py \
	NeutronsOnCone_FixedQE.py \
	Registry.py \
	__init__.py \
	repositories.py \


export:: export-package-python-modules



# version
# $Id: Make.mm 1212 2006-11-21 21:59:44Z linjiao $

# End of file
