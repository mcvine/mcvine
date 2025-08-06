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


PROJECT = mccomponents/tests
PACKAGE = libmccomponents/kernels


PROJ_TIDY += $(PROJ_CPPTESTS)
PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  #alltests.py
PROJ_CPPTESTS = test_SimplePowderDiffractionKernel \


PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)

PROJ_CXX_INCLUDES += $(DANSE_DIR)/include $(DANSE_DIR)/include/danse/ins
PROJ_LIBRARIES = -L$(BLD_LIBDIR) \
	-lmccomponents -lmccomposite -lmcni \
	-lfparser \
	-lgsl -lgslcblas -L$(GSL_LIBDIR) \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64
# PROJ_CXX_DEFINES += DEEPDEBUG


# directory structure

BUILD_DIRS = \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
# build the library
all: $(PROJ_TESTS)
	BLD_ACTION="all" $(MM) recurse

test: $(PROJ_TESTS)
	for test in $(PROJ_TESTS) ; do $${test}; done
	BLD_ACTION="test" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

#--------------------------------------------------------------------------


test_SimplePowderDiffractionKernel: test_SimplePowderDiffractionKernel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_SimplePowderDiffractionKernel.cc $(PROJ_LIBRARIES)


# version
# $Id$

#
# End of file

