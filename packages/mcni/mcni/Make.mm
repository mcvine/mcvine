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

PROJECT = mcni

BUILD_DIRS = \
    instrument_simulator  \
    neutron_coordinates_transformers  \
    neutron_storage  \
    pyre_support  \

RECURSE_DIRS = $(BUILD_DIRS)

PACKAGE = mcni

#--------------------------------------------------------------------------
#

all: export

tidy::
	BLD_ACTION="tidy" $(MM) recurse



#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractComponent.py \
	DummyComponent.py \
	Geometer.py \
	Instrument.py \
	__init__.py \



export:: export-python-modules 
	BLD_ACTION="export" $(MM) recurse


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 1404 2007-08-29 15:43:42Z linjiao $

# End of file
