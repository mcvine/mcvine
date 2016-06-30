#!/usr/bin/env python

cmd_help = """
Simulate SEQUOIA beam.

It is a wrapper of sequoia-m2s and convenient tools to 
compute monitor spectra and others.

Example:

 $ sequoia_beam --fermi_chopper=100-2.03-AST --fermi_nu=600 --T0_nu=60 --E=600 --ncount=1e8

For more details of cmd line parameters, run:

 $ sequoia_beam --help-properties

Impl notes:
* The postprocessing happens in mcvine.instruments.SEQUOIA.beam_postprocessing.
"""

# distance from moderator to monitor1, unit meter
# this should match the monitor 1 position in sequoia-moderator2sample
# application.
LM1 = 18.26
# distance from moderator to monitor2
LM2 = 29.0032
# distance to sample
LSAMPLE = 20.0254


import os, time
from mcvine.instruments.SEQUOIA import beam_postprocessing as bpp


from pyre.applications.Script import Script as base
class App(base):

    class Inventory(base.Inventory):

        import pyre.inventory

        fermi_chopper = pyre.inventory.str(
            'fermi_chopper', default='100-2.03-AST')
        fermi_chopper.meta['tip'] = 'The choice of fermi chopper'
        fermi_chopper.validator = pyre.inventory.choice(
            ['100-2.03-AST', '700-3.56-AST',
             '700-0.5-AST', # from ARCS
             ]
            )
        
        fermi_nu = pyre.inventory.float('fermi_nu', default=600)
        fermi_nu.meta['tip'] = 'Spinning frequency of fermi chopper'
        
        T0_nu = pyre.inventory.float('T0_nu', default=60)
        T0_nu.meta['tip'] = 'Spinning frequency of T0 chopper'
        
        E = pyre.inventory.float('E', default=70)
        E.meta['tip'] = 'desired incident beam energy. unit: meV'

        emission_time = pyre.inventory.float('emission_time', default=-1)
        emission_time.meta['tip'] = 'emission time for moderator unit (microsecond)'

        ncount = pyre.inventory.float('ncount', default=1000000)


    m2sout = '_m2sout'
    out = 'out'


    def help(self):
        print cmd_help
    

    def main(self):
        if not os.path.exists(self.out):
            os.makedirs(self.out)

        self._writeREADME()
        # create configuration for sequoia moderator to sample simulation
        self._run_sequoia_m2s()
        # run the simulation from mod to sample
        self._run_beam()
        # postprocessing
        bpp.run(self.m2sout, self.out, self.inventory.E)
        return


    def _writeREADME(self):
        stream = open("README.sequoia_beam", 'wt')
        stream.write(rundir_readme_txt)
        return


    def _run_sequoia_m2s(self):
        cmd = ['mcvine instruments sequoia m2s']
        keys = [
            'fermi_chopper',
            'fermi_nu',
            'T0_nu',
            'E',
            'emission_time',
            ]
        cmd += self._buildCmdFromInventory(keys)
        cmd += ['--- -dump-pml=yes', '-h'] # , '>sequoia-m2s.log']
        cmd = ' '.join(cmd)
        print 'Generating pml for sequoia beam instrument...'
        bpp._exec(cmd)
        print 'done.'
        time.sleep(1)
        return


    def _run_beam(self):
        cmd = ['mcvine instruments sequoia mod2sample']
        keys = ['ncount']
        cmd += self._buildCmdFromInventory(keys)
        cmd += ['-buffer_size=%s' % int(self.inventory.ncount/10)]
        cmd.append( '--output-dir=%s' % self.m2sout)
        from mcvine import resources as res
        moddat = os.path.join(
            res.instrument('SEQUOIA'), 'moderator',
            'source_sct521_bu_17_1.dat',
            )
        cmd += ['-mod.S_filename=%s' % moddat]
        cmd = ' '.join(cmd)
        open('run-m2s.sh', 'wt').write(cmd) # save the running command
        bpp._exec(cmd)
        return


    def _buildCmdFromInventory(self, keys):
        kwds = {}
        for k in keys:
            v = getattr(self.inventory, k)
            kwds[k] = v
            continue
        return ['-%s=%s' % (k,v) for k,v in kwds.iteritems()]
    
    
rundir_readme_txt = """
sequoia_beam: perform SEQUOIA beam simulation and save various data files

Steps:
* configure moderator2sample simulation using cmd line inputs
* run moderator2sample simulation
* sanitize the outputs and save them

Dirs and files:
* out: sanitized output including neutron packets, monitor data histograms etc
* sequoia_moderator2sample.pml: configuration file for moderator2sample sim
* run-m2s.sh: script that runs the moderator2sample sim
* _m2sout: "raw" output from the moderator2sample sim
"""


name = 'sequoia_beam'

if __name__ == '__main__': App(name).run()
