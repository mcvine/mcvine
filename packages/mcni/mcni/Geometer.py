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

    '''Geometer holds geometrical info of elements relative to host'''

    def __init__(self):
        self._registry = {}
        return


    def register(self, element, position, orientation):
        self._registry[element] = position, orientation
        return


    def position(self, element):
        return self._registry[element][0]


    def orientation(self, element):
        return self._registry[element][1]

    pass # Geometer


# version
__id__ = "$Id$"

# End of file 
