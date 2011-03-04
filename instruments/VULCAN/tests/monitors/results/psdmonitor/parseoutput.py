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

# See: http://dev.danse.us/trac/EngDiffSimulation/browser/SMARTSsimulation/trunk/SMARTS/parsers/psd_tew_monitor_parser.py
from psd_tew_monitor_parser import PSD_TEW_monitorParser

p   = PSD_TEW_monitorParser()

p.parse("tc.txt")
p.distToFile("tc_plot.txt", 0, 0)

p.parse("wc.txt")
p.distToFile("wc_plot.txt", 0, 0)

__date__ = "$Jan 14, 2011 3:35:33 PM$"


