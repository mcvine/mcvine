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

PROJECT = mccomposite/geometry

# directory structure

BUILD_DIRS = \
	operations \
	primitives \
	visitors \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# build the library

all: export
	BLD_ACTION="all" $(MM) recurse


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
export:: export-package-headers

EXPORT_HEADERS = \
	AbstractShape.h \
	AbstractShapeVisitor.h \
	Direction.h \
	Position.h \
	RotationMatrix.h \
	Vector.h \
	exception.h \
	geometry.h \
	intersect.h intersect.icc \
	locate.h \
	operations.h \
	primitives.h \
	tolerance.h \
	shape2ostream.h \
	shapes.h \


# version
# $Id$

#
# End of file
