#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


class Instrument:

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


# version
__id__ = "$Id$"

# End of file 
