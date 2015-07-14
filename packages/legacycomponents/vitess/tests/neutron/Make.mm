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

PROJECT = vitess
PACKAGE = tests

PROJ_TIDY += $(PROJ_CPPTESTS)
PROJ_CLEAN += $(PROJ_CPPTESTS)

# PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = testNeutronSize  
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR)


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

testNeutronSize: testNeutronSize.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testNeutronSize.cc $(PROJ_LIBRARIES)


# version
# $Id$

# End of file
