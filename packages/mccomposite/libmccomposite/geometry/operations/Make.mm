# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

include local.def

PROJECT = mccomposite/geometry/operations

# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# build the library

all: export
	BLD_ACTION="all" $(MM) recurse

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# export
export:: export-headers 
	BLD_ACTION="export" $(MM) recurse


EXPORT_HEADERS = \
	AbstractShape.h \
	AbstractShapeVisitor.h \
	Composition.h \
	Difference.h \
	Dilation.h \
	Intersection.h \
	Reflection.h \
	Rotation.h \
	Transformation.h \
	Translation.h \
	Union.h \
	all.h \


# version
# $Id: Make.mm 300 2005-11-23 10:37:18Z linjiao $

#
# End of file
