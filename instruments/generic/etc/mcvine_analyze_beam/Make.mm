# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                    Jiao Lin
#                        California Institute of Technology
#                        (C) 2006-2014  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = mcvine_analyze_beam
PACKAGE = 

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
# export

EXPORT_ETC = \
	mcvine_analyze_beam.pml \
	beam_analyzer.odb \


export:: export-etc

# version
# $Id: Make.mm 601 2010-10-03 19:55:29Z linjiao $

# End of file
