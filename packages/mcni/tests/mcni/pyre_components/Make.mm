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

PROJECT = mcni
PACKAGE = tests

TESTTEMPOUTPUTDIRS = \
	neutron_storage_test_out\
	neutrons\

PROJ_TIDY += alltests.py $(PROJ_CPPTESTS) $(TESTTEMPOUTPUTDIRS)
PROJ_CLEAN += alltests.py $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = 
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lmcni


#--------------------------------------------------------------------------
#

all: $(PROJ_TESTS)
	BLD_ACTION="all" $(MM) recurse

test: alltests.py
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#

alltests.py: ../alltests.py
	cp ../alltests.py .


# version
# $Id$

# End of file
