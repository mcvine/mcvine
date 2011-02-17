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

RESULT = "results/ssd4_1"

p.parse("%s/tt.txt" % RESULT)
p.toFile("%s/tt_plot.txt" % RESULT, bin="x")

p.parse("%s/tc.txt" % RESULT)
p.toFile("%s/tc_plot.txt" % RESULT, bin="x")

p.parse("%s/tb.txt" % RESULT)
p.toFile("%s/tb_plot.txt" % RESULT, bin="x")

p.parse("%s/wt.txt" % RESULT)
p.toFile("%s/wt_plot.txt" % RESULT, bin="x")

p.parse("%s/wc.txt" % RESULT)
p.toFile("%s/wc_plot.txt" % RESULT, bin="x")

p.parse("%s/wb.txt" % RESULT)
p.toFile("%s/wb_plot.txt" % RESULT, bin="x")

__date__ = "$Jan 14, 2011 3:35:33 PM$"


