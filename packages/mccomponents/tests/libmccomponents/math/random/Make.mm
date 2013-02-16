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
	test_gaussian \
	test_gaussian_gsl \

PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lmccomponents -lmccomposite -lmcni -ljournal -lfparser


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

test_gaussian: test_gaussian.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_gaussian.cc $(PROJ_LIBRARIES)

test_gaussian_gsl: test_gaussian_gsl.cc 
	$(CXX) $(CXXFLAGS) $(LCXXFLAGS) -o $@ test_gaussian_gsl.cc $(PROJ_LIBRARIES) -lgsl -lgslcblas

# version
# $Id: Make.mm 652 2010-10-22 12:31:15Z linjiao $

# End of file
