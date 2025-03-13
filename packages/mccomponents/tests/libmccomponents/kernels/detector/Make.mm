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
	testTof2Channel \
	testZ2Channel \
	testHe3Tube \
	testEventModeMCA \
	testHe3 \
	//testevents2iqe \

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

testTof2Channel: testTof2Channel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testTof2Channel.cc $(PROJ_LIBRARIES)

testZ2Channel: testZ2Channel.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testZ2Channel.cc $(PROJ_LIBRARIES)

testHe3Tube: testHe3Tube.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testHe3Tube.cc $(PROJ_LIBRARIES)

testHe3: testHe3.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testHe3.cc $(PROJ_LIBRARIES)

testEventModeMCA: testEventModeMCA.cc
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testEventModeMCA.cc $(PROJ_LIBRARIES)

//testevents2iqe: testevents2iqe.cc
//	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ testevents2iqe.cc $(PROJ_LIBRARIES)


# version
# $Id$

# End of file
