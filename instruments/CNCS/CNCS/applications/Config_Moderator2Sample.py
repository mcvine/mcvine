#!/usr/bin/env python

cmd_help = """
<cmd> --Ei=5 --f1=60. --f2=60. --f3=60. --f41=300. --f42=300. --fluxmode=9.0
"""

# CNCS_Dec_2016_py

class arm1(object):
  name='arm1'
  parameters={}
  extra='\nAT (0,0,0) ABSOLUTE\n\n\n\n\n\n'
  position=((0.0, 0.0, 0.0), 'absolute', None)
  type='Progress_bar'
  orientation=((0, 0, 0), 'absolute', None)

class moderator(object):
  name='moderator'
  parameters={'yh': '0.14', 'dist': '1.000', 'Emin': 'emin', 'Emax': 'emax', 'height': '0.12', 'width': '0.1', 'S_filename': '"source_sct21a_td_05_1.dat"', 'xw': '0.06'}
  extra='\nAT (0,0,0) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
  position=((0.0, 0.0, 0.0), 'relative', 'arm1')
  type='SNS_source'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class Guide1(object):
  name='Guide1'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.1', 'h1': '0.1', 'm': '2.5', 'l': '5.280', 'Qc': 'Gu_Qc', 'w2': '0.05', 'w1': '0.05', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,1.002) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
  position=((0.0, 0.0, 1.002), 'relative', 'arm1')
  type='Guide'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class FChopper(object):
  name='FChopper'
  parameters={'Nslit': '9', 'zero_time': '0', 'height': '0.102', 'width': '0.053', 'length': '0.017', 'time': 'f1_tof', 'nu': 'f1'}
  extra='\nAT (0,0,6.413) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n\n\n\n'
  position=((0.0, 0.0, 6.413), 'relative', 'arm1')
  type='FermiChopper'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class tof1b(object):
  name='tof1b'
  parameters={'nchan': '500', 'ymax': '.05', 'filename': '"tof1b.det"', 't0': '6000', 't1': '8000', 'xmax': '.025', 'xmin': '-.025', 'ymin': '-.05'}
  extra='\n\t\t\t    \nAt (0,0,6.555) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n'
  position=((0.0, 0.0, 6.555), 'relative', 'arm1')
  type='TOF_monitor'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class Guide4(object):
  name='Guide4'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.1', 'h1': '0.1', 'm': '2.5', 'l': '0.925', 'Qc': 'Gu_Qc', 'w2': '0.05', 'w1': '0.05', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,6.560) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n'
  position=((0.0, 0.0, 6.56), 'relative', 'arm1')
  type='Guide'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class Chopper2(object):
  name='Chopper2'
  parameters={'yheight': '0', 'nslit': '1', 'radius': '0.25', 'theta_0': '14.0', 'delay': 'f2_tof', 'nu': 'f2'}
  extra='\nAT (0,0,7.515) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n\n\n\n\n\n'
  position=((0.0, 0.0, 7.515), 'relative', 'arm1')
  type='DiskChopper_v2'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class Guide5(object):
  name='Guide5'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.1', 'h1': '0.1', 'm': '2.5', 'l': '0.965', 'Qc': 'Gu_Qc', 'w2': '0.05', 'w1': '0.05', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,7.572) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n\n\n'
  position=((0.0, 0.0, 7.572), 'relative', 'arm1')
  type='Guide'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class Guide6(object):
  name='Guide6'
  parameters={'Qcs': 'Gu_Qc', 'alphas': 'Gu_alpha', 'R0s': 'Gu_R', 'ma': '2.5', 'd': '0.001', 'Wa': 'Gu_W', 'h': '0.10', 'k': '1', 'mi': '3.5', 'l': '14.98', 'Wi': 'Gu_W', 'R0a': 'Gu_R', 'Qca': 'Gu_Qc', 'r': '2000.0', 'Ws': 'Gu_W', 'w': '0.05', 'alphaa': 'Gu_alpha', 'R0i': 'Gu_R', 'Qci': 'Gu_Qc', 'alphai': 'Gu_alpha', 'ms': '2.5'}
  extra='\nAT (0,0,8.543) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n\n'
  position=((0.0, 0.0, 8.543), 'relative', 'arm1')
  type='Bender'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

