#!/usr/bin/env python

cmd_help = """
Simulate HYSPEC beam and analyze the beam.

Example:

 $ hyspec_beam --fermi_nu=180 --E=20 --Emin=10 --Emax=39 --LMS=1.8 --ncount=1e8 --nodes=10

For more details of cmd line parameters, run:

 $ hyspec_beam --help-properties

"""

import os, time
from mcvine.instruments.HYSPEC import beam_postprocessing as bpp


from pyre.applications.Script import Script as base
class App(base):

    class Inventory(base.Inventory):

        import pyre.inventory

        fermi_nu = pyre.inventory.float('fermi_nu', default=180)
        fermi_nu.meta['tip'] = 'Spinning frequency of fermi chopper'
        
        E = pyre.inventory.float('E', default=20)
        E.meta['tip'] = 'desired incident beam energy. unit: meV'
        
        Emin = pyre.inventory.float('Emin', default=10)
        Emin.meta['tip'] = 'minimum incident energy. unit: meV'
        
        Emax = pyre.inventory.float('Emax', default=30)
        Emax.meta['tip'] = 'maximum incident energy. unit: meV'
        
        LMS = pyre.inventory.float('LMS', default=1.8)
        LMS.meta['tip'] = 'monochromator to sample distance. unit: meter'
        
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
            
        # create configuration for hyspec moderator to sample simulation
        self._configure_hyspec()
        # run the simulation from mod to sample
        self._run_beam()
        # postprocessing
        bpp.run(self.m2sout, self.out, self.inventory.E, self.inventory.LMS)
        return


    def _configure_hyspec(self):
        cmd = ['mcvine instruments hyspec config_mod2sample']
        data = dict(
            Edes = self.inventory.E,
            E_min = self.inventory.Emin,
            E_max = self.inventory.Emax,
            freq = self.inventory.fermi_nu,
            LMS = self.inventory.LMS,
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
            res.instrument('HYSPEC'), 
            'mcstas', 'SNS_TD_30o70p_fit_fit.dat',
            )
        cmd = ['mcvine instruments hyspec mod2sample']
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


name = 'hyspec_beam'

if __name__ == '__main__': App(name).run()
