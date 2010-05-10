# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


'''
factory to create an instrumnt pyre application class
from a list of component names.
'''


def build(components):
    
    from mcni.pyre_support.Instrument import Instrument as base
    class Instrument(base):

        class Inventory( base.Inventory ):

            from mcni.pyre_support import facility, componentfactory as component
            import mccomponents.pyre_support

            for name in components:
                code = '%s = facility("%s", default=component("optics", "Dummy")("%s") )' % (
                    name, name, name)
                exec code in locals()
                continue
            del code, name

            pass # end of Inventory


        def _defaults(self):
            base._defaults(self)
            self.inventory.sequence = components
            return

        pass # end of Instrument

    return Instrument


# version
__id__ = "$Id$"

# End of file 
