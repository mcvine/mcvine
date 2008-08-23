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

PROJECT = SMARTS_Moderator2Sample
PACKAGE = 

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
# export

EXPORT_ETC = \
	__vault__.odb \
	guide1.odb \
	guide1.pml \
	guide2.odb \
	guide2.pml \
	neutron_recorder.odb \
	neutron_recorder.pml \
	slit1.odb \
	slit1.pml \
	slit2.odb \
	slit2.pml \
	source.odb \
	source.pml \


export:: export-etc


# version
# $Id: Make.mm 818 2006-03-01 06:06:22Z linjiao $

# End of file
