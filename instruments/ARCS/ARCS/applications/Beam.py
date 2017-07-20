#!/usr/bin/env python

cmd_help = """
Simulate ARCS beam.

It is a wrapper of arcs-m2s and a postprocessing step to
compute monitor spectra and others.

Example:

 $ arcs_beam --fermi_chopper=700-1.5-SMI --fermi_nu=600 --T0_nu=60 --E=600 --ncount=1e8

For more details of cmd line parameters, run:

 $ arcs_beam --help-properties

Impl notes:
* The postprocessing happens in mcvine.instruments.ARCS.beam_postprocessing.
"""

import os, time
from mcvine.instruments.ARCS import beam_postprocessing as bpp


from pyre.applications.Script import Script as base
class App(base):

    class Inventory(base.Inventory):

        import pyre.inventory

        fermi_chopper = pyre.inventory.str(
            'fermi_chopper', default='100-1.5-SMI')
        fermi_chopper.meta['tip'] = 'The choice of fermi chopper'
        fermi_chopper.validator = pyre.inventory.choice(
            ['100-1.5-SMI', '700-1.5-SMI', '700-0.5-AST']
            )
        
        fermi_nu = pyre.inventory.float('fermi_nu', default=600)
        fermi_nu.meta['tip'] = 'Spinning frequency of fermi chopper'
        
        T0_nu = pyre.inventory.float('T0_nu', default=60)
        T0_nu.meta['tip'] = 'Spinning frequency of T0 chopper'
        
        E = pyre.inventory.float('E', default=70)
        E.meta['tip'] = 'desired incident beam energy. unit: meV'

        emission_time = pyre.inventory.float('emission_time', default=-1)
        emission_time.meta['tip'] = 'emission time for moderator unit (microsecond)'

        with_moderator_angling = pyre.inventory.bool('with_moderator_angling', default=True)
        with_moderator_angling.meta['tip'] = "turn on/of moderator angling"

        ncount = pyre.inventory.float('ncount', default=1000000)

        nodes = pyre.inventory.int('nodes', default=0)


    m2sout = '_m2sout'
    out = 'out'


    def help(self):
        print cmd_help
    

    def main(self):
        if not os.path.exists(self.out):
            os.makedirs(self.out)
        
        self._writeREADME()
        # create configuration for arcs moderator to sample simulation
        self._run_arcs_m2s()
        # run the simulation from mod to sample
        self._run_beam()
        # postprocessing
        bpp.run(self.m2sout, self.out, self.inventory.E)
        return


    def _writeREADME(self):
        stream = open("README.arcs_beam", 'wt')
        stream.write(rundir_readme_txt)
        return


    def _run_arcs_m2s(self):
        cmd = ['mcvine instruments arcs m2s']
        keys = [
            'fermi_chopper',
            'fermi_nu',
            'T0_nu',
            'E',
            'emission_time',
            'with_moderator_angling',
            ]
        cmd += self._buildCmdFromInventory(keys)
        cmd += ['--- -dump-pml=yes', '-h'] # , '>arcs-m2s.log']
        cmd = ' '.join(cmd)
        print 'Generating pml for arcs beam instrument...'
        bpp._exec(cmd)
        print 'done.'
        time.sleep(1)
        return


    def _run_beam(self):
        cmd = ['mcvine instruments arcs mod2sample']
        keys = ['ncount']
        cmd += self._buildCmdFromInventory(keys)
        cmd += ['--buffer_size=%s' % int(self.inventory.ncount/10)]
        cmd.append( '--output-dir=%s' % self.m2sout)
        from mcvine import resources
        moddat = os.path.join(
            resources.instrument('ARCS'), 'moderator',
            'source_sct521_bu_17_1.dat',
            )
        cmd += ['--moderator.S_filename=%s' % moddat]
        # mpi nodes
        from mcni.pyre_support.MpiApplication import mpi_launcher_choice
        if self.inventory.nodes:
            cmd += ['--%s.nodes=%s' % (
                mpi_launcher_choice, self.inventory.nodes)]
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
        return ['--%s=%s' % (k,v) for k,v in kwds.iteritems()]
    
    
rundir_readme_txt = """
arcs_beam: perform ARCS beam simulation and save various data files

Steps:
* configure moderator2sample simulation using cmd line inputs
* run moderator2sample simulation
* sanitize the outputs and save them

Dirs and files:
* out: sanitized output including neutron packets, monitor data histograms etc
* arcs_moderator2sample.pml: configuration file for moderator2sample sim
* run-m2s.sh: script that runs the moderator2sample sim
* _m2sout: "raw" output from the moderator2sample sim
"""


name = 'arcs_beam'
if __name__ == '__main__': App(name).run()
