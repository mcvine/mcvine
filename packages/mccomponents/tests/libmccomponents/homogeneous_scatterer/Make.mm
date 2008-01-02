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

PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = test_random testHomogeneousNeutronScatterer testCompositeScatteringKernel
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -ljournal -lmcni -lmccomposite -lmcstas_compact -lmccomponents


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

test_random: test_random.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_random.cc $(PROJ_LIBRARIES)

testHomogeneousNeutronScatterer: testHomogeneousNeutronScatterer.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testHomogeneousNeutronScatterer.cc $(PROJ_LIBRARIES)

testCompositeScatteringKernel: testCompositeScatteringKernel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testCompositeScatteringKernel.cc $(PROJ_LIBRARIES)



# version
# $Id: Make.mm 620 2007-07-11 23:24:50Z linjiao $

# End of file
