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

"""
McStasConverter - converts McStas component to the McVine component

Example:

McStas component:

COMPONENT L_monitor9 = L_monitor(
    nchan = 140, filename = "Vulcan_asbuilt_L_monitor9.txt",
    xwidth = 0.15, yheight = 0.15, Lmin = 0.0, Lmax = 14.0,
    restore_neutron = 1)
  AT (0, 0, 0.971)  RELATIVE  FU_Out

is converted to:

{"name":        "L_monitor9",
"type":         "L_monitor",
"position":     "AT (0, 0, 0.971)  RELATIVE  FU_Out",
"extra":        [], # like ROTATION
"parameters": {	"nchan": "140",
		"filename": "'Vulcan_asbuilt_L_monitor9.txt'",
		"xwidth": "0.15",
		"yheight": "0.15",
		"Lmin": "0.0",
		"Lmax": "14.0",
		"restore_neutron": "1"}

Issues:
    - Check if name is case sensitive (like COMPONENT)
    - Extract properties from "extra" to separate properties
"""

# XXX: Figure out what other metadata to extract from "extra" properties

tempText = """COMPONENT L_monitor9 = L_monitor(
    nchan = 140, filename = "Vulcan_asbuilt_L_monitor9.txt",
    xwidth = 0.15, yheight = 0.15, Lmin = 0.0, Lmax = 14.0,
    restore_neutron = 1)
  AT (0, 0, 0.971)  RELATIVE  FU_Out"""



# Regular expressions
SPACES          = '[ \t]*'              # Spaces and tabs
NAME            = '%s([^ ()=]*)%s' % (SPACES, SPACES)  # Extracts name
NO_BRACKETS     = '[^()]*'              # No brackets
PARAMETERS      = '(%s)' % NO_BRACKETS  # Component parameters
COMPONENT       = "COMPONENT%s=%s\(%s\)" %(NAME, NAME, PARAMETERS)  # Component

import re

class McStasConverter:

    def __init__(self, filename):
        self._filename      = filename
        self._components    = []    # list of dictionaries

    def parse(self):
        str = "COMPONENT L_monitor9 = L_monitor(\nhello)"
        p   = re.compile(COMPONENT)
        matches     = p.findall(tempText)        # Finds all components

        print matches
        
#        for m in matches:
#            name    = m[0].lower()
#            print name


    # XXX: Fix
    def toString(self):
        print self._components


if __name__ == "__main__":
    conv    = McStasConverter("hi")
    conv.parse()

__date__ = "$Aug 19, 2010 10:25:18 AM$"