class Guide7(object):
  name='Guide7'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.1', 'h1': '0.1', 'm': '3.0', 'l': '7.0', 'Qc': 'Gu_Qc', 'w2': '0.05', 'w1': '0.05', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,23.544) RELATIVE arm1 \n\n\n'
  position=((0.0, 0.0, 23.544), 'relative', 'arm1')
  type='Guide'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Guide8(object):
  name='Guide8'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.0765', 'h1': '0.1', 'm': '3.5', 'l': '2.447', 'Qc': 'Gu_Qc', 'w2': '0.035', 'w1': '0.05', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,30.545) RELATIVE arm1 \n\n\n'
  position=((0.0, 0.0, 30.545), 'relative', 'arm1')
  type='Guide'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Chopper3(object):
  name='Chopper3'
  parameters={'yheight': '0', 'nslit': '1', 'radius': '0.25', 'theta_0': '14.0', 'delay': 'f3_tof', 'nu': 'f3'}
  extra='\nAT (0,0,33.020) RELATIVE arm1\n\n\n'
  position=((0.0, 0.0, 33.02), 'relative', 'arm1')
  type='DiskChopper_v2'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Guide9(object):
  name='Guide9'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.0597', 'h1': '0.076', 'm': '3.5', 'l': '1.700', 'Qc': 'Gu_Qc', 'w2': '0.0218', 'w1': '0.0332', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,33.025) RELATIVE arm1\n\n\n\n\n\n\n\n\n\n\n\n\n \n\n\n'
  position=((0.0, 0.0, 33.025), 'relative', 'arm1')
  type='Guide'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Chopper41(object):
  name='Chopper41'
  parameters={'yheight': '0.065', 'nslit': '1', 'radius': '0.2825', 'theta_0': 'fluxmode', 'delay': 'f41_tof', 'nu': '-f41'}
  extra='\nAT (0,0,34.784) RELATIVE arm1\n'
  position=((0.0, 0.0, 34.784), 'relative', 'arm1')
  type='DiskChopper_v2'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Chopper42(object):
  name='Chopper42'
  parameters={'yheight': '0.065', 'nslit': '1', 'radius': '0.2825', 'theta_0': 'fluxmode', 'delay': 'f42_tof', 'nu': 'f42'}
  extra='\nAT (0,0,34.785) RELATIVE arm1\nGROUP guide\n\n\n\n\n\n'
  position=((0.0, 0.0, 34.785), 'relative', 'arm1')
  type='DiskChopper_v2'
  orientation=((0, 0, 0), 'relative', 'arm1')

class tof3a(object):
  name='tof3a'
  parameters={'nchan': '60', 'ymax': '.05', 'filename': '"tof3a.det"', 't0': 'mon3_tof_start', 't1': 'mon3_tof_stop', 'xmax': '.025', 'xmin': '-.025', 'ymin': '-.05'}
  extra='\n\t\t\t    \nAt (0,0,d_mod_mon3) RELATIVE arm1\n\n\n\n\n\n'
  position=((0.0, 0.0, 'd_mod_mon3'), 'relative', 'arm1')
  type='TOF_monitor'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Guide10(object):
  name='Guide10'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.0503', 'h1': '0.0587', 'm': '3.5', 'l': '0.875', 'Qc': 'Gu_Qc', 'w2': '0.0152', 'w1': '0.0211', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,34.863) RELATIVE arm1\n\n\n'
  position=((0.0, 0.0, 34.863), 'relative', 'arm1')
  type='Guide'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Guide11(object):
  name='Guide11'
  parameters={'R0': 'Gu_R', 'W': 'Gu_W', 'h2': '0.05', 'h1': '0.05', 'm': '4.0', 'l': '0.220', 'Qc': 'Gu_Qc', 'w2': '0.015', 'w1': '0.015', 'alpha': 'Gu_alpha'}
  extra='\nAT (0,0,35.762) RELATIVE arm1\n\n'
  position=((0.0, 0.0, 35.762), 'relative', 'arm1')
  type='Guide'
  orientation=((0, 0, 0), 'relative', 'arm1')

class save_neutrons(object):
  name='save_neutrons'
  parameters={'path': '"neutrons"'}
  extra='\n  AT (0, 0, 36.114) RELATIVE arm1\n\n\n\n\n\n\n\n\n\n'
  position=((0.0, 0.0, 36.114), 'relative', 'arm1')
  type='NeutronToStorage'
  orientation=((0, 0, 0), 'relative', 'arm1')

class Div_monh(object):
  name='Div_monh'
  parameters={'maxdiv': '5', 'yheight': '0.1', 'filename': '"Divh_Sample.dat"', 'npos': '500', 'xwidth': '0.1', 'ndiv': '500'}
  extra='\n    \nAT (0,0,36.264) RELATIVE arm1\nROTATED (0,0,0) RELATIVE arm1\n\n\n\n\n\n\n\n\n\n  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFINALLY\n%{\n%}\nEND\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
  position=((0.0, 0.0, 36.264), 'relative', 'arm1')
  type='DivPos_monitor'
  orientation=((0.0, 0.0, 0.0), 'relative', 'arm1')

