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

PROJECT = simulation
PACKAGE = tests

PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = testAbstractNeutronScatterer testAbstractNeutronComponent 
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -ljournal -lmccomposite


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

testAbstractNeutronScatterer: testAbstractNeutronScatterer.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testAbstractNeutronScatterer.cc $(PROJ_LIBRARIES)

testAbstractNeutronComponent: testAbstractNeutronComponent.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testAbstractNeutronComponent.cc $(PROJ_LIBRARIES)


# version
# $Id: Make.mm 620 2007-07-11 23:24:50Z linjiao $

# End of file
