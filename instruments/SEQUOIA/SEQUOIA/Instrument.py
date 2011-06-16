#!/usr/bin/env python


from mcvine.applications.InstrumentBuilder import build
components = [
    'arm1', 'mod', 'core_ves', 'shutter_guide', 'guide1', 'guide2', 'guide3', 'guide4', 'guide5', 'guide6', 'guide7', 'guide8', 'guide9', 'guide10', 'guide11', 't0_chopp', 
    'guide13', 'guide14', 'guide15', 'guide16', 'guide17', 'guide18', 'guide19', 'guide20', 'guide21', 'guide22', 'guide23', 'guide24', 'guide25', 'guide26', 'guide27', 'fermi_chopp', 'adjustable_slits', 'Monitor1', 'guide29', 'guide31', 'guide32', 'guide34', 'E_det', 'recorder', 't_mon2']
Instrument = build(components)
