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
PACKAGE = neutron_storage


BUILD_DIRS = \
	_neutron_storage_impl  \


RECURSE_DIRS = $(BUILD_DIRS)

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
	Storage.py \
	__init__.py \
	idfneutron.py \
	idf_usenumpy.py \
	idf_usestruct.py \
	merge.py \


export:: export-package-python-modules
	BLD_ACTION="export" $(MM) recurse



# version
# $Id: Make.mm 1212 2006-11-21 21:59:44Z linjiao $

# End of file
