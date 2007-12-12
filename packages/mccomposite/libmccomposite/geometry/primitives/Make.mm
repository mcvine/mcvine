
include local.def

PROJECT = mccomposite/geometry/primitives

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
	Box.h \
	all.h \



# version
# $Id: Make.mm 300 2005-11-23 10:37:18Z linjiao $

#
# End of file
