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

PROJECT = ARCS_Moderator2Sample
PACKAGE = 

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
# export

EXPORT_ETC = \
	core_vessel_insert.odb core_vessel_insert.pml \
	energy_monitor1.odb energy_monitor1.pml \
	fermi_chopper.odb fermi_chopper.pml \
	guide1.odb guide1.pml \
	guide2.odb guide2.pml \
	guide3.odb guide3.pml \
	guide4.odb guide4.pml \
	guide5.odb guide5.pml \
	neutron_recorder.odb neutron_recorder.pml \
	shutter_guide.odb shutter_guide.pml \
	sns_moderator_beamline18.odb sns_moderator_beamline18.pml \
	t0_chopper.odb t0_chopper.pml \
	tof_monitor1.odb tof_monitor1.pml \
	__vault__.odb \


export:: export-etc

# version
# $Id$

# End of file
