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

PROJECT = mccomposite
PACKAGE = tests

PROJ_TIDY += alltests.py $(PROJ_CPPTESTS)
PROJ_CLEAN += alltests.py $(PROJ_CPPTESTS)

PROJ_PYTESTS =  alltests.py
PROJ_CPPTESTS = 
PROJ_TESTS = $(PROJ_PYTESTS) $(PROJ_CPPTESTS)
PROJ_LIBRARIES = -L$(BLD_LIBDIR) -lmcni


# directory structure

BUILD_DIRS = \
	extensions \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: neutron_printer2 $(PROJ_TESTS)
	BLD_ACTION="all" $(MM) recurse	

tidy::
	BLD_ACTION="tidy" $(MM) recurse	

test: alltests.py
	for test in $(PROJ_TESTS) ; do $${test}; done

release: tidy
	cvs release .

update: clean
	cvs update .

#--------------------------------------------------------------------------
#


neutron_printer2::
	cd neutron_printer2 ; $(MM) ; cd - 


alltests.py: ../alltests.py
	cp ../alltests.py .


# version
# $Id$

# End of file
