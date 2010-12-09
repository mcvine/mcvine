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


from AbstractNeutronTracer import AbstractNeutronTracer as base

class ConsoleNeutronTracer(base):

    def __init__(self, name='console-neutron-tracer'):
        super(ConsoleNeutronTracer, self).__init__(name)
        return

    
    def __call__(self, neutrons):
        for neutron in neutrons:
            print neutron
        print

# version
__id__ = "$Id$"

# End of file 