def config(Ei=5, f1=60., f2=60., f3=60., f41=300., f42=300., fluxmode=9.0):
  
  from numpy import sqrt, pi
  twopi = 2*pi
  
  
  
  
  
  f2w = f2*twopi
  f3w = f3*twopi
  f41w = f41*twopi
  f42w = f42*twopi
  
  
  
  
  
  Gu_alpha = 5.0;
  Gu_R = 0.99;
  Gu_W = 0.002;
  Gu_Qc = 0.02;
  
  
  
  d_mod_mon1=6.313    ;
  L1=6.413            ; 
  L2=7.515            ;
  d_mod_mon2=7.556    ;     
  L3=33.020           ; 
  L4=34.784           ; 
  d_mod_mon3=34.836   ;
  d_mod_sample=36.262 ;
  d_mod_det=39.762    ;
  
  
  erange=0.20*Ei;
  emin=Ei-erange;
  emax=Ei+erange;
  
  
  
  T0=(1.0+Ei);
  T0=198.2*pow(T0,-0.84098)/1.e6;
  Toff=0.0;
  
  
  
  
  
  f1_tof=T0+(2286.3*L1)/sqrt(Ei)/1.e6;
  f1_tof_deg=360.0 *f1*f1_tof;
  
  ffict_tof=T0+(2286.3*6.350)/sqrt(Ei)/1.e6;
  
  f2_tof=T0+(2286.3*L2)/sqrt(Ei)/1.e6;
  
  f3_tof=T0+(2286.3*L3)/sqrt(Ei)/1.e6;
  
  f41_tof=T0+(2286.3*L4)/sqrt(Ei)/1.e6;
  
  f41omega=f41;
  
  f42_tof=T0+(2286.3*L4)/sqrt(Ei)/1.e6;
  
  f42omega=f42;
  
  sample_tof=T0+(2286.3*d_mod_sample)/sqrt(Ei);
  sample_tof_start=sample_tof-150;
  sample_tof_stop=sample_tof+150;
  
  mon3_tof=T0+(2286.3*d_mod_mon3)/sqrt(Ei);
  mon3_tof_start=mon3_tof-150;
  mon3_tof_stop=mon3_tof+150;
  components = [arm1, moderator, Guide1, FChopper, tof1b, Guide4, Chopper2, Guide5, Guide6, Guide7, Guide8, Chopper3, Guide9, Chopper41, Chopper42, tof3a, Guide10, Guide11, save_neutrons, Div_monh()]
  from mcvine.instrument.pml import set_instrument_parameters, PmlRenderer
  class instrument: pass
  instrument.name=u'cncs_moderator2sample'
  instrument.components=components
  set_instrument_parameters(instrument, locals())
  from mcvine.instrument.pml import PmlRenderer
  renderer = PmlRenderer()
  text = '\n'.join(renderer.render(instrument))
  pml = 'cncs_moderator2sample.pml'
  open(pml, 'wt').write(text)
  return

from pyre.applications.Script import Script as base
class App(base):
  class Inventory(base.Inventory):
    import pyre.inventory
    Ei = pyre.inventory.float("Ei", default="5")
    f1 = pyre.inventory.float("f1", default="60.")
    f2 = pyre.inventory.float("f2", default="60.")
    f3 = pyre.inventory.float("f3", default="60.")
    f41 = pyre.inventory.float("f41", default="300.")
    f42 = pyre.inventory.float("f42", default="300.")
    fluxmode = pyre.inventory.float("fluxmode", default="9.0")
    pass # Inventory
  def main(self, *args, **kwds):
    d={}
    d["Ei"] = self.inventory.Ei
    d["f1"] = self.inventory.f1
    d["f2"] = self.inventory.f2
    d["f3"] = self.inventory.f3
    d["f41"] = self.inventory.f41
    d["f42"] = self.inventory.f42
    d["fluxmode"] = self.inventory.fluxmode
    config(**d)
    return
  def help(self):
    import sys, os
    h = os.path.basename(sys.argv[0]) + "  "
    print h,
    print "--Ei=5 --f1=60. --f2=60. --f3=60. --f41=300. --f42=300. --fluxmode=9.0"

name = 'cncs_config_mod2sample'

def main(): App(name).run()
if __name__=='__main__': main()
