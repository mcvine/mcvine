# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = mccomponents
PACKAGE = tests

PROJ_TIDY += $(PROJ_CPPTESTS)
PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = \
	testHomogeneousNeutronScatterer \
	testCompositeScatteringKernel \
	testMultipleScattering \


PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)

PROJ_CXX_INCLUDES += $(DANSE_DIR)/include $(DANSE_DIR)/include/danse/ins
PROJ_LIBRARIES = -L$(BLD_LIBDIR) \
	-lmccomponents -lmccomposite -lmcni \
	-lfparser \
	-lgsl -lgslcblas -L$(GSL_LIBDIR) \
	-ljournal \
	-L$(DANSE_DIR)/lib -L$(DANSE_DIR)/lib64

#--------------------------------------------------------------------------
#

all: $(PROJ_TESTS)

test:
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#

testHomogeneousNeutronScatterer: testHomogeneousNeutronScatterer.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testHomogeneousNeutronScatterer.cc $(PROJ_LIBRARIES)

testMultipleScattering: testMultipleScattering.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testMultipleScattering.cc $(PROJ_LIBRARIES)

testCompositeScatteringKernel: testCompositeScatteringKernel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testCompositeScatteringKernel.cc $(PROJ_LIBRARIES)



# version
# $Id$

# End of file
