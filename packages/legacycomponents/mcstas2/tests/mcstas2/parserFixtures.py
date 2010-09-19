# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Alex Dementsov
#                      California Institute of Technology
#                        (C) 2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

testtext = """
/*******************************************************************************
*
*
*
* McStas, neutron ray-tracing package
*         Copyright 1997-2002, All rights reserved
*         Risoe National Laboratory, Roskilde, Denmark
*         Institut Laue Langevin, Grenoble, France
*
* Component: E_monitor
*
* %I
* Written by: Kristian Nielsen and Kim Lefmann
* Date: April 20, 1998
* Version: $Revision: 438 $
* Origin: Risoe
* Release: McStas 1.6
*
* Energy-sensitive monitor.
*
* %D
* A square single monitor that measures the energy of the incoming neutrons.
*
* Example: E_monitor(xmin=-0.1, xmax=0.1, ymin=-0.1, ymax=0.1,
*                 Emin=1, Emax=50, nchan=20, filename="Output.nrj")
*
* %P
* INPUT PARAMETERS:
*
* xmin:     Lower x bound of detector opening (m)
* xmax:     Upper x bound of detector opening (m)
* ymin:     Lower y bound of detector opening (m)
* ymax:     Upper y bound of detector opening (m)
* Emin:     Minimum energy to detect (meV)
* Emax:     Maximum energy to detect (meV)
* nchan:    Number of energy channels (1)
* filename: Name of file in which to store the detector image (text)
*
* OUTPUT PARAMETERS:
*
* E_N:      Array of neutron counts
* E_p:      Array of neutron weight counts
* E_p2:     Array of second moments
*
* %E
*******************************************************************************/
the rest of text
"""

snstext = """
DEFINE COMPONENT SNS_source
DEFINITION PARAMETERS ()
SETTING PARAMETERS (char *S_filename="SNS_moderator_data_file",width=0.1, height=0.12, dist=2.5, xw=0.1, yh=0.12, Emin=50, Emax=70)
OUTPUT PARAMETERS (hdiv,vdiv,p_in)
STATE PARAMETERS (x,y,z,vx,vy,vz,t,s1,s2,p)
"""


# XXX: Check if split by lines for definitions is legal
psd_tew = """
DEFINE COMPONENT PSD_TEW_monitor
DEFINITION PARAMETERS (nxchan=20, nychan=20, nbchan=20, string type="time", string filename, string format="table")
SETTING PARAMETERS (xwidth=0, yheight=0, bmin=0, bmax=0, deltab=0,
                    restore_neutron=0)
OUTPUT PARAMETERS (TOF_N, TOF_p, TOF_p2, b_min, b_max, delta_b, x_min, x_max, delta_x, y_min, y_max, delta_y)
STATE PARAMETERS (x,y,z,vx,vy,vz,t,s1,s2,p)
POLARISATION PARAMETERS (sx,sy,sz)
"""
__date__ = "$Sep 15, 2010 3:17:26 PM$"


