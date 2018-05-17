import mcvine, mcvine.components as mcomps
instrument = mcvine.instrument()

mod = mcomps.sources.SNS_source(name='mod', yh=0.12, dist=2.5, Emin=Emin, Emax=Emax, height=0.12, width=0.1, S_filename="source_sct521_bu_17_1.dat", xw=0.1)
instrument.append(mod, position=(0.0, 0.0, 0.0), orientation=(0, 0, 0))

core_ves = mcomps.optics.Guide_channeled(name='core_ves', Qcx=Gu_Qc, R0=0.0, W=Gu_W, alphay=Gu_alpha, h2=0.102362, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.11323, l=1.2444, w2=0.084684, w1=0.094285, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(core_ves, position=(0.0, 0.0, 1.0106), orientation=(0, 0, 0), relativeTo=mod)

shutter_guide = mcomps.optics.Guide_channeled(name='shutter_guide', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.086880, alphax=Gu_alpha, Qcy=Gu_Qc, h1=.094040, l=1.853, w2=0.070880, w1=0.074930, k=1, my=2.5, mx=2.5, d=0.0)
instrument.append(shutter_guide, position=(0.0, 0.0, 2.2679), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_1_1 = mcomps.optics.Guide_channeled(name='Guide_1_1_1', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.08573, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.08688, l=0.48354, w2=0.07019, w1=0.07088, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_1_1, position=(0.0, 0.0, 4.1723), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_1_2 = mcomps.optics.Guide_channeled(name='Guide_1_1_2', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.08454, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.08573, l=0.48354, w2=0.06947, w1=0.07019, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_1_2, position=(0.0, 0.0, 4.65589), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_1_3 = mcomps.optics.Guide_channeled(name='Guide_1_1_3', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.08329, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.08454, l=0.48354, w2=0.06871, w1=0.06947, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_1_3, position=(0.0, 0.0, 5.13948), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_2_1 = mcomps.optics.Guide_channeled(name='Guide_1_2_1', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.08197, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.08329, l=0.48354, w2=0.06792, w1=0.06871, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_2_1, position=(0.0, 0.0, 5.62331), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_2_2 = mcomps.optics.Guide_channeled(name='Guide_1_2_2', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.08060, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.08197, l=0.48354, w2=0.06710, w1=0.06792, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_2_2, position=(0.0, 0.0, 6.1069), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_2_3 = mcomps.optics.Guide_channeled(name='Guide_1_2_3', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.07917, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.08060, l=0.48354, w2=0.06624, w1=0.06710, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_2_3, position=(0.0, 0.0, 6.59049), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_3_1 = mcomps.optics.Guide_channeled(name='Guide_1_3_1', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.07766, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.07917, l=0.48354, w2=0.06534, w1=0.06624, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_3_1, position=(0.0, 0.0, 7.07433), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_3_2 = mcomps.optics.Guide_channeled(name='Guide_1_3_2', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.07609, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.07766, l=0.48354, w2=0.06440, w1=0.06534, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_3_2, position=(0.0, 0.0, 7.55792), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_3_3 = mcomps.optics.Guide_channeled(name='Guide_1_3_3', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.07443, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.07609, l=0.48354, w2=0.06342, w1=0.06440, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_3_3, position=(0.0, 0.0, 8.04145), orientation=(0, 0, 0), relativeTo=mod)

t0_chopp = mcomps.optics.Vertical_T0(name='t0_chopp', ymax=0.045, len=0.474, tc=phase_T0, w2=0.101, w1=0.08, delta=0.0, ymin=-0.045, nu=T0_nu)
instrument.append(t0_chopp, position=(0.0, 0.0, 'LT0'), orientation=(0, 0, 0), relativeTo=mod)

Guide_2_1_1 = mcomps.optics.Guide_channeled(name='Guide_2_1_1', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.06936, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.07094, l=0.40204, w2=0.06044, w1=0.06136, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_2_1_1, position=(0.0, 0.0, 9.47504), orientation=(0, 0, 0), relativeTo=mod)

Guide_2_1_2 = mcomps.optics.Guide_channeled(name='Guide_2_1_2', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.06771, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.06936, l=0.40204, w2=0.05948, w1=0.06044, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_2_1_2, position=(0.0, 0.0, 9.87713), orientation=(0, 0, 0), relativeTo=mod)

Guide_2_3_3 = mcomps.optics.Guide_channeled(name='Guide_2_3_3', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.06598, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.06771, l=0.40204, w2=0.05848, w1=0.05948, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_2_3_3, position=(0.0, 0.0, 10.27922), orientation=(0, 0, 0), relativeTo=mod)

Guide_1_3_4 = mcomps.optics.Guide_channeled(name='Guide_1_3_4', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.06417, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.06598, l=0.40204, w2=0.05745, w1=0.05848, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_1_3_4, position=(0.0, 0.0, 10.68131), orientation=(0, 0, 0), relativeTo=mod)

Guide_2_1_5 = mcomps.optics.Guide_channeled(name='Guide_2_1_5', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.06227, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.06417, l=0.40204, w2=0.05637, w1=0.05745, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_2_1_5, position=(0.0, 0.0, 11.0834), orientation=(0, 0, 0), relativeTo=mod)

fermi_chopp = mcomps.optics.Fermi_chop2(name='fermi_chopp', nchan=nchans, ymax=.0325, len=0.10, tc=phasefc1, bw=0.0005, w=0.06, delta=0.0, ymin=-.0325, nu=Fermi_nu, blader=nrad)
instrument.append(fermi_chopp, position=(0.0, 0.0, 'LF'), orientation=(0, 0, 0), relativeTo=mod)

Monitor1 = mcomps.monitors.TOF_monitor2(name='Monitor1', nchan=100, tmin=tplotmin, ymax=0.035, tmax=tplotmax, filename=mon1optstr, xmax=0.035, xmin=-0.035, ymin=-0.035)
instrument.append(Monitor1, position=(0.0, 0.0, 'LM1'), orientation=(0, 0, 0), relativeTo=mod)

Guide_3_1_1 = mcomps.optics.Guide_channeled(name='Guide_3_1_1', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.05931, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.06046, l=0.225, w2=0.05473, w1=0.05536, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_3_1_1, position=(0.0, 0.0, 11.84975), orientation=(0, 0, 0), relativeTo=mod)

Guide_4_1_1 = mcomps.optics.Guide_channeled(name='Guide_4_1_1', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.05674, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.05924, l=0.46275, w2=0.05331, w1=0.05468, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_4_1_1, position=(0.0, 0.0, 12.08825), orientation=(0, 0, 0), relativeTo=mod)

Guide_4_1_2 = mcomps.optics.Guide_channeled(name='Guide_4_1_2', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.05408, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.05674, l=0.46275, w2=0.05187, w1=0.05331, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_4_1_2, position=(0.0, 0.0, 12.55105), orientation=(0, 0, 0), relativeTo=mod)

Guide_5_1_1 = mcomps.optics.Guide_channeled(name='Guide_5_1_1', Qcx=Gu_Qc, R0=Gu_R, W=Gu_W, alphay=Gu_alpha, h2=0.05172, alphax=Gu_alpha, Qcy=Gu_Qc, h1=0.05405, l=0.37920, w2=0.05062, w1=0.05186, k=1, my=Gu_m, mx=Gu_m, d=0.0)
instrument.append(Guide_5_1_1, position=(0.0, 0.0, 13.0183), orientation=(0, 0, 0), relativeTo=mod)

E_det = mcomps.monitors.E_monitor(name='E_det', nchan=100, ymax=.025, Emin=Emin, Emax=Emax, filename=detoptstr, xmax=.025, xmin=-.025, ymin=-.025)
instrument.append(E_det, position=(0.0, 0.0, 'LS-.001'), orientation=(0, 0, 0), relativeTo=mod)
