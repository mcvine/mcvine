#!/usr/bin/env python

cmd_help = """
This app wraps arcs_moderator2sample.
The 'arcs_moderator2sample' is a instrument simulation script 
with a list of components from moderator to sample (just before sample).
There are quite a few components and configuring it could be
troublesome.
This script is a wrapper. Its interface is simpler: there are less
than ten parameters to set. And this script computes parameters
of some components such as phase of fermi chopper based on user's
inputs here.

Use --help-properties to see the configurable options:

 $ <cmd> --help-properties

"""


from mcvine.applications.SuperAppBase import SuperAppBase as base

class App(base):

    class Inventory(base.Inventory):

        import pyre.inventory
        
        fermi_chopper = pyre.inventory.str(
            'fermi_chopper', default='100-1.5-SMI')
        fermi_chopper.meta['tip'] = 'fermi chopper choice'
        fermi_chopper.meta[base.inventory_item_signature] = True
        fermi_chopper.validator = pyre.inventory.choice(
            ['100-1.5-SMI', '700-1.5-SMI', '700-0.5-AST']
            )
        
        fermi_nu = pyre.inventory.float('fermi_nu', default=600)
        fermi_nu.meta['tip'] = 'Spinning frequency of fermi chopper'
        fermi_nu.meta[base.inventory_item_signature] = True

        fermi_bladeradius = pyre.inventory.float('fermi_bladeradius', default=-1)
        fermi_bladeradius.meta['tip'] = 'blade radius of fermi chopper'
        fermi_bladeradius.meta[base.inventory_item_signature] = True

        T0_nu = pyre.inventory.float('T0_nu', default=60)
        T0_nu.meta['tip'] = 'Spinning frequency of T0 chopper'
        T0_nu.meta[base.inventory_item_signature] = True
        
        E = pyre.inventory.float('E', default=70)
        E.meta['tip'] = 'desired incident beam energy. unit: meV'
        E.meta[base.inventory_item_signature] = True

        emission_time = pyre.inventory.float('emission_time', default=-1)
        emission_time.meta['tip'] = 'emission time for moderator unit (microsecond)'
        emission_time.meta[base.inventory_item_signature] = True

        dry_run = pyre.inventory.bool('dry_run', default=False)
        dry_run.meta[base.inventory_item_signature] = True

        pass # end of Inventory


    def help(self):
        print cmd_help
    
    
    def runApp(
        self, 
        fermi_chopper = None,
        fermi_nu=None, fermi_bladeradius=None, 
        T0_nu=None, E=None, emission_time=None,
        dry_run = False,
        ):
        
        #
        Emin = E*0.8
        Emax = E*1.2
        
        #
        # emission_time = self.inventory.emission_time
        if emission_time < 0: emission_time = None
        else:emission_time *= 1.e-6
        from mcvine.instruments.ARCS import t0chopper, fermichopper
        t0phase = t0chopper.phase(E, 8.77, emission_time=emission_time)
        fermiphase = fermichopper.phase(E, 11.61, emission_time=emission_time)

        # set the fermi chopper component
        # see ../etc/arcs_moderator2sample
        fermichopper_name = 'fermichopper-%s' % fermi_chopper

        # 
        opts = {
            # fermi chopper
            'fermichopper': fermichopper_name,
            'fermichopper.nu': fermi_nu,
            'fermichopper.tc': fermiphase,
            # T0
            't0chopper.nu': T0_nu,
            't0chopper.tc': t0phase,
            # moderator
            'moderator.Emin': Emin,
            'moderator.Emax': Emax,
            }
        
        # this is only for advanced users: fermi chopper blade radius
        if fermi_bladeradius>0:
            opts['fermichopper.blader'] = fermi_bladeradius
            
        import sys
        addOptions(opts, sys.argv)

        if dry_run:
            print sys.argv
        
        else:
            from mcvine.instruments.ARCS.Instrument import Instrument
            instrument = Instrument('arcs_moderator2sample')
            instrument.run()
        
        return



def addOptions(opts, argv):
    for k, v in opts.iteritems():
        if hasOpt(k, argv): continue
        argv.append('-%s=%s' % (k,v))
        continue
    return argv


def hasOpt(key, argv):
    for arg in argv:
        if arg.startswith('-%s=' % key) \
                or arg.startswith('--%s=' % key):
            return True
        continue
    return False


name = 'arcs_m2s'
if __name__ == '__main__': App(name).run()
