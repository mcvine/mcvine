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


class Geometer:

    '''Geometer holds geometrical info about an instrument'''

    def __init__(self):
        self._registry = {}
        return


    def register(self, component, position, orientation):
        self._registry[component] = position, orientation
        return


    def position(self, component):
        return self._registry[component][0]


    def orientation(self, component):
        return self._registry[component][1]

    pass # Geometer


# version
__id__ = "$Id$"

# End of file 
