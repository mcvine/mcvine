#!/usr/bin/env python
#
#


# this is the original, minimal implementation of the Instrument data object
# it just contains a list of components
class Instrument0(object):

    '''Instrument is a container of neutron components'''

    def __init__(self, components = None ):
        self.components = components or []
        return


    def append(self, component):
        self.components.append(component)
        return


    def insert(self, index, component):
        self.components.insert(index, component)
        return

    pass # Instrument


# This class provides some syntatic sugar to simplify the
# procedure for users to create an instrument.
# It contains the geometer also.
class Instrument(Instrument0):

    '''Instrument is a container of neutron components, with a geometer'''

    def __init__(self, components = None, geometer = None):
        super(Instrument, self).__init__(components)
        self.geometer = geometer or self._createGeometer()
        return

    def simulate(self, N, **kwds):
        """simulate N neutrons. **kwds are used to update simulation context

simulation context is an instance of SimulationContext
"""
        # convenient method to run simulation
        from . import simulate, neutron_buffer
        neutrons = neutron_buffer(N)
        simulate(self, self.geometer, neutrons, **kwds)
        return neutrons

    def append(self, component, position=None, orientation=None, relativeTo=None):
        super(Instrument, self).append(component)
        if position is None and orientation is None: return
        self._register(component, position, orientation, relativeTo)
        return

    def insert(self, index, component, position=None, orientation=None, relativeTo=None):
        super(Instrument, self).insert(index, component)
        if position is None and orientation is None: return
        self._register(component, position, orientation, relativeTo)
        return

    def _register(self, component, position, orientation, relativeTo=None):
        from .Geometer2 import AbsoluteCoord as abs, RelativeCoord as rel
        if position is None: position = (0,0,0)
        if orientation is None: orientation = (0,0,0)
        if relativeTo:
            position = rel(position, relativeTo)
            orientation = rel(orientation, relativeTo)
        else:
            position = abs(position)
            orientation = abs(orientation)
        self.geometer.register(component, position, orientation)
        return

    def _createGeometer(self):
        from .Geometer2 import Geometer
        return Geometer()

    pass # Instrument


# End of file 
