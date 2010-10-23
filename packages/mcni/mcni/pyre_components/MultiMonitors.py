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
    

    def process(self, neutrons):
        return self.engine.process(neutrons)


    def _init(self):
        super(MultiMonitors, self)._init()
        from mcni.components.ComponentGroup import ComponentGroup
        self.engine = ComponentGroup(self.name, self.monitors)
        return

    
    pass # end of MultiMonitor



# version
__id__ = "$Id$"

# End of file 
