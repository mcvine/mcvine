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
PROJ_CPPTESTS = testVector3 testMatrix3 testcoords_transform
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -ljournal -lmcni


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

testVector3: testVector3.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testVector3.cc $(PROJ_LIBRARIES)

testMatrix3: testMatrix3.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testMatrix3.cc $(PROJ_LIBRARIES)

testcoords_transform: testcoords_transform.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testcoords_transform.cc $(PROJ_LIBRARIES)


# version
# $Id: Make.mm 620 2007-07-11 23:24:50Z linjiao $

# End of file
