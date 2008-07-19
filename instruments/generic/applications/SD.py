#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from mcni.pyre_support.Instrument import Instrument as base

class Instrument(base):

    class Inventory( base.Inventory ):

        from mcni.pyre_support import facility, componentfactory as component
        import mccomponents.pyre_support
        
        source = facility(
            'source',
            default = component('optics', 'Dummy')('source') )

        detector = facility(
            'detector',
            default = component( 'optics', 'Dummy')('detector') )
        
        pass # end of Inventory


    def __init__(self, name = 'SD'):
        base.__init__(self, name)
        return


    def _defaults(self):
        base._defaults(self)
        self.inventory.sequence = ['source', 'detector']
        return
    
    pass # end of Instrument


def main():
    app = Instrument()
    app.run()
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
