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


category = 'optics'

from mcni.pyre_support.AbstractComponent import AbstractComponent

class Dummy( AbstractComponent ):

    '''Dummy neutron component that does nothing'''

    def process(self, neutrons):
        return neutrons
    
    pass # end of Dummy



# version
__id__ = "$Id$"

# End of file 
