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


from pyre.components.Component import Component

class AbstractNeutronTracer(Component):

    def __init__(self, name, facility='neutron-tracer'):
        super(AbstractNeutronTracer, self).__init__(name, facility)
        return

    
    def __call__(self, neutrons):
        raise NotImplementedError        


# version
__id__ = "$Id$"

# End of file 
