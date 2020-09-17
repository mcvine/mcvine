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


def buildGeometer(componentnames, name=None):
    geometer_name = name or 'geometer'
    declarations = [
        8*' ' + '%s = Register("%s")' % (name, name) for name in componentnames ]
    declarations = '\n'.join( declarations )
    
    from .Geometer import Geometer as base, Register
    code = '''
class Geometer1(base):
    class Inventory(base.Inventory):
%s
''' % declarations
    # not sure why but for py2 have to use combination of g and l instead of just l itself
    g, l = globals(), locals()
    g.update(l)
    exec(code, g)
    Geometer1 = g['Geometer1']
    return Geometer1(geometer_name)


def buildGeometerFromInventory(Inventory, name=None):
    #find all components
    componentnames = dir(Inventory)

    from .NeutronComponentFacility import NeutronComponentFacility
    componentnames = [cname for cname in componentnames if isinstance(
            getattr(Inventory, cname), NeutronComponentFacility )]
    
    return buildGeometer(componentnames, name=name)


# version
__id__ = "$Id$"

# End of file 
