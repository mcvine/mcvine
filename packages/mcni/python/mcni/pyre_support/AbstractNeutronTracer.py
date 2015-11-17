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


from ..AbstractNeutronTracer import AbstractNeutronTracer as base
from pyre.components.Component import Component

class AbstractNeutronTracer(base, Component):

    def __init__(self, name, facility='neutron-tracer'):
        super(AbstractNeutronTracer, self).__init__(name, facility)
        return

    
# version
__id__ = "$Id$"

# End of file 
