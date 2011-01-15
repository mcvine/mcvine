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

p.parse("tt.txt")
p.toFile("tt_plot.txt", bin="x")

p.parse("tc.txt")
p.toFile("tc_plot.txt", bin="x")

p.parse("tb.txt")
p.toFile("tb_plot.txt", bin="x")

p.parse("wt.txt")
p.toFile("wt_plot.txt", bin="x")

p.parse("wc.txt")
p.toFile("wc_plot.txt", bin="x")

p.parse("wb.txt")
p.toFile("wb_plot.txt", bin="x")

__date__ = "$Jan 14, 2011 3:35:33 PM$"


