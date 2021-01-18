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


from mcni.pyre_support import componentfactory

#def componentinfo(type, category=None, supplier=None):
def componentinfo(*args, **kwds):
    kwds = dict(kwds)
    type = kwds['type']; del kwds['type']
    category = kwds.get('category')
    if 'category' in kwds: del kwds['category']
    supplier = kwds.get('supplier')
    if 'supplier' in kwds: del kwds['supplier']
    
    # find the component factory and instantiate a componnet
    from mcni._find_component import find
    found = find(type, category=category, supplier=supplier)
    if found is None:
        msg = "Failed to find component (type=%s, category=%s, supplier=%s)" % (type, category, supplier)
        raise RuntimeError(msg)
    type, category, supplier = found
    factory = componentfactory(type=type, category=category, supplier=supplier)
    if hasattr(factory, 'factoryfactory'):
        factory = factory(*args, **kwds)
    comp = factory('component')
    # docs for parameters
    from mcni.pyre_support._invutils import getComponentPropertyNameTipPairs
    params = getComponentPropertyNameTipPairs(comp)
    l = ['  * %s: %s' % (k,v) for k,v in params]
    # title
    simple_description = comp.simple_description
    title = '%s: %s' % (type, simple_description)
    full_description = comp.full_description
    #
    startend = '='*70; separator = '-'*70
    l = [startend, title, separator, full_description, separator, 'Parameters:'] + l + [startend]
    #
    return '\n'.join(l)


# version
__id__ = "$Id$"

# End of file 
