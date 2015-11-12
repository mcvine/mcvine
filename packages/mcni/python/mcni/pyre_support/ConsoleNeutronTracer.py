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

    
    def __call__(self, neutrons, context=None):
        if context:
            context.identify(self)

        for neutron in neutrons:
            print neutron
        print


    def onBefore(self, context):
        print 'Before entering %s' % context.obj


    def onProcessed(self, context):
        print 'After processed by %s' % context.obj


# version
__id__ = "$Id$"

# End of file 
