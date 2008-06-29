# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                        (C) 2008 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mcni
PACKAGE = components/_neutron_storage_impl


BUILD_DIRS = \


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
	PacketSizeStore.py \
	__init__.py \


export:: export-package-python-modules
	BLD_ACTION="export" $(MM) recurse


# version
# $Id$

# End of file
