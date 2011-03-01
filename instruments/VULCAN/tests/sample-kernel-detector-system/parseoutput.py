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
p.distToFile("%s/tt_plot.txt" % RESULT, 0, 0)

p.parse("%s/tc.txt" % RESULT)
p.distToFile("%s/tc_plot.txt" % RESULT, 0, 0)

p.parse("%s/tb.txt" % RESULT)
p.distToFile("%s/tb_plot.txt" % RESULT, 0, 0)

p.parse("%s/wt.txt" % RESULT)
p.distToFile("%s/wt_plot.txt" % RESULT, 0, 0)

p.parse("%s/wc.txt" % RESULT)
p.distToFile("%s/wc_plot.txt" % RESULT, 0, 0)

p.parse("%s/wb.txt" % RESULT)
p.distToFile("%s/wb_plot.txt" % RESULT, 0, 0)

__date__ = "$Jan 14, 2011 3:35:33 PM$"


