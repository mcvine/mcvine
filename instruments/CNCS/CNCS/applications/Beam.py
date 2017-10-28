#!/usr/bin/env python

cmd_help = """
Simulate CNCS beam and analyze the beam.

Example:

 $ cncs_beam --E=5 --f1=60. --f2=60. --f3=60. --f41=300. --f42=300. --fluxmode=9.0 --ncount=1e8 --nodes=10

Notes:

    Incident energy: Ei (meV)

    Frequency Fermi Chopper 1: (Hz)     typically 60 Hz
    Frequency Disk Chopper 2: (Hz)      typically 60 Hz
    Frequency Disk Chopper 3: (Hz)      typically 60 Hz

    fluxmode:
      High Flux (HF)    = 9.0 deg
      Intermidiste (AI) = 4.4 deg
      High Res (HR)     = 2.0 deg

    Frequency DoubleDisk Chopper 1: (Hz)         300 Hz for HF       240 Hz for AI        180 Hz for HR
    Frequency DoubleDisk Chopper 2: (Hz)         300 Hz for HF       240 Hz for AI        180 Hz for HR


For more details of cmd line parameters, run:

 $ cncs_beam --help-properties

"""

import os, time
from mcvine.instruments.CNCS import beam_postprocessing as bpp


from pyre.applications.Script import Script as base
class App(base):

    class Inventory(base.Inventory):

        import pyre.inventory

        E = pyre.inventory.float('E', default=20)
        E.meta['tip'] = 'desired incident beam energy. unit: meV'
        
        f1 = pyre.inventory.float('f1', default=60)
        f1.meta['tip'] = 'Chopper freq 1. unit: Hz'
        
        f2 = pyre.inventory.float('f2', default=60)
        f2.meta['tip'] = 'Chopper freq 2. unit: Hz'
        
        f3 = pyre.inventory.float('f3', default=60)
        f3.meta['tip'] = 'Chopper freq 3. unit: Hz'
        
        f41 = pyre.inventory.float('f41', default=300)
        f41.meta['tip'] = 'Chopper freq 41. unit: Hz'
        
        f42 = pyre.inventory.float('f42', default=300)
        f42.meta['tip'] = 'Chopper freq 42. unit: Hz'
        
        fluxmode = pyre.inventory.float('fluxmode', default=9.)
        fluxmode.meta['tip'] = 'flux mode'
        
        ncount = pyre.inventory.float('ncount', default=1000000)
        ncount.meta['tip'] = 'neutron count'
        
        nodes = pyre.inventory.int('nodes', default=1)
        nodes.meta['tip'] = '# of mpi nodes'
        
        
    m2sout = '_m2sout'
    out = 'out'
    
    
    def help(self):
        print cmd_help
    

    def main(self):
        if not os.path.exists(self.out):
            os.makedirs(self.out)
            
        # create configuration for cncs moderator to sample simulation
        self._configure_cncs()
        # run the simulation from mod to sample
        self._run_beam()
        # postprocessing
        bpp.run(self.m2sout, self.out, self.inventory.E)
        return


    def _configure_cncs(self):
        cmd = ['mcvine instruments cncs config_mod2sample']
        data = dict(
            Ei = self.inventory.E,
            f1 = self.inventory.f1,
            f2 = self.inventory.f2,
            f3 = self.inventory.f3,
            f41 = self.inventory.f41,
            f42 = self.inventory.f42,
            fluxmode = self.inventory.fluxmode,
            )
        cmd += self._buildCmdOptions(data)
        cmd = ' '.join(cmd)
        bpp._exec(cmd)
        print 'done.'
        time.sleep(1)
        return


    def _run_beam(self):
        from mcvine import resources as res
        moddat = os.path.join(
            res.instrument('CNCS'), 
            'mcstas', 'source_sct21a_td_05_1.dat',
            )
        cmd = ['mcvine instruments cncs mod2sample']
        from mcni.pyre_support.MpiApplication \
            import mpi_launcher_choice as launcher
        data = {
            "ncount": self.inventory.ncount,
            "buffer_size": int(self.inventory.ncount/5/self.inventory.nodes),
            ("%s.nodes" % launcher): self.inventory.nodes,
            "output-dir": self.m2sout,
            'moderator.S_filename': moddat,
            }
        cmd += self._buildCmdOptions(data)
        cmd = ' '.join(cmd)
        open('run-m2s.sh', 'wt').write(cmd) # save the running command
        bpp._exec(cmd)
        return
    
    
    def _buildCmdOptions(self, kwds):
        return ['--%s=%s' % (k,v) for k,v in kwds.iteritems()]


name = 'cncs_beam'

if __name__ == '__main__': App(name).run()
