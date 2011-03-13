# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mcvineui
PACKAGE = content

RECURSE_DIRS = \

EXPORT_PACKAGE_DATA_DIRS = \
	components \
	images \

EXPORT_DATAFILES = \


OTHERS = \

#--------------------------------------------------------------------------
#

all: export-package-data
	BLD_ACTION="all" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse



export-package-data:: export-package-data-dirs export-package-data-files 

include luban/default.def


# version
# $Id$

# End of file
