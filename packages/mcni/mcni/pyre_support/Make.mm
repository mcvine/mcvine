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
	AbstractNeutronTracer.py \
	ConsoleNeutronTracer.py \
	Instrument.py \
	Geometer.py \
	LauncherMPICH2.py \
	List.py \
	MpiApplication.py \
	NeutronComponentFacility.py \
	NeutronTracerFacility.py \
	NoNeutronTracer.py \
	ParallelComponent.py \
	RegistryToDict.py \
	__init__.py \
	_geometer_utils.py \
	_invutils.py \
	compareRegistry.py \
	component_suppliers.py \


export:: export-package-python-modules



# version
# $Id$

# End of file
