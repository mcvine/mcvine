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
Sets name relations between McStas component and VNF neutron component

Example: "SNS_source4" -> "./vnfb/vnfb/dom/neutron_experiment_simulations/neutron_components/SNSModerator"

Notes:
    - Dom names that match McStas names are not included in this dictionary
"""

IMPORT_DICT     = {
    "SNS_source4":          "SNSModerator",
    "Collimator_linear":    "CollimatorLinear",     # not exist
    "L_monitor":            "LMonitor",    
    "Guide_gravity":        "GuideGravity",         # not exist
    "PSD_monitor":          "PSDMonitor",           # not exist
    "Monitor_nD":           "NDMonitor",            # not exist
    "V_sample":             "VanadiumPlate",
    "PSD_TEW_monitor":      "PSD_TEWMonitor"        # not exist
}

# Parameters dictionary for job builder
PARAMS_DICT      = {
    "xmin":     "m.x_min",
    "xmax":     "m.x_max",
    "ymin":     "m.y_min",
    "ymax":     "m.y_max",
    "filename": "outputfilename(m)"
}
__date__ = "$Oct 1, 2010 6:23:27 PM$"


