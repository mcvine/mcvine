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

# Sets name relations between McStas component and VNF neutron component
#   Names that coincide are not included in this dictionary
# Example: "SNS_source4" -> "./vnfb/vnfb/dom/neutron_experiment_simulations/neutron_components/SNSModerator"
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
# Slit          # not exist
# Guide         # not exist
# DiskChopper   # not exist
# Monitor

__date__ = "$Oct 1, 2010 6:23:27 PM$"


