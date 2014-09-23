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

PROJ_TIDY += $(PROJ_CPPTESTS)
PROJ_CLEAN += $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = \
	testAbstractNeutronScatterer \
	testCompositeNeutronScatterer \
	testGeometer \
	test_neutron_propagation \
	testMultipleScattering \

PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lmccomposite -lmcni -ljournal


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

testCompositeNeutronScatterer: testCompositeNeutronScatterer.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testCompositeNeutronScatterer.cc $(PROJ_LIBRARIES)

testGeometer: testGeometer.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testGeometer.cc $(PROJ_LIBRARIES)

test_neutron_propagation: test_neutron_propagation.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_neutron_propagation.cc $(PROJ_LIBRARIES)

testMultipleScattering: testMultipleScattering.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testMultipleScattering.cc $(PROJ_LIBRARIES)


# version
# $Id$

# End of file
