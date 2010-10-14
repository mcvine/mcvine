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
COMPVAR     = "component"
PARAMS_DICT      = {
    "xmin":     "%s.x_min" % COMPVAR,
    "xmax":     "%s.x_max" % COMPVAR,
    "ymin":     "%s.y_min" % COMPVAR,
    "ymax":     "%s.y_max" % COMPVAR,
    "filename": "outputfilename(%s)" % COMPVAR
}

# VULCAN parameters
frequency   = 60.0
vlambda     = 1.5
mode        = "hint"
out_format  = "table"
PI          = 3.14159265

# INITIALIZE section
dc_tphase = 6.529/3960*vlambda  # 0.002473
dc_omega  = 2*PI*frequency      # 377.0

if mode == "hint":
    tg_w11= 0.016473;  tg_h11= 0.068046;  tg_alpha1= 2.800;
    tg_w12= 0.016476;  tg_h12= 0.065935;  tg_alpha2= 3.479;
    tg_w13= 0.016475;  tg_h13= 0.063581;  tg_alpha3= 2.800;
    tg_w14= 0.016476;  tg_h14= 0.060960;  tg_alpha4= 2.800;
    tg_w15= 0.016374;  tg_h15= 0.058013;  tg_alpha5= 4.191;
    tg_w16= 0.016207;  tg_h16= 0.054874;  tg_alpha6= 4.191;
    tg_w17= 0.015969;  tg_h17= 0.051553;  tg_alpha7= 3.479;
    tg_w18= 0.015659;  tg_h18= 0.048142;  tg_alpha8= 4.191;
    tg_w19= 0.015292;  tg_h19= 0.044808;  tg_alpha9= 3.479;

    tg_w21= 0.016473;  tg_h21= 0.065939;  tg_m_top1= 3.72;  tg_m_sid1= 3.12;
    tg_w22= 0.016477;  tg_h22= 0.063596;  tg_m_top2= 3.72;  tg_m_sid2= 3.10;
    tg_w23= 0.016475;  tg_h23= 0.060965;  tg_m_top3= 3.72;  tg_m_sid3= 3.12;
    tg_w24= 0.016379;  tg_h24= 0.058027;  tg_m_top4= 3.72;  tg_m_sid4= 3.12;
    tg_w25= 0.016210;  tg_h25= 0.054878;  tg_m_top5= 3.62;  tg_m_sid5= 3.07;
    tg_w26= 0.015967;  tg_h26= 0.051556;  tg_m_top6= 3.62;  tg_m_sid6= 3.07;
    tg_w27= 0.015650;  tg_h27= 0.048150;  tg_m_top7= 3.62;  tg_m_sid7= 3.10;
    tg_w28= 0.015298;  tg_h28= 0.044809;  tg_m_top8= 3.62;  tg_m_sid8= 3.07;
    tg_w29= 0.014924;  tg_h29= 0.041770;  tg_m_top9= 3.62;  tg_m_sid9= 3.10;

elif mode == "hres":
    tg_w11= 0.009599;  tg_h11= 0.068051;  tg_alpha1= 3.525;
    tg_w12= 0.009604;  tg_h12= 0.065934;  tg_alpha2= 3.525;
    tg_w13= 0.009602;  tg_h13= 0.063580;  tg_alpha3= 3.525;
    tg_w14= 0.009601;  tg_h14= 0.060955;  tg_alpha4= 3.525;
    tg_w15= 0.009603;  tg_h15= 0.058015;  tg_alpha5= 3.311;
    tg_w16= 0.009605;  tg_h16= 0.054878;  tg_alpha6= 3.311;
    tg_w17= 0.009607;  tg_h17= 0.051544;  tg_alpha7= 3.311;
    tg_w18= 0.009607;  tg_h18= 0.048136;  tg_alpha8= 3.311;
    tg_w19= 0.009603;  tg_h19= 0.044793;  tg_alpha9= 3.311;

    tg_w21= 0.009595;  tg_h21= 0.065944;  tg_m_top1= 3.72;  tg_m_sid1= 0.0;
    tg_w22= 0.009603;  tg_h22= 0.063585;  tg_m_top2= 3.72;  tg_m_sid2= 0.0;
    tg_w23= 0.009601;  tg_h23= 0.060956;  tg_m_top3= 3.72;  tg_m_sid3= 0.0;
    tg_w24= 0.009602;  tg_h24= 0.058024;  tg_m_top4= 3.72;  tg_m_sid4= 0.0;
    tg_w25= 0.009597;  tg_h25= 0.054874;  tg_m_top5= 3.62;  tg_m_sid5= 0.0;
    tg_w26= 0.009605;  tg_h26= 0.051568;  tg_m_top6= 3.62;  tg_m_sid6= 0.0;
    tg_w27= 0.009606;  tg_h27= 0.048147;  tg_m_top7= 3.62;  tg_m_sid7= 0.0;
    tg_w28= 0.009605;  tg_h28= 0.044813;  tg_m_top8= 3.62;  tg_m_sid8= 0.0;
    tg_w29= 0.009606;  tg_h29= 0.041756;  tg_m_top9= 3.62;  tg_m_sid9= 0.0;

__date__ = "$Oct 1, 2010 6:23:27 PM$"


