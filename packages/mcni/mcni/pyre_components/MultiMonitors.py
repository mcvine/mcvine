#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


category = 'monitors'

from mcni.pyre_support.AbstractComponent import AbstractComponent

class MultiMonitors( AbstractComponent ):

    '''A group of monitors
    
    This is an abstract base class that need to be derived and
    initialize self.monitors correctly to work.
    
    This is useful for legacy detector/monitor components.
    If in the simulation we need to simulate a few detector/monitor
    components intercepting the same neutron beam, we can use this
    composite component. 

    Note: the neutrons passed to this group-component will not change
    when they exit.
    '''


    # derived component needs to overload this
    monitors = []


    class Inventory(AbstractComponent.Inventory):

        import pyre.inventory
        
        #geometer. this is a place holder. it got automatically
        #created in _defaults
        from mcni.pyre_support.Geometer import Geometer
        geometer = pyre.inventory.facility(
            'geometer', default = Geometer() )
        geometer.meta['tip'] = 'geometer of instrument'

    

    def process(self, neutrons):
        return self.engine.process(neutrons)


    def _defaults(self):
        super(MultiMonitors, self)._defaults()
        from mcni.pyre_support._geometer_utils import buildGeometerFromInventory
        # geometer_name='%s-geometer' % self.name
        geometer = buildGeometerFromInventory(
            self.Inventory)#, name=geometer_name)
        self.inventory.geometer = geometer
        return


    def init(self):
        if self._showHelpOnly:
            for m in self.monitors:
                m._showHelpOnly = True
                continue
            return
        outdir = self.getOutputDir()
        for m in self.monitors:
            m.setOutputDir(outdir)
            continue

        super(MultiMonitors, self).init()
        return


    def fini(self):
        if self._showHelpOnly:
            return

        super(MultiMonitors, self).fini()
        return


    def _init(self):
        super(MultiMonitors, self)._init()
        if self._showHelpOnly:
            return
        
        geometer = self.inventory.geometer
        from mcni.neutron_coordinates_transformers import default as transformer
        from mcni.components.ComponentGroup import ComponentGroup
        self.engine = ComponentGroup(self.name, self.monitors, geometer, transformer)
        return

    
    pass # end of MultiMonitor



# version
__id__ = "$Id$"

# End of file 
