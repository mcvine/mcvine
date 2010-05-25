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

def componentinfo(type, category=None, supplier=None):
    # find the component factory and instantiate a componnet
    from mcni._find_component import find
    type, category, supplier = find(type, category=category, supplier=supplier)
    factory = componentfactory(type=type, category=category, supplier=supplier)
    comp = factory(name='component')
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
