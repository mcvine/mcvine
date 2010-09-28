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

PROJECT = mcvine
PACKAGE = tests

PROJ_CLEAN += $(PROJ_CPPTESTS) 
PROJ_TIDY += *.dat
PROJ_PRUNE = out

PROJ_PYTESTS =
PROJ_CPPTESTS = 
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR)




# directory structure

BUILD_DIRS = \
	mcvine \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all: $(PROJ_TESTS)
	BLD_ACTION="all" $(MM) recurse

test:
	for test in $(PROJ_TESTS) ; do $${test}; done
	BLD_ACTION="test" $(MM) recurse

tidy:: prune
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse


#--------------------------------------------------------------------------
#
REMOVE_ALL = rm -rf
prune: 	
	rm -rf $(PROJ_PRUNE)


# version
# $Id$

# End of file
