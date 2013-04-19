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

PROJECT = sequoia_analyze_beam
PACKAGE = 

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
# export

EXPORT_ETC = \
	sequoia_analyze_beam.pml \
	beam_analyzer.odb \


export:: export-etc

# version
# $Id: Make.mm 601 2010-10-03 19:55:29Z linjiao $

# End of file
