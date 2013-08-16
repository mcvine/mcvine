#!/usr/bin/env python


from mcvine.applications.InstrumentBuilder import build
components = [
    'moderator', 
    'mon0_tof', 'mon0_total',
    # ------- The guide in the shutter (G1A) & biological shield (G1B, G1C) -----
    'g1a_guide',
    # ------- The guide in the biological shield & chopper cave (G1B, G1C) ------
    'g1b_guide', 'g1c_guide',
    # ---------------------------- Chopper Box A --------------------------------
    't0_t1a_guide', 't1a_chopper',
    # -------------- The curved guide G2 connecting Box-A and G3-----------------
    'g2_curved_guide',
    # ----------- The components between the curved guide and box B -------------
    'g3_guide', 'shutter2_guide', 'shutter2_valve_guide', 
    'valve_mon1_guide', 'mon1_tof', 'mon1_total', 'mon1_t1b_guide',
    # -------------------------------- Chopper box B ----------------------------
    't1b_chopper', 't1b_t2_guide', 't2_fermi',
    't2_mon2_guide', 'mon2_tof', 'mon2_total',
    # -------------------------- Straight guide G4 after box B ------------------
    'g4_guide',
    # ------------------- Focusing monochromator crystals -----------------------
    'arm2', # rotated
    'monochromator', # rotated
    # ------------------- Exit beam tube on the drum shield ---------------------
    'exit_tube',
    # ------------------- Optical Rail pre-sample -------------------------------
    'mon3_tof', 'mon3_total',
    'aperture1', 'soeller40', 'soeller20', 'aperture2',
    # -------------- At Sample position, actual sample --------------------------
    'recorder',
    ]
Instrument = build(components)
