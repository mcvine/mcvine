#!/usr/bin/env python
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
utils for pyre inventory
'''


def getComponentPropertyTraits(comp, skipprops=[]):
    if not skipprops:
        skipprops = ['name', 'typos']
    r = []
    for prop in comp.inventory.propertyNames():
        if prop.startswith('help'): continue
        if prop in skipprops: continue
        trait = comp.inventory.getTrait(prop)
        r.append(trait)
        continue
    return r


def getComponentPropertyNameTipPairs(comp, skipprops=[]):
    traits = getComponentPropertyTraits(comp, skipprops=skipprops)
    return [(t.name, t.meta.get('tip') or t.name) for t in traits]


# version
__id__ = "$Id$"

# End of file 
