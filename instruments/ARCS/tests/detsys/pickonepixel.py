#!/usr/bin/env python

import os
from mcvine import resources

def execute(cmd):
    print '* executing %s... ' % cmd
    if os.system(cmd):
        raise RuntimeError, "%r failed" % cmd

    
def run(
    ncount=100, 
    pixelID = 0,
    ei = 700,
    ):
    # read pixel position
    pixelpos = readPixelPosition(pixelID)
    
    # convert to mcstas coordinates
    vx,vy,vz = pixelpos
    vi = vy, vz, vx
    runsim(vi, ei, ncount)
    
    # get number of absorbed events
    eventsdat = 'out/events.dat'
    n = getNumberOfEvts(eventsdat, pixelID)
    print n
    return n


def readPixelPosition(pixelID):
    ppfile = 'pixelID2position.bin'
    ppfile = os.path.join(resources.instrument('ARCS'), 'reduction', ppfile)
    import numpy
    positions = numpy.fromfile(ppfile, 'double')
    positions.shape = -1,3
    return positions[pixelID]


def runsim(vi, ei, ncount):
    xml = os.path.join(resources.instrument('ARCS'), 'reduction', 'ARCS.xml.reduction.standard')
    # run main sim
    cmd = './sd --source.velocity="%s" --source.energy=%s --detector.instrumentxml=%s --ncount=%s' % (
        tuple(vi), ei, xml, ncount)
    execute(cmd)
    return


def getNumberOfEvts(filename, pixelID):
    from mccomponents.detector import event_utils 
    evts = event_utils.readEvents(filename)
    _ = lambda evt: evt['pixelID'] == pixelID
    return len(filter(_, evts))


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
        pixelID = pyre.inventory.int('pixelID', default=0)
        ei = pyre.inventory.float('ei', default=700)

        
    def main(self):
        ncount = self.inventory.ncount
        pixelID = self.inventory.pixelID
        ei = self.inventory.ei
        run(
            ncount=ncount, pixelID=pixelID, ei=ei,
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
