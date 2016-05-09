#!/usr/bin/env python

import os
from mcvine import resources

def execute(cmd):
    print '* executing %s... ' % cmd
    if os.system(cmd):
        raise RuntimeError, "%r failed" % cmd

    
def run(
    ncount=100, 
    vi=(0,0,1),
    ei = 700,
    ):
    # convert to mcstas coordinates
    vx,vy,vz = vi
    vi = vy, vz, vx
    xml = os.path.join(resources.instrument('ARCS'), 'reduction', 'ARCS.xml.reduction.standard')
    # run main sim
    cmd = './sd --source.velocity="%s" --source.energy=%s --detector.instrumentxml=%s --ncount=%s' % (
        tuple(vi), ei, xml, ncount)
    print ("running", cmd)
    execute(cmd)
    
    # reduce events to S(Q,E)
    eventsdat = 'out/events.dat'
    return


mod2sample_distance = 13.6


# constants
import pyre.units.length
import pyre.units.energy
import pyre.units.time
npixels = 117760 # number of pixels for ARCS
mod2sample=13.6*pyre.units.length.meter
mod_period=0.015*pyre.units.time.s # moderator period



from pyre.applications.Script import Script as AppBase
class App(AppBase):

    class Inventory(AppBase.Inventory):

        import pyre.inventory
        ncount = pyre.inventory.float('ncount', default=1e7)
        vi = pyre.inventory.array('vi', default=[0,0,1])
        ei = pyre.inventory.float('ei', default=700)

        
    def main(self):
        ncount = self.inventory.ncount
        vi = self.inventory.vi
        ei = self.inventory.ei
        run(
            ncount=ncount, vi=vi, ei=ei,
            )
        return
    

def main():
    app = App('sim')
    app.run()
    return


interactive = False

if __name__ == '__main__': 
    interactive = True
    main()
