#!/usr/bin/env python

"""
HYSPEC simulation from moderator to sample position.

The configurations are in .../etc/hyspec_moderator2sample/
"""

"""
import warnings
warnings.simplefilter('ignore')
import mcvine
warnings.simplefilter('default')
"""

def buildApp():
    from mcvine.applications.InstrumentBuilder import build
    components = ['arm1', 'source_00', 'Mon0_toF', 'Mon0_total', 'G1A_guide', 'G1B_guide', 'G1C_guide', 'T0_T1A_guide', 'T1A_chopper', 'G2_curved_guide', 'G3_guide', 'Shutter2_guide', 'Shutter2_valve_guide', 'Valve_mon1_guide', 'Mon1_toF', 'Mon1_total', 'Mon1_t1b_guide', 'T1B_chopper', 'T1B_T2_guide', 'T2_Fermi', 'T2_MON2_guide', 'Mon2_toF', 'Mon2_total', 'G4_guide', 'arm2', 'monochromator', 'Exit_tube', 'Mon3_ToF', 'Mon3_total', 'Aperture1', 'Soeller20', 'Aperture2', 'sample_10x10', 'sample_1x1', 'recorder']
    App = build(components)
    return App

App = buildApp()
name = 'hyspec_moderator2sample'


if __name__ == '__main__': App(name).run()

# This application was modified from a script created by the following command:
# $ mcvine-create-instrument-simulation-application -name=hyspec_moderator2sample -components=arm1,source_00,Mon0_toF,Mon0_total,G1A_guide,G1B_guide,G1C_guide,T0_T1A_guide,T1A_chopper,G2_curved_guide,G3_guide,Shutter2_guide,Shutter2_valve_guide,Valve_mon1_guide,Mon1_toF,Mon1_total,Mon1_t1b_guide,T1B_chopper,T1B_T2_guide,T2_Fermi,T2_MON2_guide,Mon2_toF,Mon2_total,G4_guide,arm2,monochromator,Exit_tube,Mon3_ToF,Mon3_total,Aperture1,Soeller20,Aperture2,sample_10x10,sample_1x1,recorder

