#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def buildGeometer(componentnames):
    declarations = [
        8*' ' + '%s = Register("%s")' % (name, name) for name in componentnames ]
    declarations = '\n'.join( declarations )
    
    from Geometer import Geometer as base, Register
    code = '''
class Geometer1(base):
    class Inventory(base.Inventory):
%s
''' % declarations
    
    exec code in locals()
    
    return Geometer1()


def buildGeometerFromInventory(Inventory):
    #find all components
    componentnames = dir(Inventory)

    from NeutronComponentFacility import NeutronComponentFacility
    componentnames = filter(
        lambda name: isinstance(
            getattr(Inventory, name), NeutronComponentFacility ),
        componentnames )
    
    return buildGeometer(componentnames)


# version
__id__ = "$Id$"

# End of file 
