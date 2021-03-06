# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


PROJECT = mccomposite/tests
PACKAGE = libmccomposite


# directory structure

BUILD_DIRS = \
	geometry \
	mccomposite \
	boostpython_binding \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
# build the library
all: 
	BLD_ACTION="all" $(MM) recurse

test: 
	BLD_ACTION="test" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

#--------------------------------------------------------------------------



# version
# $Id$

#
# End of file

