# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                        California Institute of Technology
#                        (C) 2007-2008  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mcni

BUILD_DIRS = \
	bindings  \
	components  \
	coordinate_system_transformers \
	instrument_simulator  \
	neutron_coordinates_transformers  \
	neutron_storage  \
	pyre_components  \
	pyre_support  \
	utils  \

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
	component_suppliers.py \
	rng_seed.py \
	seeder.py \
	units.py \
	_component_listing.py \
	_component_factories.py \
	_find_component.py \


export:: export-python-modules 
	BLD_ACTION="export" $(MM) recurse


include doxygen/default.def
docs: export-doxygen-docs


# version
# $Id: Make.mm 1404 2007-08-29 15:43:42Z linjiao $

# End of file
