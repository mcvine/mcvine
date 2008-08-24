# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = SANS_Prototype
PACKAGE = 

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
# export

EXPORT_ETC = \
	__vault__.odb \
	detector.odb \
	detector.pml \
	neutron_recorder.odb \
	neutron_recorder.pml \
	sample.odb \
	sample.pml \
	source.odb \
	source.pml \


export:: export-etc


# version
# $Id: Make.mm 818 2006-03-01 06:06:22Z linjiao $

# End of file
