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

PROJ_PYTESTS =  
PROJ_CPPTESTS = \
	testmcvine2vitess \
	testvitess2mcvine \

PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lvitess


#--------------------------------------------------------------------------
#

all: $(PROJ_TESTS)

test:
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

tidy::
	BLD_ACTION="tidy" $(MM) recurse

#--------------------------------------------------------------------------
#

testmcvine2vitess: testmcvine2vitess.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testmcvine2vitess.cc $(PROJ_LIBRARIES)

testvitess2mcvine: testvitess2mcvine.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testvitess2mcvine.cc $(PROJ_LIBRARIES)


# version
# $Id$

# End of file
