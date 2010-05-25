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
PACKAGE = pyre_support

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
	AbstractComponent.py \
	Instrument.py \
	Geometer.py \
	LauncherMPICH2.py \
	List.py \
	MpiApplication.py \
	NeutronComponentFacility.py \
	ParallelComponent.py \
	__init__.py \
	_invutils.py \
	component_suppliers.py \


export:: export-package-python-modules



# version
# $Id: Make.mm 1212 2006-11-21 21:59:44Z linjiao $

# End of file
