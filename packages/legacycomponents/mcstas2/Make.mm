
PROJECT = mcstas2

# directory structure

BUILD_DIRS = \
    examples \
    lib \
    mcstas2 \
    component_library \


OTHER_DIRS = \


RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all:
	BLD_ACTION="all" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

export::
	BLD_ACTION="export" $(MM) recurse

# version
# $Id: Make.mm 410 2006-04-17 06:11:45Z jiao $

