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


category = 'abstract'


from mcni.AbstractComponent import AbstractComponent

class ComponentGroup( AbstractComponent ):

    simple_description = 'A composite component that can group a bunch of components together'

    full_description = '''
    In various situtations, it is useful to group a few components
    together, each of them getting the same input neutrons.
    This is especially useful for legacy detector/monitor components.
    If in the simulation we need to simulate a few detector/monitor
    components intercepting the same neutron beam, we can use this
    composite component. Be careful, however, since this can only
    be used that the components in the group do not interfer (no
    multiple scattering among these components).

    Note: the neutrons passed to this group-component will not change
    when they exit
    '''

    __doc__ = simple_description + '\n' + full_description


    debug_logger = None
    

    def __init__(self, name, components, geometer, neutron_coords_transformer):
        AbstractComponent.__init__(self, name)
        self.components = components
        self.geometer = geometer
        self.neutron_coords_transformer = neutron_coords_transformer
        return


    def process(self, neutrons):
        geometer = self.geometer
        N = len(neutrons)
        for c in self.components:
            # make a copy
            copy = neutrons.snapshot(N)
            # transform coordinates of neutrons to the local
            # coordinate system of the sub component
            position = geometer.position(c)
            orientation = geometer.orientation(c)
            self.neutron_coords_transformer(
                copy, (0,0,0), (0,0,0),
                position, orientation)
            # send to sub-component
            if self.debug_logger:
                self.debug_logger("neutrons in subcomponent %s coordinate system: %s" % (
                        c.name, copy))
            c.process(copy)
            continue
        return neutrons

    pass # end of ComponentGroup


# version
__id__ = "$Id$"

# End of file 
